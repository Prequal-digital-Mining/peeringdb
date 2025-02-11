# Generated by Django 3.2.14 on 2022-08-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0096_auto_20220829_1419"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="never_flag_for_deletion",
            field=models.BooleanField(
                default=False,
                help_text="This user will never be flagged for deletion through the orphaned user cleanup process.",
            ),
        ),
    ]
