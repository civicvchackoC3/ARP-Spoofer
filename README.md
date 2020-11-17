# ARP-Spoofer
In ARP Spoofer we use a technique to send spoof packets to victim machine, which 
results in replacing mac address of a gateway or router with attacker mac address 
in victim arp table.
After achieving this all packets which are send to router by victim will come to 
attacker and victim will not even know about that

# Requirements
(install all the below libraries)

    pip3 install scapy
    pip3 install art
    pip3 install tabulate
# HOW TO USE IT
 first allow all permission
  
    git clone https://github.com/civicvchackoC3/ARP-Spoofer.git
    cd Arp-Spoofer.py
    chmod +x Arp-Spoofer.py
# requirements.txt
    pip install -r requirements.txt
# RUN
    ./Arp-Spoofer.pY
    OR
    python3 Arp-Spoofer.py
# Developer
    civic v chacko
