# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from SGCS.apps.cadastro.forms import PacienteForm
from SGCS.apps.cadastro.models import Paciente

from .base import AdicionarPessoaView, PessoasListView, EditarPessoaView


class AdicionarPacienteView(AdicionarPessoaView):
    template_name = "cadastro/pessoa_add.html"
    success_url = reverse_lazy('cadastro:listapacientesview')
    success_message = "Paciente <b>%(nome_razao_social)s </b>adicionado com sucesso."
    permission_codename = 'add_paciente'

    def get_context_data(self, **kwargs):
        context = super(AdicionarPacienteView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR PACIENTE'
        context['return_url'] = reverse_lazy('cadastro:listapacientesview')
        context['tipo_pessoa'] = 'paciente'
        return context

    def get(self, request, *args, **kwargs):
        form = PacienteForm(prefix='paciente_form')
        return super(AdicionarPacienteView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        req_post = request.POST.copy()
        req_post['paciente_form-limite_de_credito'] = req_post['paciente_form-limite_de_credito'].replace(
            '.', '')
        request.POST = req_post
        form = PacienteForm(request.POST, request.FILES,
                           prefix='paciente_form', request=request)
        return super(AdicionarPacienteView, self).post(request, form, *args, **kwargs)


class PacientesListView(PessoasListView):
    template_name = 'cadastro/pessoa_list.html'
    model = Paciente
    context_object_name = 'all_pacientes'
    success_url = reverse_lazy('cadastro:listapacientesview')
    permission_codename = 'view_paciente'

    def get_context_data(self, **kwargs):
        context = super(PacientesListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'PACIENTES CADASTRADOS'
        context['add_url'] = reverse_lazy('cadastro:addpacienteview')
        context['tipo_pessoa'] = 'paciente'
        return context


class EditarPacienteView(EditarPessoaView):
    form_class = PacienteForm
    model = Paciente
    template_name = "cadastro/pessoa_edit.html"
    success_url = reverse_lazy('cadastro:listapacientesview')
    success_message = "Paciente <b>%(nome_razao_social)s </b>editado com sucesso."
    permission_codename = 'change_paciente'
    def get_context_data(self, **kwargs):
        context = super(EditarPacienteView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listapacientesview')
        context['tipo_pessoa'] = 'paciente'
        
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form_class.prefix = "paciente_form"
        form = self.get_form(form_class)

        return super(EditarPacienteView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        req_post = request.POST.copy()
        req_post['paciente_form-limite_de_credito'] = req_post['paciente_form-limite_de_credito'].replace('.', '')
        request.POST = req_post
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES,
                          prefix='paciente_form', instance=self.object, request=request)
        
        return super(EditarPacienteView, self).post(request, form, *args, **kwargs)
