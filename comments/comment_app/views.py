
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.list import ListView

from comment_app.forms import (Addcomment, CustomAuthenticationForm,
                               CustomUserCreationForm)
from comment_app.models import Comment, User


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    
    template_name = "register.html"
    
class Login(LoginView):

    authentication_form = CustomAuthenticationForm

    form_class = CustomAuthenticationForm
    success_url = reverse_lazy("home/")
    template_name = 'login.html'

    def form_valid(self, form):


        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)
    
class CommentListView(LoginRequiredMixin,ListView):
    paginate_by = 3
    model= Comment
    template_name = "index.html"
    def get_queryset(self):
        
        queryset=Comment.objects.all().order_by('-id')
        return queryset

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
    
    
class AddCommentView(LoginRequiredMixin,FormView):
    form_class = Addcomment
    success_url = reverse_lazy("home/")
    template_name = "home"
    def post(self, request):
        comment='none'
        log=Addcomment(request.POST)
        if log.is_valid():

            comment=log.cleaned_data['Comment']

            user=User.objects.get(username=request.user)
            if user:
                comments=Comment(Comment=comment,user=user)
                comments.save()
            return redirect('home/')
        else:
            return render(request,'index.html',{'comment': False})
        
class CommentDeleteView(LoginRequiredMixin,DeleteView):
   model=Comment
   template_name='index.html'
   success_url=reverse_lazy("home")