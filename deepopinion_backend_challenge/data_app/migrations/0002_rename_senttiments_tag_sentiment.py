# Generated by Django 4.1.9 on 2023-05-29 14:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("data_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tag",
            old_name="senttiments",
            new_name="sentiment",
        ),
    ]