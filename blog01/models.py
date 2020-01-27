from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    title = models.CharField('TITLE', max_length=80)
    content = models.TextField('CONTENT', max_length=1000)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    image = models.ImageField(upload_to='photo/%Y/%m', null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog01:post_detail', args=(self.id,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()