import requests

#GET avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

#codigo de status HTTP
# print(avaliacoes.status_code)

#acessando dados da resposta
print(avaliacoes.json())

#acessando o nome do ultimo elemento da lista que retorna apos transformar em json
print(avaliacoes.json()['results'][-1]['nome'])


#GET Cursos

headers = {'Authorization': 'Token 6775129258ca19e1b24f3f459713cd4ea93a0f20'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.json())