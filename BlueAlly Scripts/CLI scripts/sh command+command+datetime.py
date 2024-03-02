#File showing show command output
#With additional --including the show commands
#With additional current date and time added
import cli
from datetime import datetime

cmds = ["show users", "show ip interface brief", "show ip ospf neighbor", "show ip route summary"]

# Generate the filename with the current date
current_date = datetime.now().strftime("%m_%d_%Y")
filename = f"TEST_{current_date}.txt"

with open(f"/bootflash/guest-share/{filename}", "w") as outfile:
    for c in cmds:
        # Write the command to the output file
        outfile.write(f"Command: {c}\n")
        
        #Execute the command and capture the output
        output = cli.execute(c)
        
        #Write the output to the output file
        outfile.write(output)