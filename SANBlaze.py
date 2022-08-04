## SANBlaze Testing - SAS QA ##
## M.Razif 2020 ##

import urllib.request
import time
from time import strftime
import os

ip = 'http://192.168.50.11/goform/XmlApi?op='

def vlunSystemInfo():
    sanblaze = ip + 'vlunSystemInfo'
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunPortList():
    sanblaze = ip + 'vlunPortList'
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunPortStatus(port):
    sanblaze = ip + 'vlunPortStatus' + '&port=' + str(port)
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunTargetList(port):
    sanblaze = ip + 'vlunTargetList' + '&port=' + str(port)
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunTargetStatus(port,target):
    sanblaze = ip + 'vlunTargetStatus' + '&port=' + str(port) +'&target=' + str(target)
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunLunStatus(port,target,lun):
    sanblaze = ip + 'vlunTargetStatus' + '&port=' + str(port) +'&target=' + str(target) + '&lun' + str(lun)
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunTestList(port):
    sanblaze = ip + 'vlunTestList' + '&port=' + str(port)
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunTestStatus(port,test_id): #test_id must include ''
    sanblaze = ip + 'vlunTestStatus' + '&port=' + str(port) + '&test_id=' + str(test_id)
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunTargetGetInjectedErrorStatus(port, target, lun): # Target only
    sanblaze = ip + 'vlunTargetGetInjectedErrorStatus' + '&port=' + str(port) + '&target=' + str(
        target) + '&lun=' + str(lun)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunTargetGetLogOnErr(port, target, lun, count):
    sanblaze = ip + 'vlunTargetGetInjectedErrorStatus' + '&port=' + str(port) + '&target=' + str(
        target) + '&lun=' + str(lun) + '&count=' + str(count)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))


def vlunTargetGetLUNConfig(port, target, lun):
    sanblaze = ip + 'vlunTargetGetLUNConfig' + '&port=' + str(port) + '&target=' + str(
        target) + '&lun=' + str(lun)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))


def vlunLunSearch(serial_number):  # need serial number, case sensitive
    sanblaze = ip + 'vlunLunSearch' + '&serial_number=' + str(serial_number)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunStartTest(port, test_type, threads, blocks, ios):
    # port = [8, 9] for SAS
    # test_type = [Read, Write, Compare, Verify, Rewrite, R10W90, R25W75, R50W50,R75W25, R90W10]
    # threads = [0-32]
    # opcode = [0, 6, 10, 12,16] #0 random
    # blocks = [1,2,3,4] # Transfer Length 1 = 512bytes
    # ios = [1,2,3,4] - Loop to send command # 0 unlimited
    sanblaze = ip + 'vlunStartTest' + '&port=' + str(port) + '&test_type=' + str(
        test_type) + '&threads=' + str(threads) + '&blocks=' + str(blocks) + '&ios=' + str(ios)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunStartTestAdvanced(port, test_type, seek_type, opcode, pattern, threads, blocks, ios ):
    # test_type = [Read, Write, Compare, Verify, Rewrite, R10W90, R25W75, R50W50,R75W25, R90W10]
    # seek_type = [0, 1, 2, 3] # Sequential, Random, Min/Max, Butterfly
    # opcode = [0, 6, 10, 12,16] #0 random
    # pattern = [xrange(0,13,1), -1, -2)
    # 0:8 random, 0x00ff00ff, 0x55aa55aa, 8-bit incr, 8-bit walking 1_0, 0x0000ffff, 0x5555aaaa, 16-bit incr, 16-bit walking 1_0
    # 9:13,-1,-2 32-bit incr, Low Frequency 8B/10B, Med Frequency 8B/10B, High Frequency 8B/10B, Jitter (CJPAT), custom, Existing data
    # threads = [0, 1, 128, 512}
    # blocks = [512, 1024, 4096]
    # ios = [0] number of IOs to do, 0 = unlimited
    sanblaze = ip + 'vlunStartTest' + '&port=' + str(port) + '&test_type=' + str(
        test_type) + '&seek_type=' + str(seek_type) + '&opcode=' + str(opcode) + '&pattern=' + str(
        pattern) + '&threads=' + str(threads) + '&blocks=' + str(blocks) + '&ios=' + str(ios)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunStopTest(port):
    sanblaze = ip + 'vlunStopTest' + '&port=' + str(port)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunChangeTestState(port,state ): #state= pause, unpause, start got problem need to specific test ID
    sanblaze = ip + 'vlunChangeTestState' + '&port=' + str(port) + '&state=' + str(state)
    print(sanblaze)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunLinkReset(port): # Port 8 and 9 only for SAS
    sanblaze = ip + 'vlunLinkReset' + '&port=' + str(port)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunPortReset(port): # Port 8 and 9 only for SAS
    sanblaze = ip + 'vlunPortReset' + '&port=' + str(port)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

def vlunTaskManagement(command): # Port 8 and 9
    # command = [BusReset , TargetReset, LogicalUnitReset, ClearTaskSet, AbortTaskSet, AbortTask, ControllerReset]
    sanblaze = ip + 'vlunTaskManagement' + '&port=8' + '&command=' + str(command)
    req = urllib.request.urlopen(sanblaze)
    print(req.read().decode())
    print(strftime("%Y-%m-%d %H:%M:%S"))

#Start = vlunStartTest(8,'Write', 1, 4, 0)
#Stop = vlunStopTest(8)
Start = vlunTaskManagement('BusReset')




