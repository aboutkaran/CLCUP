# Generated by Django 4.1.7 on 2023-05-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_attendancepdfform_paid_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancepdfform',
            name='remark',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
