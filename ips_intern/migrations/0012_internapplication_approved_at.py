# Generated by Django 5.2.3 on 2025-06-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ips_intern', '0011_remove_internapplication_certificate_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='internapplication',
            name='approved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
