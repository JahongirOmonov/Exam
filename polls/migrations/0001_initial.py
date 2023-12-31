# Generated by Django 4.2.5 on 2023-09-12 09:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('surname', models.CharField(default='', max_length=100)),
                ('date_of_birth', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='bookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('page', models.PositiveIntegerField(default=3)),
                ('year_of_invented', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.authormodel')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
