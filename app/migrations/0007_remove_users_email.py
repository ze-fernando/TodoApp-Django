# Generated by Django 4.2.2 on 2023-07-04 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_users_delete_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
    ]
