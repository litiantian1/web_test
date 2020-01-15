# -*-coding:utf-8 -*-
# !user/bin/python
import os
import subprocess
import time


class Appium(object):
    def start_Appium(self, host, port, devices_uid):
        # device_uid,
        # appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600
        errormsg = ""
        appium_server_url = ""
        try:
            if self.port_is_free(host, port):
                cmd = 'start/b appium -a ' + host + ' -p ' + port + ' -U' + devices_uid
                print cmd
                # p= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=PIPE, stderr=PIPE)
                p = subprocess.Popen(cmd, shell=True, stdout=open('E:/logs.log', 'w'), stderr=subprocess.STDOUT)
                print p
                appium_server_url = 'http://' + host + ':' + str(port) + '/wd/hub'
                print appium_server_url
            else:
                print "port:%d is used!" % port
        except Exception, msg:
            errormsg = str(msg)
        return appium_server_url, errormsg

    def port_is_free(self, host, port):
        if host is not None and port is not None:
            return host, port
        else:
            return 'please enter right parameter'

    def stop_Appium(self, get_port):
        cmd = 'stopAppiumServer.BAT %s' % get_port
        # print cmd
        p = os.popen(cmd)
        print p.read()

    def ABD(self, X, Y):
            cmd = 'start/b adb shell input tap ' + str(X) + " " + str(Y)
            p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
            print cmd
    def ABD_Move(self, X, Y, Z, G, S):
            cmd = "start/b adb shell input swipe {0} {1} {2} {3} {4}".format(str(X), str(Y), str(Z), str(G), str(S))
            p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
            print cmd
    def ABDKey(self, X):
            cmd = 'start/b adb shell input keyevent ' + str(X)
            p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
            print cmd

'''if __name__=='__main__':
   appium1=Appium()
   #appium1.ABD(209.8, 1489.1)
  # time.sleep(1)
  # appium1.ABD(334.7, 1483.1)
   #appium1.ABD_Move(312.7, 1830.0, 730.2, 1824.0, 5000)  # 添加录音
   appium1.start_Appium('127.0.0.1','4723','5LMBGM6SBYIRINRS')
   time.sleep(8)
   os.system('start/b stopAppiumServer.BAT')'''
