# Generated by Django 4.1.3 on 2022-12-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_rename_posts_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
