import requests

headers = {'Authorization': 'Token 6775129258ca19e1b24f3f459713cd4ea93a0f20'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso ={
    "titulo": "scrum metodologia",
    "url": "http://www.geekuniversity.com.br/scrum"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

assert resultado.status_code == 201