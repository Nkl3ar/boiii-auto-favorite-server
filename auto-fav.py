from urllib.request import urlopen
import json
import os


# its T7 because its loading all the T7/Black Ops 3 servers
game = "T7"
# this will store only the ip:port
extractedServersIPandPort = []

# iw4madmin master server api
# instance endpoint contains all the data in a json format
IW4MadminURL = "http://api.raidmax.org/instance/"

# opening the url
print("Connecting to the iw4madmin master server...\n")
IW4MadminResponse = urlopen(IW4MadminURL)
# parsing the json and storing it
IW4MadminData = json.loads(IW4MadminResponse.read())

print("Combing through the data...\n")
# iterating over all the data
for data in IW4MadminData:
    # iterating over only the servers
    for server in data["servers"]:
        # if we stumble upon a T7 gameserver
        if(server["game"]==game):
            # we save it and add a new line character at the end to make things easier later
            ip = server["ip"]+":"+str(server["port"])+'\n'
            extractedServersIPandPort.append(ip)


print("Saving...\n")
# check if boiii_players/user exists, if not, create it
isExist = os.path.exists("boiii_players/user")
if not isExist:
   os.makedirs("boiii_players/user")

# now we just write into the favorite servers file
# and thats it
f = open("boiii_players/user/favorite_servers.txt", "w")
f.writelines(extractedServersIPandPort)
f.close()

print("Done :)\n")

    


    

