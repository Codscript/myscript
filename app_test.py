from flask import Flask, render_template, request, redirect, url_for, flash, redirect

import pyodbc

app = Flask(__name__)
wsgi_app = app.wsgi_app

def conexao():
	server = 'DESKTOP-NISJNM0\SQLEXPRESS' 
	database ='FAISP'

	cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
	cursor = cnxn.cursor()
	return cnxn.cursor()


@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/")
@app.route("/cadastrar")
def cadastrar():
	return render_template("cadastro.html")

def voltar():
	return render_template("home")
#cadastro em sql
@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
	
	if request.method == "POST":
		nome = (request.form.get("nome"))
		data_de_nacimento = (request.form.get("data_de_nacimento"))
		idade = (request.form.get("idade"))
		objetivo_da_graduacao = (request.form.get("objetivo_da_graduacao"))
		genero = (request.form.get("genero"))
		email = (request.form.get("email"))
    
	
	cursor = conexao()
	cursor.execute('INSERT into aln(nome, data_de_nacimento, idade, objetivo_da_graduacao, genero, email) values(?,?,?,?,?,?);',(nome, data_de_nacimento, idade, objetivo_da_graduacao, genero, email))
	cursor.commit()
	
	return redirect(url_for("home"))

@app.route("/lista",)
def lista():
	cursor = conexao()
	cursor.execute('select * from aln ORDER BY id_aln')
	aln = cursor.fetchall()
	
	
	return render_template("lista.html", aln=aln)

@app.route("/atualizar/<int:id>", methods=['GET'])
def atualizar(id):
	cursor = conexao()
	cursor.execute(f'select * from aln where id_aln = {id}')
	aln = cursor.fetchall()
	cursor.close()
	return render_template("atualizar.html", aln=aln)
@app.route("/atualiz/", methods = ['POST'])
def atualiz():
	if request.method == 'POST' :
		nome = (request.form.get("nome"))
		data_de_nacimento = (request.form.get("data_de_nacimento"))
		idade = (request.form.get("idade"))
		objetivo_da_graduacao = (request.form.get("objetivo_da_graduacao"))
		genero = (request.form.get("genero"))
		email = (request.form.get("email"))
		id_aln= (request.form.get("id_aln"))

	cursor = conexao()
	cursor.execute(f'Update aln set nome = {nome}, data_de_nacimento = {data_de_nacimento}, idade = {idade}, objetivo_da_graduacao = {objetivo_da_graduacao}, genero = {genero}, email = {email} where id_aln = {id_aln}')
	cursor.commit()
	
	 
	return "<h1> atualizaçaõ realiazada com sucesso!!!!<h1>"

	

@app.route("/excluir/<int:id>")
def excluir(id):
	cursor = conexao()
	cursor.execute(f'delete from aln where id_aln = {id}')
	cursor.commit()
	
	
	return redirect("http://127.0.0.1:5000/lista")
	

		

if __name__== '__main__':
    app.run(debug=True)