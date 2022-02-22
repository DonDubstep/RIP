# Generated by Django 4.0 on 2021-12-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=200)),
            ],
        ),
    ]