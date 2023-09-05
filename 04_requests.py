import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)



url = 'https://w3schools.com/python/demopage.asp'
x = requests.post(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})

print(x.text)