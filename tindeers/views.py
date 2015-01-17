from django.shortcuts import render,HttpResponse
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
	video = request.POST.get('video',None)
	if not video:
		video = request.GET.get('video',None)
	response_data = {}
	if video:
		p = Product()
		p.video_link = video
		p.description = "abc"
		p.title = "TITLE"
		p.creator_id = 1
		p.save()
		response_data["product"] = p.id
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def display(request,vid):
	p = Product.objects.get(pk=vid)
	return render(request, 'tindeers/display.html', {'video_id':p.video_link})