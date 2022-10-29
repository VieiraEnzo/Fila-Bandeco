class Control:

    #Checa se o login do aluno é valido
    def valida_senha_aluno(self, identificador,senha):
        if: ##########econtrou no banco de dados
            return render_template("aluno_main.html")
        else:
            return render_template("index.html", popup = "block", erro = "erroLOGIN")

    #Registra o aluno dentro do Banco de Dados
    def registrar_aluno(self, nome, cpf, telefone, email, dre, senha):
        if: ###### cpf ja dentro do banco de dados
            return render_template("regis_aluno.html", erro = "erroJALOGADO")
        else:
            ##################### adicionar no banco de dados
            return render_template("index.html", popup = "block")