from flask import Flask
from flask import render_template, url_for, request, redirect
from bdHelper import bdHelper

app = Flask(__name__)
sql = bdHelper()

@app.route('/')
def index():
	return render_template('index.html')

# Menus

@app.route('/cliente')
def cliente():
	return render_template('clientes.html')

@app.route('/funcionario')
def funcionario():
	return render_template('funcionarios.html')

@app.route('/restaurante')
def restaurante():
	return render_template('restaurante.html')

@app.route('/restaurante/cardapio/')
def cardapio():
	return render_template('cardapio.html')

@app.route('/restaurante/mesa/')
def mesa():
	return render_template('mesa.html')

@app.route('/pedido')
def pedido():
	return render_template('pedidos.html')

# fim Menus

# crud clientes

####### Cadastrar #######

@app.route('/cliente/cadastro')
def cadastro_cliente():
	return render_template('cadastro/cadastro_cliente.html')	

@app.route('/cadastro/cliente/submit', methods=['POST'])
def cliente_submit():
	nome = None
	tel = None
	cpf = None
	nome = request.form['nome_cliente']
	tel = request.form['tel_cliente']
	cpf = request.form['cpf_cliente']
	sql.cadastro_cliente(nome, tel, cpf)
	return redirect(url_for('cliente'))

########################
####### Exibir #########

@app.route('/cliente/search')
def search_cliente():
	return render_template('selecionar_cliente.html')

@app.route('/cliente/results')
def results_cliente_nome():
	nome = request.args.get('nome')
	results = sql.search_cliente(nome=nome)
	return render_template('listar_resultados_cliente.html', results=results)

@app.route('/cliente/results')
def results_cliente_algo():
	pass

@app.route('/cliente/<nome>')
def exibir_clientes(nome):
	id = request.args.get('id')
	results = sql.search_cliente(idCli=id)
	return render_template('exibir_cliente.html', results=results)

########################
####### Alterar ########

@app.route('/cliente/alterar/<id>/nome')
def cliente_nome(id):
	return render_template('alterar.html', name="Nome", action=url_for('cliente_nome_submit', id=id), type="text", label="Novo Nome")

@app.route('/cliente/alterar/<id>/nome/submit', methods=['POST'])
def cliente_nome_submit(id):
	novo = request.form['alt']
	sql.alter_cliente_nome(idCli=id, nome=novo)
	return redirect(url_for('cliente'))

@app.route('/cliente/alterar/<id>/telefone')
def cliente_tel(id):
	return render_template('alterar.html', name="Tel", action=url_for('cliente_tel_submit', id=id), type="tel", label="Novo Telefone")

@app.route('/cliente/alterar/<id>/telefonesubmit', methods=['POST'])
def cliente_tel_submit(id):
	novo = request.form['alt']
	sql.alter_cliente_tel(idCli=id, tel=novo)
	return redirect(url_for('cliente'))

@app.route('/cliente/alterar/<id>/cpf')
def cliente_cpf(id):
	return render_template('alterar.html', name="CPF", action=url_for('cliente_cpf_submit', id=id), type="text", label="Novo CPF")

@app.route('/cliente/alterar/<id>/cpfsubmit', methods=['POST'])
def cliente_cpf_submit(id):
	novo = request.form['alt']
	sql.alter_cliente_cpf(idCli=id, cpf=novo)
	return redirect(url_for('cliente'))

########################
######## Remover #######

@app.route('/cliente/<nome>/<idCli>/remove', methods=["POST"])
def rm_cliente(nome, idCli):
	sql.rm_cliente(idCli=idCli)
	return redirect(url_for('cliente'))

#crud pedidos

@app.route('/pedido/cadastro')
def cadastro_pedido():
	return render_template('cadastro/cadastro_pedido.html')

@app.route('/cadastro/pedido/submit', methods=['POST'])
def pedido_submit():
	nroMesa = None
	nroMesa = request.form['nroMesa']
	sql.cadastro_pedido(nroMesa)
	return redirect(url_for('pedido'))

@app.route('/pedido/search')
def search_pedido():
	return render_template('selecionar_pedido.html')

@app.route('/pedido/results')
def results_pedido_nome():
	return render_template('listar_resultados.html')

@app.route('/pedido/results')
def results_pedido_algo():
	pass



#crud funcionarios

@app.route('/funcionario/cadastro')
def cadastro_funcionario():
	return render_template('cadastrar_funcionarios.html')

@app.route('/funcionario/cadastro/cozinheiro')
def cadastro_cozinheiro():
	return render_template('cadastro/cadastro_cozinheiro.html')

@app.route('/funcionario/cadastro/garcom')
def cadastro_garcom():
	return render_template('cadastro/cadastro_garcom.html')

@app.route('/funcionario/cadastro/<funcao>/submit', methods=['POST'])
def funcionario_submit(funcao):
	nome_funcionario = None
	sal_funcionario = None
	cpf_funcionario = None
	nome_funcionario = request.form['nome_funcionario']
	sal_funcionario = request.form['sal_funcionario']
	cpf_funcionario = request.form['cpf_funcionario']

	if funcao == 'cozinheiro':
		cpf_chefe = None
		cpf_chefe = request.form['cpf_chefe']
		cadastro_cozinheiro(nome_funcionario, sal_funcionario, cpf_funcionario, cpf_chefe)
	else:
		bdHelper.cadastro_garcom(nome_funcionario, sal_funcionario, cpf_funcionario)
	return redirect(url_for('funcionario'))

@app.route('/funcionario/search')
def search_funcionario():
	return render_template('selecionar_funcionario.html')

@app.route('/funcionario/results')
def results_funcionario_nome():
	return render_template('listar_resultados.html')

@app.route('/funcionario/results')
def results_funcionario_algo():
	pass


# crud pratos	

####### Cadastrar #######

@app.route('/restaurante/cardapio/prato/cadastro')
def cadastro_prato():
	return render_template('cadastro/cadastro_prato.html')	

@app.route('/restaurante/cardapio/prato/cadastro/submit', methods=['POST'])
def prato_submit():
	nome = None
	nome = request.form['nome_prato']
	sql.cadastro_prato(nome)
	return redirect(url_for('cardapio'))

########################
####### Exibir #########

@app.route('/restaurante/prato/search')
def search_prato():
	return render_template('selecionar_prato.html')

@app.route('/prato/results')
def results_prato_nome():
	nome = request.args.get('nome_prato')
	results = sql.search_prato(nome=nome)
	return render_template('listar_resultados_prato.html', results=results)

@app.route('/prato/results')
def results_prato_algo():
	pass

@app.route('/prato/<nome>')
def exibir_prato(nome):
	id = request.args.get('id')
	results = sql.search_prato(id=id)
	return render_template('exibir_prato.html', results=results)

########################
####### Alterar ########

@app.route('/prato/alterar/<id>/')
def prato_nome(id):
	return render_template('alterar.html', name="Nome", action=url_for('prato_nome_submit', id=id), type="text", label="Novo Nome")

@app.route('/prato/alterar/<id>/submit', methods=['POST'])
def prato_nome_submit(id):
	novo = request.form['alt']
	sql.alter_prato_nome(id=id, nome=novo)
	return redirect(url_for('cardapio'))

########################
######## Remover #######

@app.route('/prato/<nome>/<id>/remove', methods=["POST"])
def rm_prato(nome, id):
	sql.rm_prato(id=id)
	return redirect(url_for('cardapio'))

# crud mesa

####### Cadastrar #######

@app.route('/mesa/cadastro')
def cadastro_mesa():
	return render_template('cadastro/cadastro_mesa.html')	

@app.route('/cadastro/mesa/submit', methods=['POST'])
def mesa_submit():
	numero_da_mesa = None
	numero_de_pessoas = None
	numero_da_mesa = request.form['numero_da_mesa']
	numero_de_pessoas = request.form['numero_de_pessoas']
	sql.cadastro_cliente(numero_da_mesa, numero_de_pessoas)
	return redirect(url_for('mesa'))

########################
####### Exibir #########

@app.route('/mesa/search')
def search_mesa():
	return render_template('selecionar_mesa.html')

@app.route('/mesa/results')
def results_mesa_numero_da_mesa():
	nome = request.args.get('numero_da_mesa')
	results = sql.search_mesa(numero_da_mesa=numero_da_mesa)
	return render_template('listar_resultados_mesa.html', results=results)

@app.route('/mesa/results')
def results_mesa_algo():
	pass

@app.route('/mesa/<numero_da_mesa>')
def exibir_mesa(numero_da_mesa):
	numero_de_pessoas = request.args.get('numero_de_pessoas')
	results = sql.search_cliente(numero_de_pessoas=numero_de_pessoas)
	return render_template('exibir_mesa.html', results=results)

########################
####### Alterar ########

@app.route('/mesa/alterar/<id>/')
def numero_da_mesa(numero_da_mesa):
	return render_template('alterar.html', name="Numero da mesa", action=url_for('numero_da_mesa_submit', id=id), type="num", label="Novo Numero da Mesa")

@app.route('/mesa/alterar/<id>/submit', methods=['POST'])
def numero_da_mesa_submit(numero_da_mesa):
	novo = request.form['alt']
	sql.alter_numero_da_mesa(numero_da_mesa=numero_da_mesa, numero_novo=novo)
	return redirect(url_for('mesa'))

@app.route('/mesa/alterar/<id>/')
def numero_de_pessoas(numero_da_mesa):
	return render_template('alterar.html', name="Numero de Pessoas", action=url_for('numero_de_pessoas_submit', id=id), type="num", label="Novo Numero de Pessoas")

@app.route('/mesa/alterar/<id>/submit', methods=['POST'])
def numero_de_pessoas_submit(numero_da_mesa):
	novo = request.form['alt']
	sql.alter_numero_de_pessoas(numero_da_mesa=numero_da_mesa, numero_de_pessoas=novo)
	return redirect(url_for('mesa'))

########################
######## Remover #######

@app.route('/mesa/<nroMesa>/remove', methods=["POST"])
def rm_mesa(nroMesa):
	sql.rm_mesa(numero_da_mesa=numero_da_mesa)
	return redirect(url_for('mesa'))

#crud pedidos

# #@app.route('/pedido/cadastro')
# #def cadastro_pedido():
# 	#return render_template('cadastro/cadastro_pedido.html')

# @app.route('/cadastro/pedido/submit', methods=['POST'])
# def pedido_submit():
# 	nroMesa = None
# 	nroMesa = request.form['nroMesa']
# 	sql.cadastro_pedido(nroMesa)
# 	return redirect(url_for('pedido'))

# @app.route('/pedido/search')
# def search_pedido():
# 	return render_template('selecionar_pedido.html')

# @app.route('/pedido/results')
# def results_pedido_nome():
# 	return render_template('listar_resultados.html')

# @app.route('/pedido/results')
# def results_pedido_algo():
# 	pass


if __name__ == '__main__':
	app.run(debug=True)