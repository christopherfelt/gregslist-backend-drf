# Generated by Django 3.0.3 on 2020-05-28 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('description', models.TextField()),
                ('imgUrl', models.TextField()),
                ('price', models.IntegerField()),
                ('levels', models.IntegerField()),
            ],
        ),
    ]
