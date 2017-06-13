from django.contrib import admin

# Register your models here.

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

admin.site.register(Post)

admin.site.register(Side)

admin.site.register(Rating)

admin.site.register(News_category1)

admin.site.register(News_category2)

admin.site.register(News_middel)

admin.site.register(News_bottam)

admin.site.register(Game_up)

admin.site.register(Game_bottam)

admin.site.register(Review)