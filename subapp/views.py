from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json)
    posts = Post.objects.all()[:25]
    return render(request, 'post.html', {'posts':posts})


def delete(request, post_id):
    post  = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

    
   