# Generated by Django 4.1.3 on 2022-12-09 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_alter_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categorys',
        ),
    ]