"""Imports"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import CommentForm, PostForm, CategoryForm
# Create your views here.


class PostList(generic.ListView):
    """PostList Model created from generic view"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetail(View):
    """Post Detail class to show single post after clicking on it"""

    def get(self, request, slug, *args, **kwargs):
        """function to get specific post"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(request, "post_detail.html", {
            "post": post,
            "comments": comments,
            "liked": liked,
            "comment_form": CommentForm()
        },)
    def post(self, request, slug, *args, **kwargs):
        """function to post comment"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request, "post_detail.html", {
            "post": post,
            "comments": comments,
            "liked": liked,
            "comment_form": CommentForm()
        },)

class PostLike(View):
    """PostLike Class View"""
    def post(self, request, slug):
        """post function"""
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(generic.CreateView):
    """Create new Blog Post"""
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePost(generic.UpdateView):
    """to update the blog"""
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'


class DeltePost(generic.DeleteView):
    """To Delte the Blog"""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategory(generic.CreateView):
    """To add Categories"""
    model = Category
    template_name = 'add_category.html'
    form_class = CategoryForm


class CategoryListView(generic.ListView):
    """To show the categories"""
    template_name = 'category_detail.html'
    context_object_name = 'categorylist'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryListView,
        self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter
            (category__name=self.kwargs['category']).filter(status=1)
        }
        return content
