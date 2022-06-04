# Generated by Django 4.0.5 on 2022-06-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleBaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
    ]