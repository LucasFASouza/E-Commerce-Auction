# Generated by Django 4.1.5 on 2023-02-07 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_rename_text_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
    ]
