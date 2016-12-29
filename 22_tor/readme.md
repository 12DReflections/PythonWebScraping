# Python Tor Automation
- Author Julian Wise 2016 

####
This program is an automated web crawler hidden as a human to increase a site's traffic.
The randomness is generated through a tor browser.
The exit pointed is a preferred country.
On cycle the crawler will go to the site and will randomly perform certain randomised actions. 


#### Setup 

The dependencies are a pain

stem (sudo apt-get install python-stem)
socksipy (sudo apt-get install python-socksipy)
tor (sudo apt-get install tor)
python 2.7 (which is often installed by default)

Torrc file (normally located in /etc/tor/torrc on unix systems)
- To open the port and enable cookie authentication
- Enabling control port on 9051
- Cookie authentication (check https://stem.torproject.org/faq.html#)


#### Dependencies

- sudo apt-get install python-stem
- sudo apt-get install python-socksipy
- sudo apt-get install tor

or

sudo apt-get install tor

sudo apt-get remove --purge tor
--

sudo apt-get install python-stem
--
sudo apt-get install python-socksipy
or
sudo apt-get install python-socks
--


and cookie authentication (check https://stem.torproject.org/faq.html#)

- sudo pip install stem
- sudo pip install PySocks


http://stackoverflow.com/questions/9887505/how-to-change-tor-identity-in-python
http://stackoverflow.com/questions/9925381/python-script-exception-with-tor


#### Setup

- refer to /connection_test for scripts to set TOR up

#### mech_agent folder

- Contains code of setting up a randomised mechanize browser


=======
# Library
https://stem.torproject.org/api/connection.html //Details on connection


sudo /etc/init.d/tor stop.

1. Install tor
2. Install dependencies
3. Reinstall tor
4. Restart service

