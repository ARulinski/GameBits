# Generated by Django 4.2.13 on 2024-06-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0024_alter_comment_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reply",
            name="date_added",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
