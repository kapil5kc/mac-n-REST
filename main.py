import requests
import sys

if len(sys.argv) != 3:
  print("Invalid arguments! please provide MAC Address and API Key as parameters")
  exit()

mac = sys.argv[1]
apikey = sys.argv[2]

def IsMacValid(S):
  digits = S.split(':')
  if len(digits) == 1:
    digits = S.split('-')
    if len(digits) == 7:
      if digits[0] != '01':
        return False
      digits.pop(0)
  if len(digits) != 6:
    return False
  for digit in digits:
    if len(digit) != 2:
      return False
    try:
      int(digit, 16)
    except ValueError:
      return False
  return True

if IsMacValid(mac)== True:
  print("Valid MAC Address entered")
else:
  print("Invalid MAC Address, Kindly enter a correct MAC Address!")
  exit()

URL="https://api.macaddress.io"
path="/v1?output=json&search="
headers  = {"Accept": "application/json"}

params = {
  "apiKey": apikey,
}

r= requests.get(URL+path+mac, headers = headers, params=params)
print(r.status_code)

output=r.json()

if r.status_code!=200:
  print("Kindly enter a valid API Key")
else:
  vendor=output['vendorDetails']['companyName']
  vendorAddr=output['vendorDetails']['companyAddress']
  print("Company Name registered with the MAC address is '" +vendor+"' with address at '" + vendorAddr +"'")