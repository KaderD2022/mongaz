# Generated by Django 4.1.7 on 2023-02-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaz', '0002_gaz_image_alter_gaz_etat'),
    ]

    operations = [
        migrations.AddField(
            model_name='newgaz',
            name='image',
            field=models.CharField(default='', max_length=1000000000),
            preserve_default=False,
        ),
    ]