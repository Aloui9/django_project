
from django.db.models.query import QuerySet
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from blog.models import Post
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class PostListView(ListView,LoginRequiredMixin):
    # model = Post
    template_name = "dashbord/dashbord.html"
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__id=user.id)
    

class PostCreateView(CreateView):
    model=Post
    template_name ="dashbord/new_post.html"
    fields=["title","body"]

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('dashbord:post_list')

    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name ="dashbord/update_post.html"
    fields=["title","body"]

    def form_valid(self,form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('dashbord:post_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class PostDeleteView(DeleteView):
    model=Post
    template_name ="dashbord/delete_post.html"
    success_url = reverse_lazy("dashbord:post_list")

