import requests

proxies = {
  'https': '89.117.22.218:8080',
}

url = 'https://cleantalk.org/blacklists/ivanov@gmail.com'

response = requests.post(url, proxies=proxies)

print(response.text)