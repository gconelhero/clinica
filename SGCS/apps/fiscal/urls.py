# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'fiscal'
urlpatterns = [
    # Nota fiscal saida
    # fiscal/notafiscal/saida/adicionar/
    path('notafiscal/saida/adicionar/',
        views.AdicionarNotaFiscalSaidaView.as_view(), name='addnotafiscalsaidaview'),
    # fiscal/notafiscal/saida/listanotafiscal
    path('notafiscal/saida/listanotafiscal/',
        views.NotaFiscalSaidaListView.as_view(), name='listanotafiscalsaidaview'),
    # fiscal/notafiscal/saida/editar/
    path('notafiscal/saida/editar/<int:pk>/', views.EditarNotaFiscalSaidaView.as_view(
    ), name='editarnotafiscalsaidaview'),
    # fiscal/notafiscal/saida/importar/
    path('notafiscal/saida/importar/',
        views.ImportarNotaSaidaView.as_view(), name='importarnotafiscalsaida'),
    # fiscal/notafiscal/saida/gerar/
    path('notafiscal/saida/gerar/<int:pk>/',
        views.GerarNotaFiscalSaidaView.as_view(), name='gerarnotafiscalsaida'),

    # Nota fiscal entrada
    # fiscal/notafiscal/entrada/listanotafiscal
    path('notafiscal/entrada/listanotafiscal/',
        views.NotaFiscalEntradaListView.as_view(), name='listanotafiscalentradaview'),
    # fiscal/notafiscal/entrada/editar/
    path('notafiscal/entrada/editar/<int:pk>/', views.EditarNotaFiscalEntradaView.as_view(
    ), name='editarnotafiscalentradaview'),
    # fiscal/notafiscal/entrada/importar/
    path('notafiscal/entrada/importar/',
        views.ImportarNotaEntradaView.as_view(), name='importarnotafiscalentrada'),

    # Configuracao NF-e
    path('notafiscal/configuracaonotafiscal/',
        views.ConfiguracaoNotaFiscalView.as_view(), name='configuracaonotafiscal'),

    # Natureza operacao
    # fiscal/naturezaoperacao/adicionar/
    path('naturezaoperacao/adicionar/',
        views.AdicionarNaturezaOperacaoView.as_view(), name='addnaturezaoperacaoview'),
    # fiscal/naturezaoperacao/listanaturezaoperacao
    path('naturezaoperacao/listanaturezaoperacao/',
        views.NaturezaOperacaoListView.as_view(), name='listanaturezaoperacaoview'),
    # fiscal/naturezaoperacao/editar/
    path('naturezaoperacao/editar/<int:pk>/', views.EditarNaturezaOperacaoView.as_view(
    ), name='editarnaturezaoperacaoview'),

    # Grupo fiscal
    # fiscal/grupofiscal/adicionar/
    path('grupofiscal/adicionar/',
        views.AdicionarGrupoFiscalView.as_view(), name='addgrupofiscalview'),
    # fiscal/grupofiscal/listagrupofiscalview
    path('grupofiscal/listagrupofiscal/',
        views.GrupoFiscalListView.as_view(), name='listagrupofiscalview'),
    # fiscal/grupofiscal/editar/
    path('grupofiscal/editar/<int:pk>/',
        views.EditarGrupoFiscalView.as_view(), name='editargrupofiscalview'),

    # Acoes Nota Fiscal
    # Validar XML nota
    path('notafiscal/validar/<int:pk>/',
        views.ValidarNotaView.as_view(), name='validarnotafiscal'),
    # fiscal/notafiscal/emitir/
    path('notafiscal/emitir/<int:pk>/',
        views.EmitirNotaView.as_view(), name='emitirnotafiscal'),
    # Clonar nota
    path('notafiscal/copiar/<int:pk>/',
        views.GerarCopiaNotaView.as_view(), name='copiarnotafiscal'),
    # Cancelar nota
    path('notafiscal/cancelar/<int:pk>/',
        views.CancelarNotaView.as_view(), name='cancelarnotafiscal'),
    # Gerar DANFE
    path('notafiscal/gerardanfe/<int:pk>/',
        views.GerarDanfeView.as_view(), name='gerardanfe'),
    # Gerar DANFCE
    path('notafiscal/gerardanfce/<int:pk>/',
        views.GerarDanfceView.as_view(), name='gerardanfce'),

    # Comunicacao SEFAZ
    # Consultar cadastro
    path('notafiscal/consultarcadastro/',
        views.ConsultarCadastroView.as_view(), name='consultarcadastro'),
    # Inutilizar notas
    path('notafiscal/inutilizarnotas/',
        views.InutilizarNotasView.as_view(), name='inutilizarnotas'),
    # Consultar nota
    path('notafiscal/consultarnota/',
        views.ConsultarNotaView.as_view(), name='consultarnota'),
    path('notafiscal/consultarnota/<int:pk>/',
        views.ConsultarNotaView.as_view(), name='consultarnota'),
    # Baixar nota
    path('notafiscal/baixarnota/',
        views.BaixarNotaView.as_view(), name='baixarnota'),
    path('notafiscal/baixarnota/<int:pk>/',
        views.BaixarNotaView.as_view(), name='baixarnota'),
    # Manifestacao destinatario
    path('notafiscal/manifestacaodestinatario/',
        views.ManifestacaoDestinatarioView.as_view(), name='manifestacaodestinatario'),
]
