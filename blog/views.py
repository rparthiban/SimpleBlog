from django.shortcuts import render

from models import Blog, CATEGORIES
# Create your views here.


def index(request, *args, **kwargs):
    context = {'categories': CATEGORIES}
    if request.method == "POST":
	    content = request.POST.get('content')
	    title = request.POST.get('title') or None
	    user = request.POST.get('user') or None
	    category = request.POST.get('category')
	    try:
	        b = Blog(content=content, title=title, user=user, category=category)
	        b.save()
	    except Exception as why:
	        context['error'] = why
    context['blogs'] = Blog.objects.filter(accepted=True)
    return render(request, 'index.html', context)
