from django.db import models

# Create your models here.

class Post (models.Model):
    image = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    sort_discription = models.TextField(default='SOME discription')
    discription  = models.TextField()

    def __str__(self):
        return self.title

class Side (models.Model):
    side_image = models.CharField(max_length=250)
    side_title = models.CharField(max_length=250)
    side_discription = models.TextField()

    def __str__(self):
        return self.side_title

class Rating (models.Model):
    game_name = models.CharField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return self.game_name

class News_category1 (models.Model):
    news_image = models.CharField(max_length=250)
    news_title = models.CharField(max_length=205)
    news_discriptions = models.TextField()

    def __str__(self):
        return self.news_title


class News_category2(models.Model):
    news_image = models.CharField(max_length=250)
    news_title = models.CharField(max_length=205)
    news_discriptions = models.TextField()

    def __str__(self):
        return self.news_title


class News_middel(models.Model):
    news_image = models.CharField(max_length=250)
    news_title = models.CharField(max_length=205)
    news_sort_discriptions = models.TextField()
    news_discriptions = models.TextField()

    def __str__(self):
        return self.news_title


class News_bottam(models.Model):
    news_image = models.CharField(max_length=250)
    news_title = models.CharField(max_length=205)
    news_sort_discriptions = models.TextField()
    news_discriptions = models.TextField()

    def __str__(self):
        return self.news_title


class Game_up(models.Model):
    game_image = models.CharField(max_length=250)
    game_title = models.CharField(max_length=205)
    game_discriptions = models.TextField()

    def __str__(self):
        return self.game_title

class Game_bottam(models.Model):
    game_image = models.CharField(max_length=250)
    game_title = models.CharField(max_length=205)
    game_sort_discriptions = models.TextField()
    game_discriptions = models.TextField()

    def __str__(self):
        return self.game_title

class Review(models.Model):
    review_image = models.CharField(max_length=250)
    review_title = models.CharField(max_length=250)
    review_rating = models.FloatField(max_length=10)
    review_review = models.CharField(max_length=250)
    review_sort_discription = models.TextField()
    review_discription = models.TextField()

    def __str__(self):
        return self.review_title