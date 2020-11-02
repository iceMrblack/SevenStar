from django.shortcuts import render
import xlrd
from .models import company_basic_information,company_finance_data
from django.http import HttpResponse
from seven_star import models


# 打开excel，将数据list化
def read_xls(file_name):
	data = xlrd.open_workbook(file_name)
	table = data.sheets()[0]
	rows = table.nrows
	cols=table.ncols
	list_data = []
	
	for v in range(1,rows):
		values = table.row_values(v)
		row_data = []
		for col in range(0,cols):
			row_data.append(str(values[col]))
		list_data.append(row_data)
	return list_data


# 检测数据是否合格
def check_condition(item):
	if(item == "--" or item == '-'):
		return ''
	else:
		return item

# 拼接年报数据
def connect_str(items):
	return_str = ""
	for item in items:
		if(item == "--" or item == '-'):
			return_str = return_str+";"
		else:
			return_str = return_str+item+";"
	return return_str

#公司基本信息
def save_company_data(file_name):
	list_data = read_xls(file_name)
	for items in list_data:
		cbi = company_basic_information()
		cbi.stock_code = check_condition(items[0])
		cbi.stock_name = check_condition(items[1])
		cbi.credit_code = check_condition(items[2])
		cbi.company_name = check_condition(items[3])
		cbi.found_date = check_condition(items[4])
		cbi.business_code = check_condition(items[5])
		cbi.registered_capital = check_condition(items[6])
		cbi.legal_representative = check_condition(items[7])
		cbi.phone = check_condition(items[8]).split(';')[0]
		cbi.registered_address = check_condition(items[9])
		cbi.website = check_condition(items[10]).split(';')[0]
		cbi.profile = check_condition(items[11])
		cbi.stock_type = ''
		cbi.business_scope = check_condition(items[12])
		cbi.listed = 0
		cbi.deteled = 0
		try:
			cbi.save()
		except BaseException as reason:
			print("error"+str(reason))

#年报
def save_finance_data(file_name):
	list_data = read_xls(file_name)
	for items in list_data:
		cfd = company_finance_data()
		cfd.stock_code = items[0]
		cfd.stock_name = items[1]
		cfd.total_share_capital = check_condition(items[2])
		cfd.total_assets_turnover = connect_str(items[3:9])
		cfd.roa = connect_str(items[9:15])
		cfd.total_assets = connect_str(items[15:21])
		cfd.total_liabilities = connect_str(items[21:27])
		cfd.asset_liability_ratio = connect_str(items[27:33])
		cfd.net_profit = connect_str(items[33:39])
		cfd.net_assets = connect_str(items[39:45])
		cfd.roe = connect_str(items[45:51])
		cfd.total_profit = connect_str(items[51:57])
		cfd.current_ratio = connect_str(items[57:63])
		cfd.net_assets_per_share = connect_str(items[63:69])
		cfd.operating_income_per_share = connect_str(items[69:75])
		cfd.enterprise_value = check_condition(items[75])
		cfd.equity_multiplier = connect_str(items[76:82])
		cfd.cash_return = connect_str(items[82:88])
		cfd.quick_ratio = connect_str(items[88:94])
		cfd.sale_net_profit = connect_str(items[94:100])
		cfd.forecast_earnings = check_condition(items[100])
		cfd.forecast_net_profit = check_condition(items[101])
		cfd.forecast_main_business_income = check_condition(items[102])
		cfd.forecast_earnings_before_tax = check_condition(items[103])
		cfd.forecast_cash_flow = check_condition(items[104])
		cfd.forecast_total_profit = check_condition(items[105])
		cfd.forecast_operating_profit = check_condition(items[106])
		try:
			cfd.save()
		except BaseException as reason:
			print("error"+str(reason))

# 初始化stock_code状态
def init_data():
	company_all_data = models.company_basic_information.objects.all()
	for item in company_all_data:
		c = models.company_basic_information.objects.filter(stock_code = item.stock_code)
		c.update(stock_type = '')

# 区分股票板块
def dis_plates(file_name):
	s_list_data = read_xls(file_name)
	company_all_data = models.company_basic_information.objects.all()
	for item in company_all_data:
		judge = 0
		for ld in s_list_data:
			if(item.stock_code == ld[0]):
				judge = 1
		c = models.company_basic_information.objects.filter(stock_code = item.stock_code)
		now = c.first().stock_type
		if judge == 1: 
			c.update(stock_type = now + "1")
		else:
			c.update(stock_type = now + "0")


# 
def fill_stock_type(file_list):
	init_data()
	for url in file_list:
		dis_plates(url)


# 存储静态数据
def save_static_data(request):
	basic_url = "C:/Users/黑子/Desktop/大三/金融信息系统/"
	company_data_url = basic_url+"全部AB股公司基本信息.xls"
	finance_data_url = basic_url+"全部AB股的报表.xls"
	stock_type_list_url = [
	basic_url+"全部A股.xls",
	basic_url+"上证A股.xls",
	basic_url+"深证A股.xls",
	basic_url+"中小企业板.xls",
	basic_url+"创业板.xls",
	basic_url+"科创板.xls",
	basic_url+"深证主板A股.xls",
	basic_url+"全部B股.xls",
	basic_url+"上证B股.xls",
	basic_url+"深证B股.xls",
	basic_url+"全部AB股.xls",
	basic_url+"上证AB股.xls",
	basic_url+"深证AB股.xls",
	]
	# 存公司基本信息
	save_company_data(company_data_url)
	# 存年报
	save_finance_data(finance_data_url)
	# 存类型
	fill_stock_type(stock_type_list_url)
	
	return HttpResponse("success!!!")