from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models.signals import post_save
import json
from tindeers.models import Product, UserProfile,Rating
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


def _process_school(schools):
    return 'college'


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


# No server side Ziggeo should be need at the time
# Can get the video merely with the id which is gotten
# via the script client side


def main_page(request):
    return render(request, 'tindeers/base.html', {})


def create(request):
    return render(request, 'tindeers/create.html', {})


def create_api(request):
    video = request.POST.get('video', None)
    description = request.POST.get('desc', None)
    title = request.POST.get('title', None)
    response_data = {}
    if video and title and description:
        p = Product.objects.create(video_link=video,
                                   description=description,
                                   title=title,
                                   creator_id=request.user.pk)
        response_data["product"] = p.pk
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")

def vote(request):
	pid = request.POST.get('pid', None)
	liked = request.POST.get('liked', None)
	print request.user.is_superuser
	currentUserProfile = request.user.userprofile
	if not pid or not liked:
		raise Http404("Must pass both a Product ID and a vote")
	prod = Product.objects.get(pk=int(pid))
	if prod.raters.filter(user=currentUserProfile).exists():
		return HttpResponse(json.dumps({'error':'Cannot vote again for this product'}),
                        content_type="application/json")
	else:
		r = Rating(liked=bool(liked),rater=currentUserProfile,product =prod)
		r.save()
		return HttpResponse(json.dumps({'success':'Voted successfully for product'}),
                        content_type="application/json")



def display(request, vid):
    p = get_object_or_404(Product, pk=vid)
    return render(request, 'tindeers/display.html', {'p': p})
