# Generated by Django 4.2.13 on 2024-05-29 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Blog", "0006_alter_author_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="Author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="Author",
        ),
    ]
