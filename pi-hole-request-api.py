import requests
payload = {"password": "CI3ZjCva"}
""" url = "https://192.168.15.2/api/auth"
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
 """
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
password = "CI3ZjCva"
pihole_address = "192.168.15.2"

""" geração da sid e exclusao da sid """

""" Cria uma sessao e envia """
def create_session(password,pihole_address):
    url = "https://" + pihole_address + "/api/auth"
    """ print(url) """
    payload = {"password": password}
    response = requests.request("Post",url,json=payload,verify=False)
    response = response.json()
    """ print(response) """
    sid = response["session"]["sid"]
    """ print(sid) """
    return sid


def delete_session(sid,pihole_address):
    url = "https://" + pihole_address + "/api/auth?sid=" + sid
    """ print(url) """
    response = requests.request("Delete",url,verify=False)
    """ response = response.json() """
    """ print(response) """

def queryRegister(pihole_address):
    """ "https://pi.hole:443/api/queries?client_ip=192.168.15.5" """
    sid = create_session(password,pihole_address)
    url = "https://" + pihole_address + "/api/queries?client_ip=192.168.15.5&domain=x.com&length=4&sid="+ sid
    response = requests.request("GET", url, json=payload, verify=False)
    """ response =  response.json() """
    print(response.json())
    delete_session(sid,pihole_address)
""" http://192.168.0.22/api/queries?client_ip=192.168.0.8&length=1 """

""" password = "CI3ZjCva"
pihole_address = "192.168.15.2" """

queryRegister(pihole_address)
""" criando uma sessao """
""" sid = create_session(password,pihole_address)  """
""" print(sid)  """

""" delete_session(sid,pihole_address) """


""" queryRegister("opIVV0VHU7paj4YRDFXboA=") """

""" http://192.168.0.22/api/queries?client_ip=192.168.0.8&length=1 """