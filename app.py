from pi_hole_request_api import RequisicoesPihole
from flask import Flask,request
import requests

pihole = RequisicoesPihole(password="CI3ZjCva", pihole_address="192.168.15.2")


""" id = pihole.get_id_group("teste")

print(id) """
app = Flask(__name__)

""" @app.route("/")
def hello_world():
        print('passei aqui')
        pihole.remove_group('tee')
        return 'hello word' """

@app.route("/get_registro", methods=['GET'])
def get_registro():
   data = request.get_json() 
   domain_name = data['domain-name']
   length = data['length']
   """ print(data) """
   """ print(length) """
   response = pihole.query_register(domain_name,length)

   return response
  


if __name__ == "__main__":    
    app.run(host='0.0.0.0',port=8000)
