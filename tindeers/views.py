from django.shortcuts import render
from pennapps import Ziggeo

def main_page(request):
    return render(request, 'tindeers/base.html', {})
