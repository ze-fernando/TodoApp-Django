# Generated by Django 4.2.2 on 2023-07-02 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tasks_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='_id',
        ),
    ]
