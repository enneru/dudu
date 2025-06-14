#######DUDU########
####made by me :3##

import subprocess

#servers

username = "johndoe"
servers = ["10.0.0.1", "10.0.0.2", "xxx.xx.xx.x"]

#command arg / command to distribute

command = "echo"

def run_command(input):
    for x in servers:
        subprocess.run([input, x])

commandOverride = input("input command to override default:\n(leave blank for default)\n")
if not commandOverride:
    print(f"executing default command: {command}")
    run_command(command)
else:
    print(f"executing overridden command: {commandOverride}")
    run_command(commandOverride)

