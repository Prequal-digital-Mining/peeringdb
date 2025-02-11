# Generated by Django 4.2.16 on 2024-09-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0132_alter_environmentsetting_setting"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internetexchange",
            name="media",
            field=models.CharField(
                choices=[
                    ("Ethernet", "Ethernet"),
                    ("ATM", "ATM"),
                    ("Multiple", "Multiple"),
                ],
                default="Ethernet",
                max_length=128,
                verbose_name="Media Type",
            ),
        ),
    ]
