#!/usr/bin/python2.6

import sys
f = open('/proc/interrupts','r')
fline = f.readlines()
f.close()
print "CPU Cores :"+str(len(fline[0].split()))
if len(sys.argv)-1 != 1:
    print "Please input the name of the interface."
    print "Example 'python interfaceQueueCounts.py eth0'"
else:
    num=0
    for line in fline:
        temp1=line.strip('\n')
        temp2=temp1.split()
        lenght=len(temp2)-1
        if sys.argv[1]+"-" in temp2[lenght]:
            num=num+1
            print temp2[0]+temp2[lenght]
        else:
            continue

    print sys.argv[1].capitalize()+" -- total number of message queue: "+str(num)

#for i in range (1,len(sys.argv)):
#    print "mmm",i,sys.argv[i]

