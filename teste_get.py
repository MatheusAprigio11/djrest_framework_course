import requests

headers = {'Authorization': 'Token 6775129258ca19e1b24f3f459713cd4ea93a0f20'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

#testando se o endpoint esta correto
assert resultado.status_code == 200

#testando quantidade de registros

assert resultado.json()['count'] == 6