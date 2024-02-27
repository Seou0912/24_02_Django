# Generated by Django 5.0.2 on 2024-02-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("likes", models.PositiveBigIntegerField(default=0)),
                ("reviews", models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]
