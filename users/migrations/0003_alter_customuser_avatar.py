# Generated by Django 4.2.13 on 2024-06-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_customuser_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(
                default="avatars/default_avatar.png", upload_to="avatars/"
            ),
        ),
    ]
