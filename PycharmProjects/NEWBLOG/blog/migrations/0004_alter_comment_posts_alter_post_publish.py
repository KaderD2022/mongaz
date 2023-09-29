# Generated by Django 4.1.3 on 2022-12-11 00:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_publish_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 11, 0, 11, 0, 834080, tzinfo=datetime.timezone.utc)),
        ),
    ]
