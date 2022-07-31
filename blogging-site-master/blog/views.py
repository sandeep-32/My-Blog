from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from blog.models import post,comment
from blog.forms import postForm,commetForm
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,
                                  ListView,DetailView,
                                  UpdateView,DeleteView)

# Create your views here.

class aboutview(TemplateView):
    template_name='blog/about.html'

class postlistview(ListView):

    model=post
    template_name='blog/post_list.html'

    def  get_queryset(self):
        return post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class postdetailview(DetailView):
    template_name='blog/post_detail.html'
    model=post
class postcreateview(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=postForm

    model=post

class postupdateview(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=postForm

    model=post


class postdeleteview(LoginRequiredMixin,DeleteView):
    model=post
    success_url=reverse_lazy('post_list')

class draftlistviews(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post_draft_list.html'
    model=post

    def get_queryset(self):
        return post.objects.filter(published_date__isnull=True).order_by('create_date')






##################################################
##################################################
@login_required
def post_publish(reqeust,pk):
    Post=get_object_or_404(post, pk=pk)
    Post.publish()
    return redirect('post_detail', pk=pk)



@login_required
def add_comment_to_post(request, pk):
    form="dummy strung"
    Post=get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form=commetForm(request.POST)
        if form.is_valid():
            Comment=form.save(commit=False)
            Comment.Post=Post
            Comment.save()
            return redirect('post_detail', pk=Post.pk)
    else:
        form=commetForm()


    return render(request,'blog/post_comment.html',{'form': form})


@login_required
def comment_approve(reqeust, pk):
    Comment=get_object_or_404(comment, pk=pk)
    Comment.approve()
    return redirect('post_detail', pk=Comment.Post.pk)
@login_required
def comment_remove(request,pk):
    Comment=get_object_or_404(comment, pk=pk)
    post_pk=Comment.Post.pk
    Comment.delete()
    return redirect('post_detail', pk=post_pk)
