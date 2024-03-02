#File showing show command output
import cli
cmds = ["show users", "show ip interface brief", "show ip ospf neighbor", "show tcp br"]

with open("/bootflash/guest-share/TEST.txt", "w") as outfile:

	for c in cmds:
		output = cli.execute(c)
outfile.write(output)