# Login Penetration Test

## Summary: 
* A login form penetration test written in python3.  
* This script will submit 1000 fake users into a login form.  
* Additionally, we assume there is a csrf_token and some cookies set during the initial load of the form which also must be submit with the form data.

## Mock Data Source:
* https://www.mockaroo.com/
* Great resource for generating fake data for databases, etc.

## Python Version:
* Python 3.7.0

## Install these packages using: pip3 install <package_name>
* certifi (recomended by python3 for SSL certs)
* requests (for this project)
* BeautifulSoup (for this project) - https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

## Terminal Command Formats:
* python3 <file>
* pip3 install <package>

