# Generated by Django 4.2.5 on 2024-04-21 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_rename_topic_room_topics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='topics',
            new_name='topic',
        ),
    ]
