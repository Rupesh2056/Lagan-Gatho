# Generated by Django 4.0.1 on 2022-02-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerpreference', '0003_alter_preference_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='marital_status',
            field=models.CharField(max_length=100),
        ),
    ]