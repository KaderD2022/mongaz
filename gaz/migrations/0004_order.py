# Generated by Django 4.1.7 on 2023-02-20 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('gaz', '0003_newgaz_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_command', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateTimeField(auto_now=True)),
                ('gaz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaz.gaz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofil')),
            ],
        ),
    ]