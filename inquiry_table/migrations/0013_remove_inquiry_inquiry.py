# Generated by Django 3.2.2 on 2021-05-13 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry_table', '0012_alter_inquiry_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiry',
            name='inquiry',
        ),
    ]