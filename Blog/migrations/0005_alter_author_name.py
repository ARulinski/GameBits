# Generated by Django 4.2.13 on 2024-05-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0004_alter_author_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
