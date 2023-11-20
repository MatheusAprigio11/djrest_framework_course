import requests

headers = {'Authorization': 'Token 6775129258ca19e1b24f3f459713cd4ea93a0f20'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo" : "Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

resultado = requests.put(url=f'{url_base_cursos}2/', headers=headers, data=curso_atualizado)


assert resultado.status_code == 200