# Generated by Django 4.2.3 on 2023-08-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('productTitle', models.CharField(max_length=100)),
                ('productContent', models.TextField()),
                ('productImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('productOption', models.TextField()),
            ],
        ),
    ]
