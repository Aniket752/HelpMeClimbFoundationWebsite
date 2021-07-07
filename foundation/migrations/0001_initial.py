# Generated by Django 3.0.5 on 2020-09-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('T_id', models.IntegerField()),
                ('who', models.CharField(max_length=50)),
                ('massage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
