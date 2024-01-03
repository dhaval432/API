from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Blog
# from django.forms import blog_form , CommentForm
from .models import*
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    data = {'key':'value'}
    return JsonResponse(getData)
# def blog_list(request):
#     blogs = Blog.objects.all()
#     return render(request, 'blog/blog_list.html', {'blogs': blogs})

# def blog_detail(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     comments = blog.comments.all()
    
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.blog = blog
#             new_comment.save()
#             return redirect('blog_detail', pk=pk)
#     else:
#         comment_form = CommentForm()

#     return render(request, 'blog/blog_detail.html', {'blog': blog, 'comments': comments, 'comment_form': comment_form})

# def add_blog(request):
#     if request.method == 'POST':
#         blog_form = blog_form(request.POST, request.FILES)
#         if blog_form.is_valid():
#             blog_form.save()
#             return redirect('blog_list')
#     else:
#         blog_form = blog_form()

#     return render(request, 'blog/add_blog.html', {'blog_form': blog_form})


blogs = [
    {
        'id': 1,
        'title': 'Anime',
        'content': "Its Izuku Midoriya. world's great heroes successor none other than All Might",
        'image': '1296475.jpg',
        'author': 'Neel Kapur',
        'timestamp': '3 mins ago',
        'comments': [],
    },
    {
        'id': 2,
        'title': 'Natural Scenery',
        'content': 'This is very peaceful natural scenery.',
        'image': 'photo-1473448912268-2022ce9509d8.avif',
        'author': 'Martin Kingsman',
        'timestamp': '5 mins ago',
        'comments': [],
    },
    {
        'id': 3,
        'title': 'Movie Talkies',
        'content': 'Its Aquaman and the lost kingdom. main characters in movies are Jason Momoa, Amber Heard, many.',
        'image': '106154636.webp',
        'author': 'Unknown',
        'timestamp': '3 mins ago',
        'comments': [],
    },
]

def home(request):
    return render(request, 'index.html', {'blogs': blogs})

def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content= request.POST.get('content')
        image = request.POST.get('image')

        # Add the new blog to the list (in a real application, you would save to a database)
        new_blog = {
            'id': len(blogs) + 1,
            'title': title,
            'content': content,
            'image': image,
            'author': 'Anonymous',
            'timestamp': 'Just now',
            'comments': [],
        }
        blogs.append(new_blog)

        return JsonResponse({'status': 'success', 'blog_id': new_blog['id']})
    else:
        return JsonResponse({'status': 'error'})

def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = next((b for b in blogs if b['id'] == blog_id), None)
        if blog:
            comment_text = request.POST.get('comment')
            if comment_text:
                comment = {
                    'text': comment_text,
                    'timestamp': 'Just now',
                }
                blog['comments'].append(comment)
                return JsonResponse({'status': 'success', 'comment': comment})
            else:
                return JsonResponse({'status': 'error', 'message': 'Comment text is required'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Blog not found'})
    else:
        return JsonResponse({'status': 'error'})

def delete_blog(request, blog_id):
    global blogs
    blogs = [b for b in blogs if b['id'] != blog_id]
    return redirect('home')



