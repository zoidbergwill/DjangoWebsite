from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import (BlogCategory, BlogPost)
from apps.utils.functions import get_total_pages


def blog(request, page_number=1):
    '''
        Renders the blog.html view which is used as base blog page i.e
        url path is www.umonya.org/blog/
        or www.umonya.org/blog/page<page_number>/
    '''
    blog_categories = BlogCategory.objects.all()
    page_number = int(page_number)
    blog_posts = BlogPost.objects.order_by('-pub_date')
    total_blog_posts = len(blog_posts)

    # gets section of blog posts wanted for page
    blog_posts = blog_posts[((page_number - 1) * 5):page_number * 5]
    total_pages = get_total_pages(total_blog_posts)

    prev = '/blog/page%s/' % (str(page_number - 1))
    next = '/blog/page%s/' % (str(page_number + 1))
    path = '/blog/page'

    return render_to_response(
        'blog.html',
        {'blog_posts': blog_posts,
        'blog_categories': blog_categories,
        'page_number': page_number,
        'total_pages': total_pages,
        'prev': prev,
        'next': next,
        'path': path},
        context_instance=RequestContext(request))


def blog_category(request, slug, page_number=1):
    '''
        Renders the blog.html with only the posts from the specific category.i.e
        url path is www.umonya.org/blog/category/<slug>
        or www.umonya.org/blog/category/<slug>/page<page_number>/

    '''
    blog_categories = BlogCategory.objects.all()
    page_number = int(page_number)
    blog_posts = BlogPost.objects.order_by('-pub_date').filter(category__name=slug)
    total_blog_posts = len(blog_posts)

    # gets section of announcements wanted for page
    if total_blog_posts > 5:
        blog_posts = blog_posts[(page_number * 5)-5:page_number * 5]
        # get page numbers, and total pages
        total_pages = total_blog_posts // 5
        total_pages += total_blog_posts % 5 and 1 or 0
    else:
        blog_posts = blog_posts[:total_blog_posts]
        total_pages = 1
    prev = str(page_number - 1)
    next = str(page_number + 1)
    host = request.get_full_path()
    host_s = host.split('/')
    if len(host_s) > 2:
        if host_s[1] == 'blog':
            prev = 'page%s/' % (prev)
            next = 'page%s/' % (next)
            path = ''
    else:
        prev = 'blog/page%s/' % (prev)
        next = 'blog/page%s/' % (next)
        path = 'blog/'
    return render_to_response(
        'blog.html',
        {'blog_posts': blog_posts,
        'blog_categories': blog_categories,
        'page_number': page_number,
        'total_pages': total_pages,
        'prev': prev,
        'next': next,
        'path': path},
        context_instance=RequestContext(request))


def view_blogpost(request, page_number, slug):
    '''
        Renders the view_blogpost.html view which is used
        to show individual blog posts
        i.e. url path is www.umonya.org/blog/page<page_number>/<slug> .
        The blog post is found by the slug stored in the database
    '''
    blog_categories = BlogCategory.objects.all()
    blog_post = get_object_or_404(BlogPost, slug=slug)
    return render_to_response('view_blogpost.html', {
        'blog_post': blog_post,
        'blog_categories': blog_categories,
        'page_number': page_number})
