import requests

class TestCursos:

    headers = {'Authorization': 'Token 6775129258ca19e1b24f3f459713cd4ea93a0f20'}

    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}4/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de programação em Ruby",
            "url": "http://prijasprijola.com.br/ruby"
        }
        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resultado.status_code == 201

    def test_put_curso(self):
        atualizado ={
            "titulo": "novo curso de ruby",
            "url": "http://prijasprijola.com.br/novocursoruby"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}1/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200


    def test_delete_curso(self):
        resultado = requests.delete(url=f'{self.url_base_cursos}1/', headers=self.headers)

        assert resultado.status_code == 204 and len(resultado.text) == 0