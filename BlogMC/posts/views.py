from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your tests here.

posts = [
    {
        'id': 1,
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'id': 2,
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'id': 3,
        'author': 'John',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 30, 2018'
    }

]


def home(request):
    html = ""
    for post in posts:
        html += f'''
        <div>
        <a href="/post/{post['id']}">
        <h1>{post['id']} - {post['title']}</h1>
        </a>
        <p>{post['content']}</p>
        <p>{post['date_posted']}</p>
        <p>{post['author']}</p>
        </div>
        '''
    return render(request, 'home.html')

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        html = f'''
            <h1>{post_dict['title']}</h1>
            <p>{post_dict['content']}</p>
            <p>{post_dict['date_posted']}</p>
            <p>{post_dict['author']}</p>
              '''
        return HttpResponse(html)
    else:
        raise Http404('Post not found 😥')