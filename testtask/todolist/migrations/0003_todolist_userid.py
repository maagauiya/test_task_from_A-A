# Generated by Django 3.2.9 on 2022-01-18 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todolist_task_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='userid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
