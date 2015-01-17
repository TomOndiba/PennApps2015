from django.shortcuts import render, HttpResponse, get_object_or_404
import json
from tindeers.models import Product


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
        p = Product()
        p.video_link = video
        p.description = description
        p.title = title
        p.creator_id = 1
        p.save()
        response_data["product"] = p.id
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")


def display(request, vid):
    p = get_object_or_404(Product, pk=vid)
    return render(request, 'tindeers/display.html', {'p': p})
