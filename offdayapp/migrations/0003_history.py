# Generated by Django 4.2 on 2024-09-26 04:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("offdayapp", "0002_offday_date_added_alter_offday_day"),
    ]

    operations = [
        migrations.CreateModel(
            name="History",
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
                ("action", models.CharField(max_length=255)),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "team_member",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="offdayapp.teammember",
                    ),
                ),
            ],
        ),
    ]
