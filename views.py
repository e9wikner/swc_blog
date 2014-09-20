from datetime import date
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import DateField
from swc_blog.models import Post

# Create your views here.


def index(request):
    return render_to_response('index.html', {'posts': Post.objects.all()})


def archive(request):
    return render_to_response('archive.html', {'posts': Post.objects.all()})


def about(request):
    return render_to_response('about.html')


def view_post(request, year, month, day, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(
            Post, pub_date=date(int(year), int(month), int(day)), slug=slug)
    })