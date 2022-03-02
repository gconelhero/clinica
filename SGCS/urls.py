# -*- coding: utf-8 -*-

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SGCS.apps.base.urls')),
    path('login/', include('SGCS.apps.login.urls')),
    path('cadastro/', include('SGCS.apps.cadastro.urls')),
    path('fiscal/', include('SGCS.apps.fiscal.urls')),
    path('vendas/', include('SGCS.apps.vendas.urls')),
    path('compras/', include('SGCS.apps.compras.urls')),
    path('financeiro/', include('SGCS.apps.financeiro.urls')),
    path('estoque/', include('SGCS.apps.estoque.urls')),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
