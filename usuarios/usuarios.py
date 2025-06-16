from validacoes.validacoes import validacaoEmail, validacaoSenha, validarStringVazia
import os
import json 

usuariosCadastrados = []
caracterSenha = "@#$%&*_"

usuarioLogado = {
    "nome" : "",
    "email" : "",
    "senha" : "",
    "caronas" : [],
}

arquivo_txt = "C:\\Users\\Andreyna\\Desktop\\Faculdade P1\\python\\Projeto.AV3\\manipular_Arquivo\\usuarios.txt"

def ler_usuarios():
    usuarios= []
    global usuariosCadastrados

    ignoraPrimeiraLinha = False
    with open(arquivo_txt, mode='r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if(ignoraPrimeiraLinha == False):
                ignoraPrimeiraLinha = True
                continue
            dados = linha.split(";")
            usuariosCadastrados.append({"nome" : dados[0], "email": dados[1], "senha": dados[2], "caronas": []})
        # return [json.loads(linha.strip()) for linha in arquivo if linha.strip()]
    

# def salvar_usuarios(usuarios):
#     with open(arquivo_txt, mode='w', encoding='utf-8') as arquivo:
#         for u in usuarios:
#             arquivo.write(json.dumps(u, ensure_ascii=False) + '\n')


def salvarUsuario(usuarios):
    with open(arquivo_txt, "w", encoding="utf8") as arquivo: #Adicionar no final
        arquivo.write(f"nome;email;senha\n")
        for usu in usuarios:
            arquivo.write(f"{usu['nome']};{usu['email']};{usu["senha"]};\n")

def cadastroUsuarios (nome, email, senha):
    usuario = {}
    usuario["nome"] = nome
    nomeValido= validarStringVazia(nome)
    if(nomeValido == False):
        return False

    usuario["email"] = email
    usuario["senha"] = senha
    senhaValida = validacaoSenha(senha)
    if (senhaValida == False):
        return False

    usuario["caronas"] = []
    
    
    emailValido = validacaoEmail(email)
    if (emailValido == False):
        return False
    
    for usu in usuariosCadastrados: 
        if(usu["email"] == usuario["email"]):
            print("\033[0;30;41mO E-mail informado já possuí cadastrado!\033[m") 
            print("Por favor, cadastre um novo E-mail: ") 
            return False
    
    

    usuariosCadastrados.append(usuario)
    print("")
    print(f"\033[30;42mUsuário cadastrado com sucesso!\033[m")
    print("")
    salvarUsuario(usuariosCadastrados)
    return True
    
    
def buscarusuario (email):
    for usu in usuariosCadastrados:
            if(usu["email"] == email):
                 return usu 
    return None

def loginUsuario (email, senha):
    usu = buscarusuario(email)
    global usuarioLogado #Dizendo ao código que estou utilizando uma variável global!
   
    if(usu == None):
        print(f"\033[30;41mNão foi esncontrado usuário com o e-mail informado!.\033[m")
        return False
   
    elif(usu["senha"] == senha):
        print("\033[30;42mLogin bem sucedido. Seja bem vindo(a)!\033[m")
        usuarioLogado = usu 
        return True
   
    else:
        print("\033[0;30;41mE-mail ou senha inválidos!\033[m")
        return False
    
def retornaUsuarioLogado():
    return usuarioLogado

def logout():
    global usuarioLogado #Puxa variável Global
    usuarioLogado = {}

    