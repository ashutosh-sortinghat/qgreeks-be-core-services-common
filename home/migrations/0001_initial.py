# Generated by Django 5.0.2 on 2024-02-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                ("price", models.CharField(blank=True, max_length=40, null=True)),
                ("quantity", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
