# Generated by Django 4.1.7 on 2023-03-07 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaz', '0008_alter_newgaz_type_alter_order_date_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]