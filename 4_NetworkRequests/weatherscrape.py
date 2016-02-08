import urllib
import re

# Got to weatherzone, ctrl+f "geo"
# http://www.weatherzone.com.au/

htmltext = urllib.urlopen("http://geo1.weatherzone.com.au/public/wz/wfs?service=WFS&version=1.0.0&request=GetFeature&typeName=wz:forecasts_daily&outputFormat=json&sortBy=priority%20D&viewparams=timestamp:2016-02-01%2010:00&_h=www.weatherzone.com.au").read()
print htmltext
#"loc_name":"Hobart","date":"2016-01-31Z","day_name":"Monday","temperature_min":18,"temperature_max":22
