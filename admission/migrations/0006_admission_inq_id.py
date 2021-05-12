# Generated by Django 3.1.7 on 2021-05-01 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry_table', '0001_initial'),
        ('admission', '0005_auto_20210411_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='inq_id',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='admission', to='inquiry_table.inquiry'),
        ),
    ]
