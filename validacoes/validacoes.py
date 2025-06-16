import usuarios.usuarios as usu
caracterSenha = "@#$%&*_"

def validarStringVazia(valor):
    if (valor == ""):
        print(f"\033[0;30;41mPor favor, informe algo válido!\033[m")
        return False
    else:
        return True


def validacaoData(data):
    if (len(data) == 10):
        dia, mes, ano = data.split("/")
        dia, mes, ano = int(dia), int(mes), int(ano)
        if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano == 2025:
            return True
        else:
            print("\033[0;30;41mData Inválida. Por favor, digite novamente!\033[m")
            return False
   
    elif (validarStringVazia(data) == False):
        print(f"\033[0;30;41mPor favor, informe uma data!\033[m")
        return False
    
    else:
        print(f"\033[0;30;41mFormato inválido. Por favor, digite novamente!\033[m")
        return False


def validacaoHora(horario):
    if (len(horario) == 5):
        hora, min = horario.split(":")
        hora, min = int(hora), int(min)
        if hora >= 0 and hora <= 23 and min >= 0 and min <= 59:
            return True
        else:
            print('\033[0;30;41mHora inválida. Por favor, digite novamente!\033[m')
            return False
    
    elif (validarStringVazia(horario) == False):
        print(f"\033[0;30;41mPor favor, informe um horário válido!\033[m") #tirar
        return False
    
    else:
        print(f"\033[0;30;41mFormato inválido. Por favor, digite novamente!\033[m")
        return False
    

def validacaoEmail(email):
    if(validarStringVazia(email) == False):
        return False
    elif(email.split("@")[0] != "" and "@" in email and (email.endswith(".com") or email.endswith(".com.br"))):
        return True
    else:
        print("\033[0;30;41mDigite um e-mail válido, por favor!\033[m")
        return False


def validacaoSenha(senha):
    validacaoCaractere= False
    for caracetere in senha:
            if (caracetere in caracterSenha):
                validacaoCaractere = True
                break
    if (len(senha) < 8 or not validacaoCaractere):
        print("\033[0;30;41mSenha inválida!\033[m")
        print("A senha deve conter no minímo 8 caracteres, incluindo um especial (EX: @, #, $, %, &, *, _)!")
        return False
    else:
        return True 


def validarValorVaga(valVagas):
    if not valVagas.isdigit() or valVagas == "":
        print("\033[0;30;41mInforme algo válido!\033[m")
        return False
    elif (float(valVagas) <=0):
        print("\033[0;30;41mValor inválido!\033[m")
        return False
    else:
        return True
    
def validarQuantidadeVaga(qntVagas):
    if not qntVagas.isdigit() or qntVagas == "":
        print("\033[0;30;41mInforme algo válido!\033[m")
        return False
    elif (int(qntVagas) <=0):
        print("\033[0;30;41mQuantidade inválida!\033[m")
        return False
    else:
        return True