from django.shortcuts import render
from pennapps import Ziggeo


# No server side Ziggeo should be need at the time
# Can get the video merely with the id which is gotten
# via the script client side


def main_page(request):
    return render(request, 'tindeers/base.html', {})

def create(request):
    return render(request, 'tindeers/create.html', {})
