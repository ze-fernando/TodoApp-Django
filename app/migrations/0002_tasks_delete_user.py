# Generated by Django 4.2.2 on 2023-07-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300)),
                ('_id', models.IntegerField()),
                ('is_done', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
