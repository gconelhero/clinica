# -*- coding: utf-8 -*-


from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum    
from SGCS.apps.base.custom_views import CustomListView

from SGCS.apps.financeiro.models import MovimentoCaixa
from SGCS.apps.cadastro.models import Paciente, paciente

from datetime import datetime, timedelta
from SGCS.apps.financeiro.models.lancamento import Entrada, Saida

from SGCS.apps.vendas.models.vendas import PedidoVenda


class FluxoCaixaView(CustomListView):
    template_name = "financeiro/fluxo_de_caixa/fluxo.html"
    success_url = reverse_lazy('financeiro:fluxodecaixaview')
    context_object_name = 'movimentos'
    permission_codename = 'acesso_fluxodecaixa'

    def get_queryset(self):
        try:
            data_inicial = self.request.GET.get('from')
            data_final = self.request.GET.get('to')

            if data_inicial and data_final:
                data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
                data_final = datetime.strptime(data_final, '%d/%m/%Y')
            elif data_inicial:
                data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
                data_final = data_inicial
            elif data_final:
                data_final = datetime.strptime(data_final, '%d/%m/%Y')
                data_inicial = data_final
            else:
                data_final = data_inicial = datetime.today().strftime('%Y-%m-%d')

        except ValueError:
            data_final = data_inicial = datetime.today().strftime('%Y-%m-%d')
            messages.error(
                self.request, 'Formato de data incorreto, deve ser no formato DD/MM/AAAA')

        return MovimentoCaixa.objects.filter(data_movimento__range=(data_inicial, data_final))


'''
class FluxoCaixaView(CustomListView):
    template_name = "financeiro/fluxo_de_caixa/fluxo.html"
    success_url = reverse_lazy('financeiro:fluxodecaixaview')
    context_object_name = 'movimentos'
    permission_codename = 'acesso_fluxodecaixa'

    def get_queryset(self):
        try:
            data_inicial = self.request.GET.get('from')
            data_final = self.request.GET.get('to')

            if data_inicial and data_final:
                data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
                data_final = datetime.strptime(data_final, '%d/%m/%Y')
            elif data_inicial:
                data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
                data_final = data_inicial
            elif data_final:
                data_final = datetime.strptime(data_final, '%d/%m/%Y')
                data_inicial = data_final
            else:
                data_final = data_inicial = datetime.today().strftime('%Y-%m-%d')

        except ValueError:
            data_final = data_inicial = datetime.today().strftime('%Y-%m-%d')
            messages.error(
                self.request, 'Formato de data incorreto, deve ser no formato DD/MM/AAAA')
        try:
            saidas = float(PedidoVenda.objects.filter(data_emissao__range=(data_inicial, data_final)).aggregate(Sum('valor_total'))['valor_total__sum']) 
        except:
            saidas = float('00.00')
        
        try:
            saidas = saidas + float(Saida.objects.filter(data_pagamento__range=(data_inicial, data_final)).aggregate(Sum('valor_total'))['valor_total__sum'])
        except:
            saidas = float(saidas) + float('00.00')
        
        try:
            entradas = float(Entrada.objects.filter(data_pagamento__range=(data_inicial, data_final)).aggregate(Sum('valor_total'))['valor_total__sum'])
        except:
            entradas = float('00.00')

        try:
            inicial_entrada = float(Entrada.objects.filter(data_pagamento__lt=data_inicial).aggregate(Sum('valor_total'))['valor_total__sum'])
        except:
            inicial_entrada = float('00.00')
        try:
            inicial_saida = float(Saida.objects.filter(data_pagamento__lt=data_inicial ).aggregate(Sum('valor_total'))['valor_total__sum']) 
        except:
            inicial_saida = float('00.00')
        
        inicial = inicial_entrada - inicial_saida

        lucro_prejuizo = entradas - saidas
        saldo_final = inicial + lucro_prejuizo
        
        return data_final, inicial, entradas, saidas, lucro_prejuizo, saldo_final #MovimentoCaixa.objects.filter(data_movimento__range=(data_inicial, data_final))
'''