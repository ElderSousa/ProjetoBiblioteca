from rest_framework import serializers
from biblioteca.models import Livro, Locador, Locacao

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'isbn']

class LocadorSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Locador
        fields = '__all__'

class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locacao
        exclude = []

class ListaLocacoesLocadorSerializer(serializers.ModelSerializer):
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Locacao
        fields = ['id', 'livro', 'locador', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

