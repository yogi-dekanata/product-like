# Generated by Django 4.2.5 on 2023-09-15 05:23

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
                ("shop_id", models.BigIntegerField(null=True)),
                ("name", models.CharField(max_length=255, null=True)),
                ("description", models.TextField(null=True)),
                ("thumbnail_url", models.TextField()),
                ("origin_price", models.BigIntegerField()),
                ("discounted_price", models.BigIntegerField()),
                ("discounted_rate", models.FloatField(null=True)),
                ("status", models.CharField(max_length=191)),
                ("in_stock", models.BooleanField(default=False)),
                ("is_preorder", models.BooleanField(default=False)),
                ("is_purchasable", models.BooleanField(default=False)),
                ("delivery_condition", models.CharField(max_length=255)),
                ("delivery_display", models.TextField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "products",
            },
        ),
    ]
