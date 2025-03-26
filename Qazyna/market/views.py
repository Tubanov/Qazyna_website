from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Article
from django.views.generic import DetailView, UpdateView, DeleteView
from login.forms import ArticleForm


def market(request):
    market = Article.objects.all()
    return render(request, 'market/market.html', {'market':market})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'market/article_detail.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'login/add.html'
    form_class = ArticleForm

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('market:market')
    template_name = 'login/delete.html'





