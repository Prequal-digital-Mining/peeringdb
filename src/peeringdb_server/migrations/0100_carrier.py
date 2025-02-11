# Generated by Django 3.2.16 on 2022-11-22 11:15

import django.db.models.deletion
import django.db.models.manager
import django_handleref.models
import django_peeringdb.models.abstract
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0099_auto_20221027_2023"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrier",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(blank=True, max_length=255, verbose_name="Status"),
                ),
                (
                    "created",
                    django_handleref.models.CreatedDateTimeField(
                        auto_now_add=True, verbose_name="Created"
                    ),
                ),
                (
                    "updated",
                    django_handleref.models.UpdatedDateTimeField(
                        auto_now=True, verbose_name="Updated"
                    ),
                ),
                ("version", models.IntegerField(default=0)),
                (
                    "name",
                    models.CharField(max_length=255, unique=True, verbose_name="Name"),
                ),
                (
                    "aka",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Also Known As"
                    ),
                ),
                (
                    "name_long",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Long Name"
                    ),
                ),
                (
                    "website",
                    django_peeringdb.models.abstract.URLField(
                        max_length=255, verbose_name="Website"
                    ),
                ),
                ("notes", models.TextField(blank=True, verbose_name="Notes")),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carrier_set",
                        to="peeringdb_server.organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Carrier",
                "verbose_name_plural": "Carriers",
                "db_table": "peeringdb_carrier",
                "abstract": False,
            },
            managers=[
                ("handleref", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="CarrierFacility",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(blank=True, max_length=255, verbose_name="Status"),
                ),
                (
                    "created",
                    django_handleref.models.CreatedDateTimeField(
                        auto_now_add=True, verbose_name="Created"
                    ),
                ),
                (
                    "updated",
                    django_handleref.models.UpdatedDateTimeField(
                        auto_now=True, verbose_name="Updated"
                    ),
                ),
                ("version", models.IntegerField(default=0)),
                (
                    "carrier",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carrierfac_set",
                        to="peeringdb_server.carrier",
                    ),
                ),
                (
                    "facility",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carrierfac_set",
                        to="peeringdb_server.facility",
                    ),
                ),
            ],
            options={
                "verbose_name": "Carrier presence at facility",
                "verbose_name_plural": "Carrier presences at facility",
                "db_table": "peeringdb_carrier_facility",
                "abstract": False,
                "unique_together": {("carrier", "facility")},
            },
            managers=[
                ("handleref", django.db.models.manager.Manager()),
            ],
        ),
    ]
