# MAC Address API Service

This is a simple program that makes an api call to www.macaddress.io with a MAC address and returns associated Vendor Name.


## Usage

The Program runs on a docker container where MAC address can be passed as an argument.

Example : docker run <image_name> <mac_address>

If no parameters are passed a default mac address<Example 44:38:39:ff:ef:57> is considered.


## Response

Valid MAC Address : Status Code 200 OK
else Error Message displayed

## Technical Debt
### Security
Implement a seure solution to pass api key in the URL
