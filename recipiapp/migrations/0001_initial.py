# Generated by Django 5.0.2 on 2024-02-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipi_name', models.CharField(max_length=100)),
                ('recipi_description', models.TextField()),
                ('recipi_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
