#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 11:29
# @Author  : qingping.niu
# @File    : run_monkey.py
# @desc    :

import subprocess
import argparse
import unittest
import os
import glob

import uiautomator2 as u2
from monkey.Drivers_monkey import DriversMonkey
from case.case import myCase
from Utils.Drivers import Drivers
from Utils.ftpUtils import ftp_downloadFile,http_downloadFile
from Utils.commonUtils import get_apk_info
from case.ParametrizedTestCase import ParametrizedTestCase
from Utils.Log import Log

if __name__ == '__main__':
    logger = Log()
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-d", "--devices", required=False, help="devices")
    # ap.add_argument("-c","--command",required=False, help="command")
    # ap.add_argument("-f","--ftp",required=True, help="ftp")
    # args = vars(ap.parse_args())
    # tempDevices = args['devices']
    # command = args['command']
    # ftpPath = args['ftp']

    # ftpPath = '//AGL Video/'

    devices = []
    ftpPath = os.environ["ftp_path"]
    command = os.environ["command"]
    requestType = os.environ["requesttype"]

    print("*******ftpPath %s :" % ftpPath)
    print("****** command %s : " % command)
    print('******requestType %s : '%requestType)

    try:
        tempDevices = os.environ["devices"]
        print("******tempDevices %s :" % tempDevices)
        if tempDevices:
            devices = tempDevices.split(',')

    except Exception as e:
        pass

    print('*****devices %s: '%devices)
    localPath = 'F:\\mibctestFTP\\download'
    apkPath=''
    if requestType == 'FTP':
        apkPath = ftp_downloadFile(localPath,ftpPath)
    elif requestType == 'HTTP':
        apkPath = http_downloadFile(localPath,ftpPath)

    apkinfo = get_apk_info(apkPath)
    #
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(myCase,apkPath))
    #
    # command="adb -s %s shell monkey -p com.tcl.demo.lsstestdemo --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v 10000"
    #
    Drivers().run_maxim(cases=suite,devices_input=devices,apkinfo=apkinfo,command=command)
    # DriversMonkey().run(method=method,ip=ips,command=command)








