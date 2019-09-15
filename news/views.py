from django.shortcuts import render
from news.models import Story, Comment
from news.forms import CommentForm

def news_index(request):
    stories = Story.objects.all().order_by('-created_on')
    context = {
        "stories": stories,
    }
    return render(request, "news_index.html", context)

def news_category(request, category):
    stories = Story.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    context = {
        "category": category,
        "stories": stories
    }
    return render(request, "news_category.html", context)

def news_detail(request, pk):
    story = Story.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "story": story,
        "comments": comments,
        "form": form
    }
    return render(request, "news_detail.html", context)
