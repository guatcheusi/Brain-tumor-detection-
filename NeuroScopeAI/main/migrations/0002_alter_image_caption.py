# Generated by Django 5.0.6 on 2024-05-27 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(max_length=100, null=True),
        ),
    ]