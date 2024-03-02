import cli
cmds = ["show ip interface brief", "show ip ospf neighbor", "show ip route", "show log"]

with open("/bootflash/guest-share/RCA_Capture.txt", "w") as outfile:

	for c in cmds:
		output = cli.execute(c)
		outfile.write(output)