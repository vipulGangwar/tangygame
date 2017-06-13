from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from news.models import Post
from news.models import Side
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
      #url(r'^$', views.index, name='index' ),
      #url(r'^home/', ListView.as_view(queryset=Post.objects.all()[:5], template_name="news/home_media.html")),
      #url(r'^$', ListView.as_view(queryset=Post.objects.all()[:5], template_name="news/home_media.html")),
      url(r'^home/', views.IndexView.as_view(), name='list'),
      url(r'^$', views.IndexView.as_view(), name='list'),
      url(r'^(?P<pk>\d+)$', views.DetailView.as_view(), name='detail'),
      url(r'^side/(?P<pk>\d+)/$', views.SideView.as_view(), name='side_detail'),
      url(r'^news/news_middel/(?P<pk>\d+)/$', views.News_middel.as_view(), name='News_middel'),
      url(r'^news/news_bottam/(?P<pk>\d+)/$', views.News_bottam_view.as_view(), name='News_bottam'),
      url(r'^game/game_up/(?P<pk>\d+)/$', views.Game_up_view.as_view(), name='News_bottam'),
      url(r'^game/game_bottam/(?P<pk>\d+)/$', views.Game_bottam_view.as_view(), name='News_bottam'),
      #url(r'^side/(?P<pk>\d+)/$', views.SideView.as_view(), name='side_detail'),
      url(r'^news/$', views.News_View.as_view(), name='news_view'),
      url(r'^game/$', views.Game_View.as_view(), name='game_view'),
      url(r'^review/', views.Review_View.as_view(), name='review_view'),
      url(r'^news_category1/(?P<pk>\d+)/$', views.SideView.as_view(), name='side_detail'),
]

if settings.DEBUG:
      urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
