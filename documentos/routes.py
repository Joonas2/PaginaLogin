from documentos import app, database, bcrypt
from flask import render_template, url_for, flash, redirect, request
from documentos.formularios import FormLogin, FormCriarConta
from documentos.models import Usuario
from flask_login import login_user, logout_user, current_user

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            flash('Login realizado com sucesso', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'E-mail ou senha incorretos. Por favor tente novamente.', 'alert-danger')
    return render_template("login.html", form_login=form_login)


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form_criar_conta = FormCriarConta()
    if form_criar_conta.validate_on_submit():
        senha_crypt = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        usuario = Usuario(nome_usuario=form_criar_conta.nome_usuario.data, email=form_criar_conta.email.data, senha=senha_crypt)
        database.session.add(usuario)
        database.session.commit()
        return redirect(url_for('login'))
    return render_template('cadastro.html', form_criar_conta=form_criar_conta)

@app.route("/sair")
def sair():
    logout_user()
    return redirect(url_for('home'))

@app.route("/perfil")
def perfil():
    return render_template('perfil.html')