from django.shortcuts import render,get_object_or_404
from .models import Post             # . -> means from current package-KK
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView # inbuilt view for class based view creations-KK
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin # alternative to decorator(@login_required) as decorators can't be used on class-class based views-KK
from django.contrib.auth.models import User


# posts=[
#     {
#         'author':'Kushal',
#         'title':'Blog Post-1',
#         'content':'First post content',
#         'date-posted':'June 17,2020'

#     },
#     {
#         'author':'Ullas',
#         'title':'Blog Post-2',
#         'content':'Second post content',
#         'date-posted':'June 18,2020'

#     }
#     ]

def home(request):
    context={
        # 'posts'posts
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})  

# Above function based view for home url is not in use.Kept just to see the two varities-KK

#class based views
class PostListView(LoginRequiredMixin,ListView):
    model=Post # related model - KK
    template_name='blog/home.html' #format for template name --> <app>/<model>_<viewtype>.html [here: djBlog/post_home.html] 
    context_object_name='posts'  # providing context to understand better - KK
    ordering=['-date_posted'] # reversing the order of posts/here to make the latest one available at top-KK
    paginate_by=5 # paginating the posts,limiting 5 posts/page-KK

class PostDetailView(DetailView):
    model=Post
    template_name='blog/post_detail.html' #only specify otherwise, default expected format for template name --> <app>/<model>_<viewtype>.html [here: djBlog/post_detail.html] 

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    template_name='blog/post_form.html'

    def form_valid(self, form): # inbuilt method to check the validity of the form-KK
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    template_name='blog/post_form.html'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self): #inbuilt method to test function
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False       


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='blog/post_confirm_delete.html'
    success_url='/'
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False   

class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html' 
    context_object_name='posts'
    paginate_by=5

    def get_queryset(self): #inbuilt method to query
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')