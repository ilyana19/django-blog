from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture

def root(request):
  return HttpResponseRedirect('pictures')

def picture(request):
  context = {
    'pictures': Picture.objects.all(),
    'title': 'Django Photogur',
  }
  response = render(request, 'pictures.html', context)
  return HttpResponse(response)

def picture_show(request, pic_id):
  picture = Picture.objects.get(id=pic_id)
  comments = picture.comments.order_by("-created_at")
  context = {
    'picture': picture,
    'comments': comments,
    'title': picture.title,
  }
  response = render(request, 'picture.html', context)
  return HttpResponse(response)

def picture_search(request):
  query = request.GET['query']
  search_results = Picture.objects.filter(artist=query)
  context = {
    'pictures': search_results,
    'title': 'Search Results',
    'query': query
  }
  response = render(request, 'results.html', context)
  return HttpResponse(response)

def comment_create(request):
  pass