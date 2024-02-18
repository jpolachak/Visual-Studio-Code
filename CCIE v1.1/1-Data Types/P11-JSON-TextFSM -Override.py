#!/usr/bin/python3
from netmiko import ConnectHandler, ssh_exception
import json

# Define dictionary
IP_dic = {'device_type': 'cisco_ios', 'ip': '192.168.254.11', 'username': 'magic', 'password': 'magic'}

try:
    net_connect = ConnectHandler(**IP_dic)

    # Send show command with textFSM filter to parse output
    output = net_connect.send_command("show vlan brief ", use_textfsm=True)
    net_connect.disconnect()

    # textFSM parsed the output variable type to be dictionary 
    # print (output)

    # Print all output using for loop
    for item in output:
        # print (item)
        if int(item['vlan_id']) < 1002 :
            print (item)
        else:
            print ('authentication failed')

    with open("output-01.json", "w") as outfile: 
        json.dump(output, outfile)

except ssh_exception.NetMikoAuthenticationException:
    print("Authentication failed. Please check your credentials.")
except Exception as e:
    print("An error occurred:", str(e))
