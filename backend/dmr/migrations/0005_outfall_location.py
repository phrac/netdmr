# Generated by Django 4.2.7 on 2023-11-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dmr", "0004_outfall_dailyreading_outfall"),
    ]

    operations = [
        migrations.AddField(
            model_name="outfall",
            name="location",
            field=models.TextField(null=True),
        ),
    ]
