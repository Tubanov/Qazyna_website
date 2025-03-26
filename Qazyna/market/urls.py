from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.market, name='market'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/update', views.ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete')
]

