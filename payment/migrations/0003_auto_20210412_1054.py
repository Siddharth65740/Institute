# Generated by Django 3.1.7 on 2021-04-12 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0005_auto_20210411_1126'),
        ('payment', '0002_payment_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='admission',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='admission', to='admission.admission'),
        ),
    ]
