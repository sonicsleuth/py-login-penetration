# Filename: login.py

import requests
import json
from bs4 import BeautifulSoup

# Load mock data (our list of fake users)
people = json.loads(open('mock_data.json').read())

# Log our results to this file.
f = open("log.txt", "a")

# Begin multiple login attempts
for person in people:
    # Load the Login Form to get our cookies and unique csrf_token.
    print("Load Form...")
    url_form    = 'https://domain.com/login-form'
    response    = requests.get(url_form, allow_redirects=False)
    cookie_data = {'SECURECOOKIE': response.cookies['SECURECOOKIE']}
    soup        = BeautifulSoup(response.content, 'html5lib')
    csrf_token  = soup.find('input', {'name': 'csrf'}).get('value')

    # Prepare the Form POST data
    email           = person.get("email")
    password        = person.get("password")
    csrf_token      = csrf_token

    # Post the Form with the above Cookies
    print("Submit Form POST...")
    url_post = 'https://domain.com/login-form'

    result = requests.post(url_post, allow_redirects=False, cookies=cookie_data, data={
        'email': email,
        'password': password,
        'csrf': csrf
    })
    # Terminal Output
    print("(" + email + " / " + password + ")")
    print(str(result.content))
    # Log Output
    f.write("Email: " + email + " Password: " + password + "\n")
    f.write(str(result.content) + "\n")

# end-of-file