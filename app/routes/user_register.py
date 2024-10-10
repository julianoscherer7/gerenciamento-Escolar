# @auth.route('/register-student', methods=['GET', 'POST'])
# def register_student():
#     if request.method == 'POST':
#         nome = request.form['nome']
#         email = request.form['email']
#         senha = request.form['senha']
        
#         if Usuario.query.filter_by(Email=email).first():
#             flash('Email já cadastrado.', 'error')
#             return redirect(url_for('auth.register_student'))
        
#         novo_aluno = Usuario(Nome=nome, Cargo='Aluno', Email=email, Senha=generate_password_hash(senha))
#         db.session.add(novo_aluno)
#         db.session.commit()
        
#         flash('Cadastro realizado com sucesso!', 'success')
#         return redirect(url_for('auth.login'))
    
#     return render_template('register_student.html')