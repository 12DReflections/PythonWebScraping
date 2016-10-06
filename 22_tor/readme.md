stem (sudo apt-get install python-stem)
socksipy (sudo apt-get install python-socksipy)
tor (sudo apt-get install tor)
python (which is often installed by default)
you might also need to configure torrc file (normally located in /etc/tor/torrc on unix systems)
due to enabling control port on 9051
and cookie authentication (check https://stem.torproject.org/faq.html#)

sudo apt-get install python-stem
sudo apt-get install python-socksipy
sudo apt-get install tor

and cookie authentication (check https://stem.torproject.org/faq.html#)


sudo pip install stem
sudo  pip install PySocks


http://stackoverflow.com/questions/9887505/how-to-change-tor-identity-in-python
http://stackoverflow.com/questions/9925381/python-script-exception-with-tor
