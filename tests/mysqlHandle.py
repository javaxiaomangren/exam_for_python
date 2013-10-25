# -*- coding: utf-8 -*-
"""
Created on 2012-3-26

@author: madf
"""
import os
import MySQLdb
import ConfigParser
from _mysql_exceptions import MySQLError
from DBUtils.PooledDB import PooledDB
from CONFIG import JDBC_CONFIG



config = ConfigParser.ConfigParser()
jdbcFile = "%s/%s" % (os.path.dirname(os.path.realpath(__file__)), JDBC_CONFIG)
config.read(jdbcFile)

class MysqlHandle(object):

    def __init__(self, section):
        try:
            self._host    = config.get(section, "host")
            self._port    = config.getint(section, "port")
            self._user    = config.get(section, "user")
            self._passwd  = config.get(section, "password")
            self._db      = config.get(section, "database")
            self.__dbpool = None
            self.__createPool()

        except Exception, e:
            raise MySQLError(e)

    def __createPool(self):
        if self.__dbpool is None:
            self.__dbpool = PooledDB(creator=MySQLdb, mincached=5, maxcached=50,
            host = self._host, port=self._port, user=self._user, passwd=self._passwd,
            db = self._db, charset="utf8")

    def getConn(self):
        return self.__dbpool.connection()

    def createConn(self):
        return self.__dbpool.connection(shareable=False)

    def getDatabaseName(self):
        return self._db

    def getHost(self):
        return self._host