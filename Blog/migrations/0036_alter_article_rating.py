# Generated by Django 4.2.13 on 2024-06-22 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0035_article_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="rating",
            field=models.IntegerField(
                blank=True,
                default=None,
                help_text="Enter rating from 1 to 5",
                null=True,
            ),
        ),
    ]
