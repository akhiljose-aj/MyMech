# Generated by Django 4.1.6 on 2023-05-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_mechanic_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='status',
            field=models.CharField(choices=[('approve', 'approve'), ('reject', 'reject')], default='pending', max_length=10),
        ),
    ]
