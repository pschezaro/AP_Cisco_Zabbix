#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Janssen dos Reis Lima

from pyzabbix import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

zapi = ZabbixAPI("http://127.0.0.1/zabbix")
zapi.login(user="user", password="passwd")

arq = csv.reader(open('/tmp/hosts.csv'))

linhas = sum(1 for linha in arq)

f = csv.reader(open('/tmp/hosts.csv'), delimiter=';')
bar = ProgressBar(maxval=linhas,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0

for [hostname,ip] in f:
    hostcriado = zapi.host.create(
        host= hostname,
        status= 0,
        interfaces=[{
            "type": 2,
            "main": "1",
            "useip": 1,
            "ip": ip,
            "dns": "",
            "port": 161,
            "details": {
                    "version": 2,
                    "community": "{$SNMP_COMMUNITY}"
                }
        }],
        groups=[{
            "groupid":133
                    }],
        templates=[{
            "templateid": 10389
        }]
    )


    i += 1
    bar.update(i)

bar.finish
print " "
