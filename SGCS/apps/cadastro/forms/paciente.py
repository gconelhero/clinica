# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext_lazy as _

from SGCS.apps.cadastro.models import Paciente


class PacienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.fields['limite_de_credito'].localize = True

    class Meta:
        model = Paciente
        fields = ('nome_razao_social','data_entrada', 'tipo', 'limite_de_credito', 'informacoes_adicionais', )
        widgets = {
            'nome_razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'data_entrada': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}, format=('%Y-%m-%d')),
            'limite_de_credito': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'informacoes_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_razao_social': _('Razão Social'),
            'tipo': _('Tipo de Paciente'),
            'data_entrada': _('Data de Entrada'),
            'limite_de_credito': _('Limite de Crédito'),
            'informacoes_adicionais': _('Informações Adicionais'),
        }

    def save(self, commit=True):
        instance = super(PacienteForm, self).save(commit=False)
        instance.criado_por = self.request.user
        if commit:
            instance.save()
        return instance
