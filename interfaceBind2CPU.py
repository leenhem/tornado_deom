#!/usr/bin/python2.6

import os,sys
import subprocess
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def bin2dec(string_num):
    return str(int(string_num, 2))
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])
        
    return ''.join([str(x) for x in mid[::-1]])
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))
#p = subprocess.Popen(['service irqbalance', 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#p.communicate()
#if p.returncode == 0:
#    p = subprocess.Popen(['service irqbalance', 'stop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    p.wait()

if len(sys.argv)-1 != 3:
    print "Please input the name of the interface <interface> <start cpuid > <end cpuid>"
    print "Example 'python interfaceBind2CPU.py eth0 0 3'"
else:
	f = open('/proc/interrupts','r')
	fline = f.readlines()
	f.close()
	cpumasklist=[]
	for corenum in range (0,len(fline[0].split())):
		binmask='1'
		for i in range(0,corenum):
			binmask=binmask+'0'
		cpumasklist.append(bin2hex(binmask))
	corelist=[]
	if corelist == []:
		for core in range (int(sys.argv[2]),int(sys.argv[3])+1):
			corelist.append(core)


	for line in fline:
		temp1=line.strip('\n')
		temp2=temp1.split()
		lenght=len(temp2)-1
		if sys.argv[1]+"-" in temp2[lenght]:
			path=temp2[0].strip(':')
			irqpath = os.path.join("/proc/irq", path, "smp_affinity")
			firq=open(irqpath, "w")
			firq.write(cpumasklist[corelist[0]])
			firq=open(irqpath, "r")
			print irqpath+"----CPU"+str(corelist[0])+" : "+firq.read()
			del corelist[0]
		else:
			continue
	for line in fline:
		temp1=line.strip('\n')
		temp2=temp1.split()
		lenght=len(temp2)-1
		if sys.argv[1] in temp2[lenght]:
			print temp2[0]+temp2[lenght]

#
#    print sys.argv[1].capitalize()+"  The number of total in the message queue: "+str(num)
#
#for i in range (1,len(sys.argv)):
#    print "mmm",i,sys.argv[i]

