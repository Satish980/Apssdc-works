# Generated by Django 3.0.8 on 2020-07-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Action', '0002_auto_20200721_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=50)),
                ('a_age', models.IntegerField()),
                ('a_no_movies', models.IntegerField()),
            ],
        ),
    ]
