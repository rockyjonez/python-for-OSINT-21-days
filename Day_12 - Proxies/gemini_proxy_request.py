import requests

def make_request_with_proxy(url, proxy):
  """
  Makes a request to a URL using a proxy.

  Args:
    url: The URL to make the request to.
    proxy: The proxy to use, in the format 'http://<proxy_host>:<proxy_port>'.
  """
  proxies = {
      'http': proxy,
      'https': proxy,
  }
  try:
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()  # Raise an exception for bad status codes
    print(response.text)
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Example usage:
url = 'https://cleantalk.org/blacklists/ivanov@gmail.com'
proxy = '103.106.231.188:42488'  # Replace with your actual proxy

make_request_with_proxy(url, proxy)