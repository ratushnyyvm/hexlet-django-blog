# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View


def index(request):
    return redirect('article', tags='python', article_id=42)


class IndexView(View):

    def get(self, request, tags, article_id):
        if tags and article_id:
            return render(
                request,
                'article/index.html',
                context={
                    'tags': tags,
                    'article_id': article_id,
                }
            )
