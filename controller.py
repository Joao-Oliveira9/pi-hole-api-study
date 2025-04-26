from pi_hole_request_api import RequisicoesPihole

pihole = RequisicoesPihole(password="CI3ZjCva", pihole_address="192.168.15.2")


id = pihole.get_id_group("teste")

print(id)