from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only':True} #NÃO VAI SER APRESENTADO QUANDO ALGUEM CONSULTAR, SERA EXIGIDO APENAS NO CADASTRO.
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship - Apresenta as avaliações que o curso possui em forma de lista - cuidado ao usar (exemplo usar qnd foi relacionamento 1,1)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field - Cria o link da api para acessar as informações - recomendado
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field - Lista com os ids de cada avaliação
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )