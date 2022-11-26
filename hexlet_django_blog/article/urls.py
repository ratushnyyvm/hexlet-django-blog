from django.urls import path

from hexlet_django_blog.article.views import (ArticleFormCreateView,
                                              ArticleFormDeleteView,
                                              ArticleFormUpdateView,
                                              ArticleView, IndexView)

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index',
    ),
    path(
        '<int:id>/',
        ArticleView.as_view(),
        name='show',
    ),
    path(
        'create/',
        ArticleFormCreateView.as_view(),
        name='articles_create',
    ),
    path(
        '<int:id>/update/',
        ArticleFormUpdateView.as_view(),
        name='articles_update',
    ),
    path(
        '<int:id>/delete',
        ArticleFormDeleteView.as_view(),
        name='articles_delete',
    ),
]
