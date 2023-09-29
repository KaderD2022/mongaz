# Generated by Django 4.1.7 on 2023-02-23 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaz', '0007_alter_order_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newgaz',
            name='type',
            field=models.CharField(choices=[('b6', 'B6'), ('b12', 'B12')], max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 13, 42, 39, 307575, tzinfo=datetime.timezone.utc)),
        ),
    ]