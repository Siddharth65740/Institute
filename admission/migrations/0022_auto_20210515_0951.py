# Generated by Django 3.2.2 on 2021-05-15 04:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0021_alter_admission_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='Fees',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Fees should not be negative')]),
        ),
        migrations.AlterField(
            model_name='admission',
            name='No_of_Days',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'no of days should not be nagetive'), django.core.validators.MaxValueValidator(7, 'no  of days should be maximum 7')]),
        ),
    ]
