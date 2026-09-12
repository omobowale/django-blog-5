from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# posts = [
#     {
#         'title': "My first post",
#         'content': "This is my first post and I hope you do like it"
#     },
#     {
#         'title': "My second post",
#         'content': "This is my second post and I hope you do like it"
#     },
#     {
#         'title': "My third post",
#         'content': "This is my third post and I hope you do like it"
#     }
# ]

# Create your views here.
@login_required
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


@login_required
def create_post(request):
    
    if request.method == "POST":
        # get form data => get data from form. 
        form = PostForm(request.POST)
        
        if form.is_valid():
            # submit to db
            form.save()
            
            # redirect to all posts
            return redirect('all_posts')
        
        else:
            print(form.errors)
        
  
    else:
        # create a form
        form = PostForm()
    
    return render(request, 'create_post.html', {"form": form})


def single_post(request, post_id):
    # fetch the post that has that id
    post = Post.objects.get(id=post_id)
    
    return render(request, 'single_post.html', {"post": post})
    
    
    