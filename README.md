# MAC Address API Service

This is a simple program that makes an api call to www.macaddress.io with a MAC address and returns associated Vendor details.


## Usage
**www.macaddress.io provides 3 specific details for a given MAC Address/OUI : 'Vendor Details', 'Block Details' & 'MAC Address Details'**

These details can be fetched via REST API either using Query Based or Header Based Authentication.

I have used Header based Authentication here written in Python.

The Program runs on a docker container where MAC address and API Key needs to be passed as an argument else this would fail.

Example : docker run <image_name> <mac_address> <api_key>

*Note: API Key can be obtained by signing up on the www.macaddress.io page.*

## Execution Steps on Linux Server

**Prerequisite:**

*Docker and GIT must be installed*
*Access to Docker Hub*

1. Clone repository :: git clone -b dev https://github.com/kapil5kc/mac-n-REST.git
2. execute command: cd mac-n-REST 
3. docker build macapp . or docker-compose build
4. docker run <docker_image> <mac_address> <api_key>


## Response

Valid MAC Address and API Token : Status Code 200 OK - **Details Retrieved!**
else Error Message displayed

**Output of a valid MAC Address and Api Key:**

Valid MAC Address

Company Name registered with the MAC address is 'allora Factory Bvba' with address at 'Lijsterlaan 11 Bornem 2880 BE'


## Technical Debt
### Security
Implement a seure solution to pass api key in the URL ex: JWT
