from rest_framework import serializers

from django.db.models import Avg

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
    
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A Validação deve ser um inteiro de 1 a 5.')


class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship - Apresenta as avaliações que o curso possui em forma de lista - cuidado ao usar (exemplo usar qnd foi relacionamento 1,1)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field - Cria o link da api para acessar as informações - recomendado
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field - Lista com os ids de cada avaliação
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2