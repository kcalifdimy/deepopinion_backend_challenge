# Generated by Django 4.1.9 on 2023-05-29 14:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("data_app", "0002_rename_senttiments_tag_sentiment"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Data",
            new_name="Text",
        ),
    ]