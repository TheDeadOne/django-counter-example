from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    published = models.DateTimeField('Опубликован', auto_now_add=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})