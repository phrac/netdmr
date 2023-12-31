# Generated by Django 4.2.7 on 2023-11-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dmr", "0002_alter_dailyreading_flow"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreading",
            name="flow",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="dailyreading",
            name="gallons",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dailyreading",
            name="hour_avg",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dailyreading",
            name="ph_end",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dailyreading",
            name="ph_mid",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dailyreading",
            name="ph_start",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dailyreading",
            name="units",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
