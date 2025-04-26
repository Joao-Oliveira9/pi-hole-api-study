from pi_hole_request_api import RequisicoesPihole
from flask import Flask,request,jsonify
import requests

pihole = RequisicoesPihole(password="CI3ZjCva", pihole_address="192.168.15.2")

app = Flask(__name__)

@app.route("/get_registro", methods=['GET'])
def get_registro():
   data = request.get_json() 
   domain_name = data['domain-name']
   length = data['length']
   response = pihole.query_register(domain_name,length)
   return response

@app.route("/add_domain_blocklist",methods=['POST'])
def post_domain():
    data = request.get_json()
    domain_name = data['domain-name']
    group_name = data['group-name']
    pihole.add_domain_blocklist(domain_name,group_name)

    message = f'Domínio {domain_name} adicionado a lista de bloqueios do grupo {group_name}' 
    return jsonify(message),200

@app.route("/create_group",methods=['POST'])
def post_group():
    data = request.get_json()
    group_name = data['group-name']
    pihole.create_group(group_name)
    message = f'Grupo {group_name} criado com sucesso'
    return jsonify(message)

""" O cliente deve pertencer a um grupo nesse endpoint """
@app.route("/add_cliente",methods=['POST'])
def post_client_grupo():
    data = request.get_json()
    client_address = data['client_address']
    group_name = data['group_name']

    pihole.insert_client_with_group(client_address,group_name)

    message = f'Cliente {client_address} foi inserido no grupo {group_name} com sucesso'
    return jsonify(message)

if __name__ == "__main__":    
    app.run(host='0.0.0.0',port=8000)
