http://www.chancellors.co.uk/properties/search?map=false&area=New+Barnet&longitude=0&latitude=0&radius=5&saleType=Rent

alias t='/usr/bin/time -f "\ntime: %E"'
t java -jar oxpath1.1.jar -browser=htmlunit -query=test.oxp -xml | grep -v [INFO]
t python test.py
t wkhtmltopdf "http://www.chancellors.co.uk/properties/search?map=false&area=New+Barnet&longitude=0&latitude=0&radius=5&saleType=Rent" test.pdf; open test.pdf

oxpath 22.04s, wkhtmltopdf 07.57s, py+phsj 03.32 (needs more simulations)

http://www.2globalnomads.info/2013/06/blogger-dynamic-views-css-fail-bug-custom-reload.html
oxpath fails, wkhtmltopdf inconsistant, py+phsj works
