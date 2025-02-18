import requests


def consulta_cep(cep):
    consulta_url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(consulta_url)
    if response.status_code == 200:
        return response.json()
    return "erro ao consultar CEP"

