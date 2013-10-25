#!/usr/bin/env python
#coding utf8
import MySQLdb
import sys
import urllib2
import json


# def pois(_id):
# 	sql = "SELECT id, name, lat, lng FROM pois where id> %s limit 100000" % _id
# 	db = MySQLdb.connect(host='116.255.244.36', port=3336, user='hadoop', passwd='tgxstbbA1005', db='navtech')
# 	cursor = db.cursor(MySQLdb.cursors.DictCursor)
# 	cursor.execute(sql)
# 	rows = cursor.fetchall()
# 	return rows

def _cursor():
    db = MySQLdb.connect(host='116.255.244.36', port=3336, user='hadoop', passwd='tgxstbbA1005', db='navtech')
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SET NAMES utf8")
    return cursor

def get_by_name(name, cur):
	sql = "SELECT name, lat, lng FROM pois where kind='A700' AND name LIKE '%%%s%%' " % name
	cur.execute(sql)
	rows = cur.fetchall()
	return rows

arg = sys.argv[1]
result = open('files/%s_rs' % arg, 'w')
def get_brand(url, line):
	rs = urllib2.urlopen(url).read()
	js_rs = json.loads(rs).get('tuan800')
	bizone = js_rs.get('bizone')
	if bizone:
		bname = js_rs.get('bizone_name')
		result.write(line+'\t' + str(bizone)+'\t'+ bname.encode('utf-8')+'\n')
	else:
		result.write(line+'\n')

cur = _cursor()
for name in open(arg, 'r').readlines():
	name = name[:-1]
	name_rows = get_by_name(name, cur)
	if name_rows:
		for row in name_rows:
			# lat, lng, _name = row.get('lat'), row.get('lng'),row.get('name')
			url = "http://192.168.10.12:9100/bizone/fromLatLng.json?lat=%(lat)s&lng=%(lng)s" % row
			line = "%s\t%s" % (name, ("%(name)s\t%(lat)s\t%(lng)s" % row))
			get_brand(url, line)
	else:
		result.write(name+'\n')

