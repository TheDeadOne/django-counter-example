# Generated by Django 2.2.3 on 2019-07-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'публикации',
                'ordering': ('-published',),
            },
        ),
    ]
