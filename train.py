import requests

# Define the URL
url = "https://login.microsoftonline.com/dda73bd8-c44f-42f8-ae35-04e83d5e5037/oauth2/token"

# Define headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "fpc=AkgOGbX-feBHoU2bxtgvTRFv_gTwAQAAACzfad8OAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd"
}

# Define form data
data = {
    "grant_type": "client_credentials",
    "client_id": "0d5f8eb0-14f3-4d0a-b0dc-c5f6e02988ca",
    "client_secret": "D4h8Q~Ta1rrsfWa9wlxHiKPfk7KUbpFl4wYMUakB",
    "resource": "https://management.azure.com/"
}

# Define proxy
proxies = {
    "http": "http://your-proxy.com:port",
    "https": "http://your-proxy.com:port"
}

# Make the request
response = requests.post(url, headers=headers, data=data, proxies=proxies)

# Print response
print(response.status_code)
print(response.text)
