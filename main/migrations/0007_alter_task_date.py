# Generated by Django 4.1.4 on 2022-12-20 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 7, 33, 32, 942037, tzinfo=datetime.timezone.utc)),
        ),
    ]
