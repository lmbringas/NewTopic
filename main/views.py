from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from models import Post , Comment , Author
from django.contrib.auth.models import User
import json
# Create your views here.


def home(request):
    '''
    codigo para ajax
    TOTAL = 5
    OFFSET = int(request.GET.get('offset', 0))
    END = OFFSET + TOTAL
    if request.method == 'GET' and request.is_ajax():
        print "hola"
        posts = Post.objects.all()[OFFSET:END]
        json_list = []
        for post in posts:
            json_list.append({
                    'title': post.title, 'content': post.content,'id':post.id
                })
        data = json.dumps(json_list)
        return HttpResponse(data,content_type='application/json')
    '''
    context = RequestContext(request)
    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        nPost = Post()
        nPost.title = title
        nPost.content = content
        nPost.publicated = True
        user = User.objects.get(pk = request.user.id)
        nPost.author = Author.objects.get(user=user)
        nPost.save()
    posts = Post.objects.all()
    context['posts'] = posts
    return render_to_response("index.html", context)

@login_required(login_url="/log")
def post(request,id_post):
    context = RequestContext(request)
    post = Post.objects.get(pk=id_post)
    if request.method == 'POST':
        comment = request.POST['comment']
        ncomment = Comment()
        ncomment.author = User.objects.get(pk = request.user.id)
        ncomment.post = post
        ncomment.comment = comment
        ncomment.approved = True
        ncomment.save()
    comments = Comment.objects.all().filter(post=id_post) #select * from commets where id_post = id_post
    context['post'] = post
    context['comments'] = comments
    return render_to_response("post.html",context)

def ownPost(request):
    context = RequestContext(request)
    user = User.objects.get(pk = request.user.id)
    author = Author.objects.get(user=user)
    posts = Post.objects.filter(author=author)
    context['posts'] = posts
    return render_to_response("index.html", context)
