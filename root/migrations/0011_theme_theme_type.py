# Generated by Django 5.2.1 on 2025-05-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("root", "0010_theme_show_transition"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="theme_type",
            field=models.CharField(
                choices=[("light", "Light"), ("dark", "Dark")],
                default="light",
                max_length=10,
            ),
        ),
    ]
