from django.shortcuts import render
from django.views.generic import ListView, DetailView
#from django.http import HttpResponse
from django.views import generic
from news.models import Post
from news.models import Side
from news.models import Rating
from news.models import News_category1
from news.models import News_category2
from news.models import News_middel
from news.models import News_bottam
from news.models import Game_up
from news.models import Game_bottam
from news.models import Review
# Create your views here.

#def index (request):
    #return render(request, 'news/news2.html')

"""class News_View(ListView):
    template_name = "news/news2.html"
    context_object_name = 'news_list'

    def get_queryset(self):
        return News_category1.objects.all().order_by("-id")[:2]
"""

class News_View(ListView):
    '''template_name = "news/news.html"
    context_object_name = 'news_list'
    model = News_category1
    queryset =News_category1.objects.all().order_by("-id")[:2]
    '''
    template_name = "news/news.html"
    context_object_name = 'News_middel'
    model = News_middel
    queryset = News_middel.objects.all().order_by("-id")[:5]

    #def get_queryset(self):
     #   return News_category1.objects.all().order_by("-id")[:2]

    def get_context_data(self):
        context = super(News_View, self).get_context_data()
        context['news_list2'] = News_category2.objects.all().order_by("-id")[:2]
        #context['News_middel'] = News_middel.objects.all().order_by("-id")[:5]
        context['News_bottam'] = News_bottam.objects.all().order_by("-id")[:14]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context

def ha_ji_won (request):
    return render(request, 'news/home.html')

"""class IndexView(generic.ListView):
    template_name = "news/home_media.html"

    def get_queryset(self):
        return Side.objects.all()[:5]


class IndexView(generic.ListView):
    template_name = "news/home_media.html"

    def get_queryset(self):
        return Post.objects.all()[:5]
"""

class IndexView(ListView):
    template_name = 'news/home_media.html'
    model = Post
    context_object_name = 'list'
    queryset = Post.objects.all().order_by("-id")[:5]

    def get_context_data(self):
        context = super(IndexView, self).get_context_data()
        context['Side_list'] = Side.objects.all().order_by("-id")[:5]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context


class DetailView(DetailView):
    model = Post
    template_name = 'news/home.html'
    #query_pk_and_slug = True
    #queryset = Post.objects.all().order_by("-id")[:5]

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['Side_list'] = Side.objects.all().order_by("-id")[:5]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context

class SideView(DetailView):
    model = Side
    template_name = 'news/side.html'
    #query_pk_and_slug = True
    #queryset = Post.objects.all().order_by("-id")[:5]

    def get_context_data(self, **kwargs):
        context = super(SideView, self).get_context_data(**kwargs)
        context['Side_list'] = Side.objects.all().order_by("-id")[:5]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context

"""class PostView(ListView):
        #model = Side
        pk_url_kwarg = "post_id"
        template_name = 'news/home.html'
        query_pk_and_slug = True
        #template_name = 'news/home_media.html'
        model = Post
        context_object_name = 'list'
        queryset = Post.objects.all().order_by("-id")[:5]

     def get_context_data(self):
            context = super(PostView, self).get_context_data()
            context['Side_list'] = Side.objects.all().order_by("-id")[:5]
            context['rating'] = Rating.objects.all().order_by("-id")[:10]

            return context
"""

class Game_View(ListView):
    template_name = "news/game.html"
    context_object_name = 'game_up'
    model = Game_up
    queryset =Game_up.objects.all().order_by("-id")[:1]

    #def get_queryset(self):
     #   return News_category1.objects.all().order_by("-id")[:2]

    def get_context_data(self):
        context = super(Game_View, self).get_context_data()
        context['Game_bottam'] = Game_bottam.objects.all().order_by("-id")[:6]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context


class Review_View(ListView):
    template_name = "news/review.html"
    context_object_name = "review"

    def get_queryset(self):
        return Review.objects.all().order_by("-id")[:20]



class News_middel(DetailView):
    model = News_middel
    template_name = 'news/news_middel.html'
    #query_pk_and_slug = True
    #queryset = News_middel.objects.all().order_by("-id")[:5]

    def get_context_data(self, **kwargs):
        context = super(News_middel, self).get_context_data(**kwargs)
        context['Side_list'] = Side.objects.all().order_by("-id")[:5]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context


class News_bottam_view(DetailView):
    model = News_bottam
    template_name = 'news/news_bottam.html'
    #query_pk_and_slug = True
    #queryset = News_middel.objects.all().order_by("-id")[:5]

    def get_context_data(self, **kwargs):
        context = super(News_bottam_view, self).get_context_data(**kwargs)
        context['Side_list'] = Side.objects.all().order_by("-id")[:5]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context

class Game_up_view(DetailView):
    model = Game_up
    template_name = 'news/game_up.html'
    #query_pk_and_slug = True
    #queryset = News_middel.objects.all().order_by("-id")[:5]

    def get_context_data(self, **kwargs):
        context = super(Game_up_view, self).get_context_data(**kwargs)
        context['Side_list'] = Side.objects.all().order_by("-id")[:5]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context

class Game_bottam_view(DetailView):
    model = Game_bottam
    template_name = 'news/game_bottam.html'
    #query_pk_and_slug = True
    #queryset = News_middel.objects.all().order_by("-id")[:5]

    def get_context_data(self, **kwargs):
        context = super(Game_bottam_view, self).get_context_data(**kwargs)
        context['Side_list'] = Side.objects.all().order_by("-id")[:5]
        context['rating'] = Rating.objects.all().order_by("-id")[:10]

        return context
