from rest_framework import viewsets, generics
from biblioteca.models import Livro, Locador, Locacao
from biblioteca.serializer import LivroSerializer, LocadorSeralizer, LocacaoSerializer, ListaLocacoesLocadorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LocadorViewSet(viewsets.ModelViewSet):
    queryset = Locador.objects.all()
    serializer_class = LocadorSeralizer

class LocacaoViewSet(viewsets.ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer

class ListaLocacoesLocador(generics.ListAPIView):
    def get_queryset(self):
        queryset = Locacao.objects.filter(locador_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaLocacoesLocadorSerializer
