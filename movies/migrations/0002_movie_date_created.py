# Generated by Django 4.1.7 on 2023-03-14 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 14, 14, 25, 12, 532668, tzinfo=datetime.timezone.utc)),
        ),
    ]
