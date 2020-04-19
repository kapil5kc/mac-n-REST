import requests
import sys


mac = sys.argv[1]
print("MAC Address : "+mac)

URL="https://api.macaddress.io/v1?apiKey=at_wEUVVeSHcoYTBCrtmArKoevOGaWVx&output=json&search="+mac
r= requests.get(URL)

output=r.json()

if r.status_code!=200:
  print("Kindly enter a valid MAC address")
else:
  vendor=output['vendorDetails']['companyName']
  print("Company Name registered with the MAC address:: " +vendor)