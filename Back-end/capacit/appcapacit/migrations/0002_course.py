# Generated by Django 4.2.1 on 2023-06-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appcapacit", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("language", models.CharField(max_length=255)),
                ("technology", models.CharField(max_length=255)),
                ("level", models.CharField(max_length=255)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=10, max_length=10),
                ),
                ("link", models.CharField(max_length=255)),
                ("teacher_name", models.CharField(max_length=255)),
            ],
        ),
    ]
