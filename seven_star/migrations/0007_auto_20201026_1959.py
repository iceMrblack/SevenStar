# Generated by Django 3.1.1 on 2020-10-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seven_star', '0006_auto_20201026_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_finance_data',
            old_name='rota',
            new_name='roa',
        ),
        migrations.AddField(
            model_name='company_finance_data',
            name='stock_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
