# Generated by Django 4.1.7 on 2023-04-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]