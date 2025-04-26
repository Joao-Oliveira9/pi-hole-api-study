import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RequisicoesPihole:
    def __init__(self, password, pihole_address):
        self.password = password
        self.pihole_address = pihole_address

    def create_session(self):
        url = f"https://{self.pihole_address}/api/auth"
        payload = {"password": self.password}
        response = requests.post(url, json=payload, verify=False)
        response = response.json()
        sid = response["session"]["sid"]
        return sid

    def delete_session(self, sid):
        url = f"https://{self.pihole_address}/api/auth?sid={sid}"
        requests.delete(url, verify=False)

    def query_register(self, domain, length):
        sid = self.create_session()
        url = f"https://{self.pihole_address}/api/queries?client_ip=192.168.15.5&domain={domain}&length={length}&sid={sid}"
        response = requests.get(url, verify=False)
        print(response.json())
        self.delete_session(sid)

    def add_domain_blocklist(self, domain, group_name):
        id_group = self.get_id_group(group_name)
        sid = self.create_session()
        payload = {
            "domain": domain,
            "comment": "teste",
            "groups": [id_group],
            "enabled": True
        }
        url = f"https://{self.pihole_address}/api/domains/deny/exact?sid={sid}"
        response = requests.post(url, json=payload, verify=False)
        print(response.json())
        self.delete_session(sid)

    def create_group(self, group_name):
        payload = {"name": group_name}
        sid = self.create_session()
        url = f"https://{self.pihole_address}/api/groups?sid={sid}"
        response = requests.post(url, json=payload, verify=False)
        print(response.json())
        self.delete_session(sid)

    def remove_group(self, group_name):
        sid = self.create_session()
        url = f"https://{self.pihole_address}/api/groups/{group_name}?sid={sid}"
        print(url)
        response = requests.delete(url, verify=False)
        """ print(response.json()) """
        self.delete_session(sid)

    def create_client(self, client_name, group_id):
        sid = self.create_session()
        payload = {
            "client": client_name,
            "groups": [group_id]
        }
        url = f"https://{self.pihole_address}/api/clients?sid={sid}"
        response = requests.post(url, json=payload, verify=False)
        print(response.json())
        self.delete_session(sid)

    def get_id_group(self, group_name):
        sid = self.create_session()
        url = f"https://{self.pihole_address}/api/groups/{group_name}?sid={sid}"
        response = requests.get(url, verify=False)
        response = response.json()
        group_id = response['groups'][0]['id']
        self.delete_session(sid)
        return group_id

    def insert_client_with_group(self, client_name, group_name):
        group_id = self.get_id_group(group_name)
        self.create_client(client_name, group_id)

    def delete_client(self, client_address):
        sid = self.create_session()
        url = f"https://{self.pihole_address}/api/clients/{client_address}?sid={sid}"
        response = requests.delete(url, verify=False)
        self.delete_session(sid)

""" create_group(pihole_address,"testando-api") """
""" remove_group(pihole_address,"teste2") """
""" queryRegister(pihole_address,"x.com","4") """
""" add_domain_blocklist("facebook.com",pihole_address,"teste") """
""" create_client(pihole_address,password,"192.168.15.5") """
""" group_id = get_id_grupo(pihole_address,password,"teste")
print(group_id) """
""" insert_client_with_group("192.168.15.5","teste",pihole_address,password) """

""" delete_client(pihole_address,"192.168.15.5") """
