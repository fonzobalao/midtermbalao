from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    post = Post.object.all()
    context['posts'] = posts
    return render(request, 'index.html', context)

def detail(request):
    pass

def create(request):
    pass

def update(request):
    pass

def comment(request):
    pass
