from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Автор')
    title = models.CharField(max_length=250, verbose_name='Название')
    snippet = RichTextUploadingField(max_length=250, verbose_name='Отрывок')
    content = RichTextUploadingField(verbose_name='Содержание')
    image = models.ImageField(null=True, blank=True, upload_to='static/', verbose_name='Изображение')
    published = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-published',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_name', verbose_name='Имя пользователя')
    text = models.TextField()
    published = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

    class Meta:
        ordering = ('-published',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text