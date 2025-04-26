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


if __name__ == "__main__":    
    app.run(host='0.0.0.0',port=8000)
