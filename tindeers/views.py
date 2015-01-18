from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import json
from tindeers.models import Product, UserProfile,Rating,Comment
from social.apps.django_app.default.models import UserSocialAuth
from django.utils.timezone import now
from django.http import Http404
import datetime
import facebook


def _process_age(birthday):
    birthdate = datetime.datetime.strptime(birthday, '%m/%d/%Y').date()
    current_date = now().date()

    delta = current_date - birthdate

    return delta.days / 365

def process_edu(edu_array):
    schools = {"High School": 0, "College": 1, "Graduate School": 2}
    level = ["High School", "College", "Graduate School"]
    best = 0
    for school in edu_array:
        ty = school["type"]
        if ty in schools and schools[ty] > best:
            best = schools[ty]
    return level[best]



def get_facebook_info(sender, instance, created, **kwargs):
    print(instance.extra_data)
    user = instance.user
    try:
        user.userprofile
    except UserProfile.DoesNotExist:
        try:
            graph = facebook.GraphAPI(instance.extra_data['access_token'])
            data = graph.get_object("me")
            print (data)
            UserProfile(age=_process_age(data['birthday']),
                        gender=data['gender'],
                        education=process_edu(data['education']),
                        relationship_status=data['relationship_status'],
                        location=data['location']['name'].split(',')[1].strip(),
                        user=user).save()
        except KeyError:
            print('well, balls')


post_save.connect(get_facebook_info,
                  sender=UserSocialAuth,
                  dispatch_uid='create_user_profile')


def main_page(request):
    return render(request, 'tindeers/ideadash.html', {'home': 'active'})


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def explore(request):
    uprofile = request.user.userprofile
    dont_get_these = uprofile.my_products.values_list('pk', flat=True)
    dont_get_these |= uprofile.my_rated_products.values_list('pk', flat=True)
    product = Product.objects.exclude(id__in=dont_get_these).first()
    return render(request, 'tindeers/swiper.html', {'explore': 'active',
                                                    'product': product})


def landing(request):
    if request.user.is_authenticated():
        return redirect('/home')
    return render(request, 'tindeers/landing.html',{})


@login_required
def create(request):
    return render(request, 'tindeers/create.html', {'mydea': 'active'})


@login_required
def feedback(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    if p.creator.user.pk != request.user.pk:
        return render(request, 'tindeers/not_yours.html', {})

    positive_reviews = UserProfile.objects.filter(my_rated_products__pk=p.pk,
                                                  rating__liked=True)
    negative_reviews = UserProfile.objects.filter(my_rated_products__pk=p.pk,
                                                  rating__liked=False)

    template_params = {
        'product': p,
        'mydea': 'active',
        'negative_reviews': negative_reviews,
        'positive_reviews': positive_reviews
    }
    return render(request, 'tindeers/ideadash.html', template_params)


@login_required
def manage_all(request):
    all_ideas = request.user.userprofile.my_products.all()

    for idea in all_ideas:
        idea.positive = 10  # idea.raters.filter('') / idea.raters.count()

    return render(request, 'tindeers/ideamanage.html', {'ideas': all_ideas,
                                                        'mydea': 'active'})


@login_required
def create_api(request):
    video = request.POST.get('video', None)
    description = request.POST.get('desc', None)
    title = request.POST.get('title', None)
    url = request.POST.get('url', None)
    response_data = {}
    if video and title and description:
        p = Product.objects.create(video_link=video,
                                   description=description,
                                   title=title,
                                   product_link=url,
                                   creator_id=request.user.pk)
        response_data["product"] = p.pk
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")

@login_required
def vote(request):
    pid = request.POST.get('pid', None)
    liked = request.POST.get('liked', None)
    currentUserProfile = request.user.userprofile
    if not pid or not liked:
        raise Http404("Must pass both a Product ID and a vote")
    prod = Product.objects.get(pk=int(pid))
    if prod.creator.pk == currentUserProfile.pk or prod.raters.filter(user=currentUserProfile).exists():
        return HttpResponse(json.dumps({'error':'Cannot vote again for this product'}),
                            content_type="application/json")
    else:
        r = Rating(liked=bool(liked),rater=currentUserProfile,product =prod)
        r.save()
        return HttpResponse(json.dumps({'success':'Voted successfully for product'}),
                        content_type="application/json")


@login_required
def display(request, vid):
    p = get_object_or_404(Product, pk=vid)
    return render(request, 'tindeers/display.html', {'p': p})

@login_required
def aggregate(request,pid):
    # pid is a product id specified by the url
    p = get_object_or_404(Product, pk=pid)

    product_ratings = Rating.objects.filter(product=p)

    data = {"gender":
                {"yes": {"male":0, "female":0,"eunuch":0},
                "no": {"male":0, "female":0,"eunuch":0}},
            "location":{"yes": {},
                "no": {}},
            "age":{"yes": {},
                "no": {}},
            "education":{"yes": { "HS":0,"CO":0,"GS":0},
                    "no": { "HS":0,"CO":0,"GS":0}},
            "relationship":{"yes": {},
                "no": {}}
            }

    for r in product_ratings:
        person = r.rater
        if r.liked:
            liked = "yes"
        else:
            liked = "no"

        if person.gender not in ["male","female"]:
            data["gender"][liked]["eunuch"] += 1
        else:
            data["gender"][liked][person.gender] += 1

        if person.location in data["location"][liked]:
            data["location"][liked][person.location] += 1
        else:
            data["location"][liked][person.location] = 1

        if person.age in data["age"][liked]:
            data["age"][liked][person.age] += 1
        else:
            data["age"][liked][person.age] = 1

        if person.education in data["education"][liked]:
            data["education"][liked][person.education] += 1
        else:
            data["education"][liked][person.education] = 1

        if person.relationship_status in data["relationship"][liked]:
            data["relationship"][liked][person.relationship_status] += 1
        else:
            data["relationship"][liked][person.relationship_status] = 1

    return HttpResponse(json.dumps(data),
                        content_type="application/json")



@login_required
def comment(request,pid):
    #pid is the product id which is being commented on
    p = get_object_or_404(Product, pk=pid)
    body = request.POST.get('msg', None)
    if not body:
        raise Http404("Must pass a body of the comment")
    if not 0 < len(body) < 200:
        raise HttpResponse("Need a body", status_code=400)
    currentUserProfile = request.user.userprofile
    com = Comment.objects.create(product=p,
                                   text=body,
                                   comment_time=now(),
                                   author=currentUserProfile)
    com.save()
    response_data = {}
    response_data["comment"] = com.pk
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
