
from django.contrib import admin
from django.urls import path, include
from biblioteca.views import LivroViewSet, LocadorViewSet, LocacaoViewSet, ListaLocacoesLocador
from rest_framework import routers

router = routers.DefaultRouter()
router.register('livros', LivroViewSet, basename='livros')
router.register('locadores', LocadorViewSet, basename='locadores')
router.register('locacoes', LocacaoViewSet, basename='locacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('locadores/<uuid:pk>/locacoes/', ListaLocacoesLocador.as_view())
]
