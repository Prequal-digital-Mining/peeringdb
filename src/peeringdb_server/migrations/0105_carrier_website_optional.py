# Generated by Django 3.2.16 on 2023-01-16 12:41

import django_peeringdb.models.abstract
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0104_mtu_choices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carrier",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, null=True, verbose_name="Website"
            ),
        ),
    ]
