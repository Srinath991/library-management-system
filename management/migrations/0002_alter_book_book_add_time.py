# Generated by Django 4.2.3 on 2024-02-25 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_add_time',
            field=models.TimeField(default=datetime.datetime(2024, 2, 25, 7, 38, 0, 757428, tzinfo=datetime.timezone.utc)),
        ),
    ]
