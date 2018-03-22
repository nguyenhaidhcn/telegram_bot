import os
import subprocess
import re
import requests

#token of bot
TOKEN = "525968331:AAHjiranH89hLS60L7wOaWB0gVjiIw"
#id of group
CHAT_ID = "-31023294732"
#api url
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

#add more process name here
PROCESS_NAMES=["pycharm", "test"];
PROCESS_PATH=["/","/"];


def findThisProcess( process_name ):
  ps     = subprocess.Popen("ps -eaf | grep "+process_name, shell=True, stdout=subprocess.PIPE)
  output = ps.stdout.read()
  ps.stdout.close()
  ps.wait()

  return output

# Thise function you can use
def isThisRunning( process_name , path):
  output = findThisProcess( process_name )

  print (path + process_name)
#search path of process on output
  if re.search(path+process_name, output) is None:
    return False
  else:
    return True

# Example of how to use
for num in range(0,2):


    if isThisRunning(PROCESS_NAMES[num], PROCESS_PATH[num]) == False:

        print("Not running")
        text = PROCESS_NAMES[num] + " process not running"
        url = URL + "sendMessage?text={}&chat_id={}".format(text, CHAT_ID)

    #send message to groups
        requests.get(url)
    else:
        print("Running!")
        text = PROCESS_NAMES[num] + " process running"
        url = URL + "sendMessage?text={}&chat_id={}".format(text, CHAT_ID)
  # send message to groups
        requests.get(url)
