import requests

url = "https://192.168.15.2/api/auth"
payload = {"password": "CI3ZjCva"}

response = requests.request("POST", url, json=payload, verify=False)

response =  response.json()
print(response)

sid = response["session"]["sid"]
print(sid)

def status_blockinlist():
    sid = "9YrOaVbC9kEc8qzePs3y+g="
    url = "https://192.168.15.2/api/dns/blocking?sid=" + sid
    print(url)

    response = requests.request("GET",url,verify=False)
    print(response.json())

""" teste(sid) """

""" status_blockinlist()  """

""" DOMIAN MANAGEMENT /domains/{type}/{kind}/{domain} """

def add_domain_blocklist(sid):
    payload= {
    "domain": "maisesports.com.br",
    "comment": "teste",
    "groups": [
        0
    ],
    "enabled": True
    }

    """ sid = "DbyYZZHQhLL0RIc5yIx97A=" """
    url = "https://192.168.15.2/api/domains/deny/exact?sid=" + sid
    """ https://pi.hole:443/api/domains/deny/exact """

    response = requests.request("POST", url, json=payload, verify=False)

    response =  response.json()
    print(response)
    
    
""" add_domain_blocklist(sid) """



def queryRegister(sid):
    """ "https://pi.hole:443/api/queries?client_ip=192.168.15.5" """

    url = "https://192.168.15.2/api/queries?client_ip=192.168.15.5&sid="+ sid
    response = requests.request("POST", url, json=payload, verify=False)
    response =  response.json()
    print(response)

""" queryRegister(sid) """