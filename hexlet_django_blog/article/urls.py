from django.urls import path

from hexlet_django_blog.article.views import ArticleView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:id>', ArticleView.as_view(), name='show'),
]
