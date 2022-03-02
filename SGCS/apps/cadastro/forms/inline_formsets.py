# -*- coding: utf-8 -*-

from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import gettext_lazy as _

from SGCS.apps.cadastro.models import Pessoa, Endereco, Fazenda, Telefone, Email, Site, Banco, Documento, Responsavel


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ('tipo_endereco', 'logradouro', 'numero', 'bairro',
                  'complemento', 'pais', 'cpais', 'uf', 'cep', 'municipio', 'cmun',)

        labels = {
            'tipo_endereco': _('Tipo'),
            'logradouro': _("Logradouro"),
            'numero': _("Número"),
            'bairro': _("Bairro"),
            'complemento': _("Complemento"),
            'pais': _("País"),
            'cpais': _("Código do País"),
            'municipio': _("Município (sem acentuação)"),
            'cmun': _("Código do município"),
            'cep': _("CEP (Apenas dígitos)"),
            'uf': _("UF"),
        }
        widgets = {
            'tipo_endereco': forms.Select(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'cpais': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'cmun': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
        }


class FazendaForm(forms.ModelForm):

    class Meta:
        model = Fazenda
        fields = ('nome','nome_impressao_nota','inscricao_estadual','endereco','bairro','uf', 'cep', 'municipio', 'cmun',)

        labels = {
            'nome': _("Nome"),
            'nome_impressao_nota': _("Nome para impressão da nota"),
            'inscricao_estadual': _("Inscrição Estadual"),
            'endereco': _("Endereço"),
            'bairro': _("Bairro"),
            'municipio': _("Município (sem acentuação)"),
            'cmun': _("Código do município"),
            'cep': _("CEP (Apenas dígitos)"),
            'uf': _("UF"),
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_impressao_nota': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'cmun': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
        }


class ResponsavelForm(forms.ModelForm):

    class Meta:
        model = Responsavel
        fields = ('nome','cpf','rg')

        labels = {
            'nome': _("Nome"),
            'cpf': _("CPF"),
            'rg': _("RG"),
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TelefoneForm(forms.ModelForm):

    class Meta:
        model = Telefone
        fields = ('tipo_telefone', 'telefone',)
        labels = {
            'tipo_telefone': _("Telefone"),
            'telefone': _(''),
        }
        widgets = {
            'tipo_telefone': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('email',)
        labels = {
            'email': _('Email')
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ('site',)
        labels = {
            'site': _('Site'),
        }
        widgets = {
            'site': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BancoForm(forms.ModelForm):

    class Meta:
        model = Banco
        fields = ('banco', 'agencia', 'conta', 'digito',)
        labels = {
            'banco': _('Banco'),
            'agencia': _('Agência'),
            'conta': _('Conta'),
            'digito': _('Dígito'),
        }
        widgets = {
            'banco': forms.Select(attrs={'class': 'form-control'}),
            'agencia': forms.TextInput(attrs={'class': 'form-control'}),
            'conta': forms.TextInput(attrs={'class': 'form-control'}),
            'digito': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento
        fields = ('tipo', 'documento',)
        labels = {
            'tipo': _('Tipo'),
            'documento': _('Documento'),
        }
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
        }


EnderecoFormSet = inlineformset_factory(
    Pessoa, Endereco, form=EnderecoForm, extra=1, can_delete=True)
ResponsavelFormSet = inlineformset_factory(
    Pessoa, Responsavel, form=ResponsavelForm, extra=1, max_num=1, can_delete=True)
FazendaFormSet = inlineformset_factory(
    Pessoa, Fazenda, form=FazendaForm, extra=1, can_delete=True)
TelefoneFormSet = inlineformset_factory(
    Pessoa, Telefone, form=TelefoneForm, extra=1, can_delete=True)
EmailFormSet = inlineformset_factory(
    Pessoa, Email, form=EmailForm, extra=1, can_delete=True)
SiteFormSet = inlineformset_factory(
    Pessoa, Site, form=SiteForm, extra=1, can_delete=True)
BancoFormSet = inlineformset_factory(
    Pessoa, Banco, form=BancoForm, extra=1, can_delete=True)
DocumentoFormSet = inlineformset_factory(
    Pessoa, Documento, form=DocumentoForm, extra=1, can_delete=True)
