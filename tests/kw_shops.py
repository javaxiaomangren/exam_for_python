#!/usr/bin/env python
#coding=utf-8
import urllib2
import json

url_template = """http://localhost:8051/hui800-search/hui800/getBenefitSearch.json?cityId=%d&countPerPage=20&group=true&pageNum=1&queryStr=%s&sortType=default"""
city_ids = [110000,120000,130100,140100,210100,210200,220100,230100,310000,320100,320200,320500,330100,330200,330300,340100,350100,350200,360100,370100,370200,410100,420100,430100,440100,440300,440400,440600,441900,500000,510100,530100,610100,620100]
city_ids.sort()
cities = {110000:"北京市", 120000:"天津市", 130100:"石家庄市",140100:"太原市", 210100:"沈阳市", 210200:"大连市", 220100:"长春市", 230100:"哈尔滨市" ,310000:"上海市", 320100:"南京市", 320200:"无锡市", 320500:"苏州市", 330100:"杭州市", 330200:"宁波市", 330300:"温州市", 340100:"合肥市", 350100:"福州市", 350200:"厦门市", 360100:"南昌市", 370100:"济南市", 370200:"青岛市", 410100:"郑州市", 420100:"武汉市", 430100:"长沙市", 440100:"广州市", 440300:"深圳市", 440400:"珠海市", 440600:"佛山市", 441900:"东莞市", 500000:"重庆市", 510100:"成都市", 530100:"昆明市", 610100:"西安市", 620100:"兰州市"}

def get_shops(cityid, keywords):
	result = urllib2.urlopen(url_template % (cityid, keywords)).read()
	shops = json.loads(result).get('groupNum')
	if shops:
		return str(shops)
	return '0'

keywords = open('kw_shops/keywords', 'r').readlines()
res_dic = {}
for kw in keywords:
	kw = kw.rstrip()
	temp = []
	for cid in city_ids:
		shops = get_shops(cid, kw)
		temp.append((cid, shops))
	res_dic[kw] = temp
	print kw

dist_file = open('kw_shops/result.txt', 'w')
dist_file.write('sad\t'+'\t'.join([cities.get(cid) for cid in city_ids])+'\n')
for kw in res_dic:
	res = res_dic[kw]
	res.sort()
	r1 = '\t'.join(map(lambda x:x[1], res))
	dist_file.write(kw + '\t' + r1+'\n')