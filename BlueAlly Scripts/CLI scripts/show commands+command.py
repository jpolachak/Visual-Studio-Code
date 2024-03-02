#File showing show command output
#With additional --including the show commands
import cli

cmds = ["show users", "show ip interface brief", "show ip ospf neighbor", "show tcp br"]

with open("/bootflash/guest-share/TEST.txt", "w") as outfile:
    for c in cmds:
        #Write the command to the output file
        outfile.write(f"Command: {c}\n")
        
        #Execute the command and capture the output
        output = cli.execute(c)
        
        # Write the output to the output file
        outfile.write(output)
        