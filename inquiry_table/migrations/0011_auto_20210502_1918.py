# Generated by Django 3.1.7 on 2021-05-02 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_master_fees'),
        ('inquiry_table', '0010_inquiry_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='course',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inquiry', to='course.course_master'),
        ),
    ]