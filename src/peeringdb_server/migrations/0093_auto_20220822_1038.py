# Generated by Django 3.2.14 on 2022-08-22 10:38

from django.db import migrations, models

import peeringdb_server.validators


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0092_create_missing_email_objects"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="email_domains",
            field=models.TextField(
                blank=True,
                help_text="If user email restriction is enabled: only allow users with emails in these domains. One domain per line, in the format of '@xyz.com'",
                null=True,
                validators=[peeringdb_server.validators.validate_email_domains],
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="restrict_user_emails",
            field=models.BooleanField(
                default=False,
                help_text="Require users in your organization to have email addresses within your specified domains.",
            ),
        ),
    ]
