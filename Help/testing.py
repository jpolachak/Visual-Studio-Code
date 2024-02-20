import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host="192.168.254.24"
port="443"
url=f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface"

headers={
     "Accept":"application/yang-data+json",
     "Content-Type":"application/yang-data+json"
     }

response=requests.get(url, auth=("root","101mAgic01**"), headers=headers, verify=False)
jsondata=response.json()

print("-"*100)
print("{:<45}{:<30}{:<30}".format("Interface", "Ingress Octets", "Egress Octets"))
print("-"*100)

for interface in jsondata["Cisco-IOS-XE-interfaces-oper:interface"]:
     if interface['oper-status'] == 'if-oper-state-ready' and interface ['interface-type'] == 'iana-iftype-ethernet-csmacd':
       switchport = interface["name"]
       ingressoctets = interface["statistics"]["in-octets"]
       egressoctets = interface["statistics"]["out-octets"]
       print("{:<45}{:<30}{:<30}".format(switchport,ingressoctets,egressoctets))