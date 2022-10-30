from flask import render_template

class Control:

    #Checa se o login do aluno é valido
    def valida_senha_aluno(self, identificador,senha):
        if: ##########econtrou no banco de dados
            return render_template("agendamento.html")
        else:
            return render_template("index.html", popup = "block", erro = "erroLOGIN")

    #Registra o aluno dentro do Banco de Dados
    def registrar_aluno(self, nome, cpf, telefone, email, dre, senha):
        if: ###### cpf ja dentro do banco de dados
            return render_template("regis_aluno.html", erro = "erroJALOGADO")
        else:
            ##################### adicionar no banco de dados
            return render_template("index.html", popup = "block")

    
    def inscricao_aluno_sessao(self, sessao):
        if #####aluno inscrito em alguma sessao:
            return render_template("agendamento.html", erro = "erroJAAGENDADO")
        else:
            ####increver aluno na secao
            return render_template("agendamento_completo.html")

    
    def valida_senha_operador(self, identificador,senha):
        if: ##########econtrou no banco de dados
            return render_template("atendimento.html")
        else:
            return render_template("login_op.html", erro = "erroLOGIN")

