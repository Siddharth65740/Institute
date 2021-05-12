# Generated by Django 3.1.7 on 2021-05-03 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry_table', '0011_auto_20210502_1918'),
        ('admission', '0019_auto_20210502_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='inquiry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admission', to='inquiry_table.inquiry'),
        ),
    ]