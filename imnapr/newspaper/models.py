from django.db import models

# Create your models here.


class News(models.Model):
    new_title = models.TextField()
    new_text = models.TextField()
    new_media_url = models.TextField()
    new_publish_date = models.DateField(auto_now=True)
    new_tag = models.TextField()
    news_summery = models.TextField(default='')


class Comments(models.Model):
    user_name = models.CharField()
    user_email = models.EmailField()
    comment_text = models.TextField()
    new = models.ForeignKey(News, on_delete=models.CASCADE)
