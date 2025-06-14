#######DUDU########
####made by me :3##

import subprocess

#username and servers are stored in the "config" file
#the first line is reserved for username and all subsequent
#hande server addresses

servers = []

conf = open("config")
username = conf.readline()
for x in conf:

    servers.append(x.strip())
conf.close()

#command arg / command to distribute to servers

#default of "echo", can be overridden at runtime or set here.
command = "echo"

#executes given command over array of servers
def run_command(input):
    for x in servers:
        subprocess.run([input, x])

#handles input of command and overriding
commandOverride = input("input command to override default:\n(leave blank for default)\n")
if not commandOverride:
    print(f"executing default command: {command}")
    run_command(command)
else:
    print(f"executing overridden command: {commandOverride}")
    run_command(commandOverride)

