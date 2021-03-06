# Generated by Django 3.1.7 on 2021-04-26 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0005_auto_20210411_1126'),
        ('payment', '0005_auto_20210412_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_info',
            name='Bank_Name',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='Branch_Name',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='admission',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admission_info', to='admission.admission'),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='ch_no',
            field=models.IntegerField(blank=True),
        ),
    ]
