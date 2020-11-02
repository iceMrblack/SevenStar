# Generated by Django 3.1.1 on 2020-10-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company_basic_information',
            fields=[
                ('stock_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('credit_name', models.CharField(max_length=20)),
                ('credit_code', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=100)),
                ('found_date', models.CharField(max_length=20)),
                ('business_code', models.CharField(max_length=20)),
                ('registered_capital', models.CharField(max_length=20)),
                ('legal_representative', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('registered_address', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=100)),
                ('profile', models.TextField()),
                ('stock_type', models.CharField(max_length=20)),
                ('business_scope', models.TextField()),
                ('listed', models.IntegerField(default=0)),
                ('deteled', models.IntegerField(default=0)),
            ],
        ),
    ]