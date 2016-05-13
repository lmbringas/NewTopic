from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
# Create your views here.
from models import Post

def home(request):
    context = RequestContext(request)
    posts = Post.objects.all()
    context['usuario_actual'] = request.user
    context['posts'] = posts
    return render_to_response("index.html", context)

def post(request,id_post):
    return render_to_response("post.html",context)
