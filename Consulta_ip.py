import requests
print(""""
############################
#       CONSULTA IP        #
############################
""")
def consulta():
    ipp = input("Digite o endereço ip, ex :170.245.225.107: ")
    url = requests.get(f'https://freegeoip.app/json/{ipp}')
    json = url.json()
    ips = json['ip']
    Pais = json['country_name']
    estado = json['region_name']
    cidade= json['city']
    cep = json['zip_code']

    print(f"Ip:{ips}\nPais:{Pais}\nEstado:{estado}\ncidade:{cidade}\nCep:{cep}")

    con = int(input("Deseja fazer uma nova consulta ?: \n1-S\n2-N\n"))
    if con == 1:
        consulta()
    else:
      print('Saindo...')
      exit()
consulta()