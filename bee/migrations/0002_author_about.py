# Generated by Django 4.2.3 on 2023-07-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bee", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="about",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]