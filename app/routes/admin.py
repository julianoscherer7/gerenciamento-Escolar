from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from models import *
from .auth import login_required, admin_required

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@admin_required
def admin_panel():
    usuario = Usuario.query.get(session['user_id'])
    return render_template('admin_panel.html', usuario=usuario)

@admin.route('/admin/gerenciar-usuarios')
@login_required
@admin_required
def gerenciar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('gerenciar_usuarios.html', usuarios=usuarios)

@admin.route('/admin/gerenciar-predios-salas')
@login_required
@admin_required
def gerenciar_predios_salas():
    predios = Predio.query.all()
    salas = Sala.query.all()
    return render_template('gerenciar_predios_salas.html', predios=predios, salas=salas)

@admin.route('/admin/gerenciar-turmas')
@login_required
@admin_required
def gerenciar_turmas():
    turmas = Turma.query.all()
    return render_template('gerenciar_turmas.html', turmas=turmas)

@admin.route('/admin/gerenciar-recursos')
@login_required
@admin_required
def gerenciar_recursos():
    recursos = Recurso.query.all()
    return render_template('gerenciar_recursos.html', recursos=recursos)

@admin.route('/admin/gerar-relatorios')
@login_required
@admin_required
def gerar_relatorios():
    return render_template('gerar_relatorios.html')

@admin.route('/admin/configuracoes-sistema')
@login_required
@admin_required
def configuracoes_sistema():
    return render_template('configuracoes_sistema.html')
