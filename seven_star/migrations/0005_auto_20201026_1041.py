# Generated by Django 3.1.1 on 2020-10-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seven_star', '0004_company_finance_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_finance_data',
            name='asset_liability_ratio',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='cash_return',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='current_ratio',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='enterprise_value',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='equity_multiplier',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='finance_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='forecast_cash_flow',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='forecast_earnings',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='forecast_earnings_before_tax',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='forecast_main_business_income',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='forecast_net_profit',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='forecast_operating_profit',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='forecast_total_profit',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='net_assets',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='net_assets_per_share',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='net_profit',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='operating_income_per_share',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='quick_ratio',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='roe',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='rota',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='sale_net_profit',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='total_assets',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='total_assets_turnover',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='total_liabilities',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_finance_data',
            name='total_profit',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
