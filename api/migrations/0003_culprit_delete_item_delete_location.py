# Generated by Django 4.2.1 on 2023-05-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_item_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Culprit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('race', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('place_of_birth', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
