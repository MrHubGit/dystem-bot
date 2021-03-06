Dystem discord bot
==================

Dystem discord bot enforces the rules on the discord server, whilst supply new bounties for work requested by community leaders.

## Install Guide

The bot has been tested to work on Ubuntu 16.04. You must run the python script under python 3. 

You must be running a Dysten node on the server in order to get price information using the ```!about``` command.

Python / bot code installation:

```  
apt install python3-pip && sudo apt-get install python3-setuptools && pip3 install discord.py && apt install python3 && apt install python-minimal
 && alias python='python3' && git clone https://github.com/Dystem/dystem-bot.git 
 ``` 

Now you must add your discord bot secret key:

```  
cd dystem-bot 
```

``` 
touch secrets.py 
```

``` 
vi secrets.py 
```

Then add the line replacing the section with the secret bot key geenrated on your discord developer account: 

``` 
TOKEN = "<YOUR SECRET TOKEN>" 
``` 

## Launch daemon

``` 
sudo nano /lib/systemd/system/myscript.service
``` 

Then add the following content to the systemd script 

``` 
[Unit]
Description=My Script Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /root/dystem-bot/main.py

[Install]
WantedBy=multi-user.target
``` 

Then set peemissions on the script

``` 
sudo chmod 644 /lib/systemd/system/myscript.service
``` 

Launch the daemon 

``` 
sudo systemctl daemon-reload
sudo systemctl enable myscript.service
``` 

Then reboot 

``` 
reboot
``` 


Then on restart check the service is up and running

``` 
sudo systemctl status myscript.service
``` 

## Configuration and customisation
There is now a configuration file ```config.py``` that contains all the customisaion settings. To use the bot for your own purposes change the configuration to match your coin.