from pi_hole_request_api import RequisicoesPihole
from flask import Flask

pihole = RequisicoesPihole(password="CI3ZjCva", pihole_address="192.168.15.2")


""" id = pihole.get_id_group("teste")

print(id) """
app = Flask(__name__)

@app.route("/")
def hello_world():
        print('passei aqui')
        pihole.remove_group('tee')
        return 'hello word'




if __name__ == "__main__":    
    app.run(host='0.0.0.0',port=8000)
