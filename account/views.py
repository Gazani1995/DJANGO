from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView
from blog.models import Article
from .mixins import FieldsMixin , FormValidMixin

# Create your views here.
# @login_required
# def home(request):
#     return render(request , 'registration/home.html')

class ArticleList(LoginRequiredMixin , ListView):
    template_name= 'registration/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author= self.request.user)


class ArticleCreate(LoginRequiredMixin,FieldsMixin ,FormValidMixin, CreateView):
    model = Article
    template_name= 'registration/article-create-update.html'



def profile(request):
    return render(request , 'registration/profile.html')