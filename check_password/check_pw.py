import requests
password = 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'  # password123
parameter = 'CBFDAC'
service = 'range'
url = "https://haveibeenpwned.com/api/v3/{service}/{parameter}"

res = requests.get(url)

print(res)
