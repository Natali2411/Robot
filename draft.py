# pip install --trusted-host pypi.python.org pack_name
from zeep import Client
from zeep import xsd
from zeep.wsse.username import UsernameToken
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
import ssl

session = Session()
session.verify = False
#transport = Transport(session=session)
#transport = Transport(http_auth=HTTPBasicAuth("testuser", "testuser"))
ssl._create_default_https_context = ssl._create_unverified_context
client = Client('http://kwsesbapu06.alfa.bank.int:8280/services/CardLogisticsWF?wsdl')
#http_headers = client.wsse.apply(envelope, http_headers)
result = client.service.getCards(shopId='8344')