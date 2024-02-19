import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = "192.168.254.11"
port = "443"
url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-interfaces-oper:interface"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

try:
    response = requests.get(url, auth=("root", "101mAgic01**"), headers=headers, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors
    jsondata = response.json()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
    print(f"Response content: {response.content}")
    exit(1)
except json.JSONDecodeError as err:
    print(f"JSON decoding error occurred: {err}")
    print(f"Response content: {response.content}")
    exit(1)

print("-" * 100)
print("{:<45}{:<30}{:<30}".format("Interface", "Ingress Octets", "Egress Octets"))
print("-" * 100)

for interface in jsondata["Cisco-IOS-XE-interfaces-oper:interface"]:
    if interface['oper-status'] == 'if-oper-state-ready' and interface['type'] == 'iana-if-type:ethernetCsmacd':
        switchport = interface["name"]
        ingressoctets = interface["statistics"]["in-octets"]
        egressoctets = interface["statistics"]["out-octets"]
        print("{:<45}{:<30}{:<30}".format(switchport, ingressoctets, egressoctets))
