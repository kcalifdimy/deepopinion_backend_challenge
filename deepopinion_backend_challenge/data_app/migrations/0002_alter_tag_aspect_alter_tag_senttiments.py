# Generated by Django 4.1.9 on 2023-05-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="aspect",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="senttiments",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]