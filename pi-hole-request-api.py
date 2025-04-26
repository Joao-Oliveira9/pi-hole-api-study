import requests

payload = {"password": "CI3ZjCva"}

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

domain_block = "maisesports.com.br"

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

def queryRegister(pihole_address,domain,length):
    """ "https://pi.hole:443/api/queries?client_ip=192.168.15.5" """
    sid = create_session(password,pihole_address)
    """ url = "https://" + pihole_address + "/api/queries?client_ip=192.168.15.5&domain=x.com&length=4&sid="+ sid """

    url = "https://" + pihole_address + "/api/queries?client_ip=192.168.15.5&domain="+ domain + "&length="+ length +"&sid="+ sid
    response = requests.request("GET", url, json=payload, verify=False)
    """ response =  response.json() """
    print(response.json())
    delete_session(sid,pihole_address)
""" http://192.168.0.22/api/queries?client_ip=192.168.0.8&length=1 """



def add_domain_blocklist(domain,pihole_address):
    sid = create_session(password,pihole_address)
    payload= {
    "domain": domain,
    "comment": "teste",
    "groups": [
        0
    ],
    "enabled": True
    }

    """ sid = "DbyYZZHQhLL0RIc5yIx97A=" """
    url = "https://" + pihole_address + "/api/domains/deny/exact?sid=" + sid
    """ https://pi.hole:443/api/domains/deny/exact """

    response = requests.request("POST", url, json=payload, verify=False)

    response =  response.json()
    print(response)
    delete_session(sid,pihole_address)
    

def create_group(pihole_address,group_name):
    payload = {    
        "name" : group_name
    }
    sid = create_session(password,pihole_address)
    url = "https://" + pihole_address + "/api/groups?sid=" + sid
    response = requests.request("POST",url,json=payload,verify=False)
    response = response.json()
    print(response)
    delete_session(sid,pihole_address)

def remove_group(pihole_address,group_name):
    """  payload = {    
        "name" : group_name
    } """

    sid = create_session(password,pihole_address)
    """ print(sid) """
    """ url = "https://" + pihole_address + "/api/groups?sid=" + sid """
    url = "https://" + pihole_address + "/api/groups/" + group_name + "?sid=" + sid
    print(url)
    """ url = "https://" + pihole_address + "/api/groups/name" + group_name + "?sid=" + sid """
    """ response = requests.request("DELETE",url,json=payload,verify=False) """
    response = requests.request("DELETE",url,verify=False)
    """ response = response.json() """
    print(response)
    delete_session(sid,pihole_address)


""" /** *! funcao inicialmente usara o ip mas posteriormente sera trocada pelo arpscan usando mac address """
def create_client(pihole_address,password,client_name,group_id):
    sid = create_session(password,pihole_address)
    payload = {
        "client" : client_name,
        "groups" : [group_id]
    }

    url = "https://" + pihole_address + "/api/clients?sid=" + sid
    response = requests.request("POST",url,json=payload,verify=False)
    print(response.json())

    delete_session(sid,pihole_address)

def get_id_group(pihole_address,password,group_name)->str:
    sid = create_session(password,pihole_address)

    url = "https://" + pihole_address + "/api/groups/" + group_name + "?sid=" + sid
    response = requests.request("GET",url,verify=False)
    response  = response.json()
    

    group_id = response['groups'][0]['id']
    
    return group_id

    delete_session(sid,pihole_address)

def insert_client_with_group(client_name,group_name,pihole_address,password):
    group_id = get_id_group(pihole_address,password,group_name)
    create_client(pihole_address,password,client_name,group_id)


""" create_group(pihole_address,"testando-api") """
""" remove_group(pihole_address,"teste2") """
""" queryRegister(pihole_address,"x.com","4") """
""" add_domain_blocklist(domain_block,pihole_address) """
""" create_client(pihole_address,password,"192.168.15.5") """
""" group_id = get_id_grupo(pihole_address,password,"teste")
print(group_id) """

insert_client_with_group("192.168.15.5","teste",pihole_address,password)
