# Generated by Django 4.1.7 on 2023-06-06 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_book_service_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_service',
            name='status',
            field=models.CharField(choices=[('accept', 'accept'), ('reject', 'reject'), ('complete', 'complete')], max_length=10),
        ),
    ]
