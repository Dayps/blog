from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, Comment
from .forms import CommentForm
from .models import Category

# Categoria Individual: criar uma view para exibir uma categoria INDIVIDUAIS e seus posts associados.
def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = category.post_set.all()
    return render(request, 'category_detail.html', {'category': category, 'posts': posts})

# Listagem de Categorias: criar uma view para listar TODAS as categorias.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/comment_new.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = post.categories.all()
    return render(request, 'posts/post_detail.html', {'post': post, 'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-date_posted')
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})
 
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})

def post_list(request):
    # Busca todos os posts no banco de dados
    posts = Post.objects.all()
    # Renderiza o template 'post_list.html', passando os posts como contexto
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

