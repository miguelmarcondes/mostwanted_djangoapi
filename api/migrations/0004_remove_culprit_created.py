# Generated by Django 4.2.1 on 2023-05-22 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_culprit_delete_item_delete_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='culprit',
            name='created',
        ),
    ]
