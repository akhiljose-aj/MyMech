# Generated by Django 4.1.6 on 2023-05-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_admin_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='status',
            field=models.CharField(choices=[('approve', 'approve'), ('reject', 'reject')], default='approve', max_length=10),
        ),
    ]
