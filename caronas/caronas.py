import usuarios.usuarios as moduloUsuario
import requisito_spotfy.spotfy as spotyfy
from time import sleep
import validacoes.validacoes as validacoes



def cadastroDeCarona(localP, destino, data, horario, qntVagas, valVagas):
    carona= {}
    motoristaCadastrado = moduloUsuario.usuarioLogado["nome"]
  
    carona ["localP"] = localP
    if (validacoes.validarStringVazia(localP) == False):
        print(f"\033[0;30;41mInforme algo válido!\033[m")
        return False
    
    carona ["destino"] = destino
    if (validacoes.validarStringVazia(destino) == False):
            print(f"\033[0;30;41mInforme algo válido!\033[m")
            return False
    
    carona ["data"] = data
    if(validacoes.validacaoData(data) == False):
        return False

    carona["hora"] = horario
    if(validacoes.validacaoHora(horario) == False):
        return False
    
    carona["qntVagas"] = int(qntVagas)
    if (validacoes.validarStringVazia(qntVagas) == False or validacoes.validarQuantidadeVaga(qntVagas) == False):
        print(f"\033[0;30;41mInforme algo válido!\033[m")
        return False
    
    carona["valVagas"] = float(valVagas)
    if (validacoes.validarStringVazia(valVagas) == False or validacoes.validarValorVaga(valVagas) == False):
        print(f"\033[0;30;41mInforme algo válido!\033[m")
        return False
    
    carona["motorista"] = motoristaCadastrado
    carona["reservas"] = [] 
    carona["passageiros"] = [] 
   
    opPlaylist= str(input("\033[1;35;43mDeseja criar uma playlist no Spotfy para essa viagem?\n"
                            "OBS: A PLAYLIST SERÁ CRIADA DE MODO ALEATÓRIO COM 4 MÚSICAS\n" 
                            "CORRESPONDENTES AO ARTISTA (ÚNICO) SUGERIDOS PELO PASSAGEIRO!\n"
                            "CRIAR PLAYLIST [S/N]:\033[m ")).upper()     
    if(opPlaylist == "S"):               
        playlist = spotyfy.criarPlaylist()

        carona["playlist"]= {
            "id": playlist["id"], 
            "link": playlist["external_urls"]["spotify"]
        } 

    carona["opPlaylist"] = opPlaylist

    moduloUsuario.usuarioLogado["caronas"].append(carona)
    print(f"\033[30;42mCarona Cadastrada com Sucesso!\033[m ")
    print("")
    return True

def listadeCaronas():
    listaCaronas= []
    for usu in  moduloUsuario.usuariosCadastrados:
        for carona in usu["caronas"]:
            carona["email"] = usu["email"]
            listaCaronas.append(carona)
    return listaCaronas
    
def listaDeCaronasDisponiveis():
    listaDisponiveis= []
    for carona in listadeCaronas():
        if (carona["qntVagas"] > 0):
            listaDisponiveis.append(carona)
    return listaDisponiveis

def buscarPorOrigemEDestino(locPartida, locDestino):
    compativelOrigemDestino= []
    for carona in listadeCaronas():
        if (carona["localP"] == locPartida and carona["destino"] == locDestino):
            compativelOrigemDestino.append(carona)
    return compativelOrigemDestino

def reservarVaganaCarona(emailMotorista, data):
    if(validacoes.validacaoData(data) == False or validacoes.validarStringVazia(emailMotorista) == False ):
        return False
    for usu in  moduloUsuario.usuariosCadastrados:
        for carona in usu["caronas"]:
            if (emailMotorista == usu["email"] and data == carona["data"]):
                if(emailMotorista ==  moduloUsuario.usuarioLogado["email"]):
                    print("\033[0;30;41mVocê é motorista. Não pode resevar uma vaga na sua própia carona!\033[m")
                elif (carona["qntVagas"]):
                    if(carona["opPlaylist"] == 'S'): #Só se o motorista optar por "S" Para criar playlist
                            print("Sabe aquele Cantor(a) ou aquela banda, ou grupo musical que você AMA ouvir?")
                            print("Nos indique o seu artista favorito para ouvirmos algumas músicas dele durante a viagem :)")
                            artistasfile= input("Nome do cantor ou banda: ")
                            spotyfy.addMusicaNaPlaylist(artistasfile, carona)

                    print("\033[30;42mVaga reservada com sucesso!\033[m")
                    print("")
                    sleep(1.0)
                    carona["qntVagas"] -= 1
                    emailReserva =  moduloUsuario.usuarioLogado ["email"] 
                    nomeReserva =  moduloUsuario.usuarioLogado["nome"]
                    carona["reservas"].append(emailReserva)
                    carona["passageiros"].append(nomeReserva)
                    return True
                
                else:
                    print(f"\033[0;30;41mNão possuí vagas na carona informada!\033[m")
                    return False


def cancelarReservaCarona(emailMotorista, data):
    if(validacoes.validacaoData(data) == False or validacoes.validarStringVazia(emailMotorista) == False ):
        return False
    for usu in  moduloUsuario.usuariosCadastrados:
        for carona in usu["caronas"]: 
            if (emailMotorista == usu["email"] and data == carona["data"]):
                    emailReserva =  moduloUsuario.usuarioLogado["email"]
                    nomeReserva =  moduloUsuario.usuarioLogado["nome"]
                    if(emailReserva in carona["reservas"]):
                        carona["reservas"].remove(emailReserva)
                        carona["qntVagas"] += 1
                
                        if(nomeReserva in carona["passageiros"] ):
                            carona["passageiros"].remove((nomeReserva))
                        print(f"\033[30;42mReserva cancelada!\033[m") 
                        return True
    return False

def cancelarCarona(data):
    if(validacoes.validacaoData(data) == False):
        return False
    emailUsuarioLogado =  moduloUsuario.usuarioLogado ["email"]
    for usu in  moduloUsuario.usuariosCadastrados:
        for carona in usu["caronas"]:
            if (data == carona["data"] and emailUsuarioLogado == usu["email"]): 
                usu["caronas"].remove(carona)
                print(f"\033[30;42mA carona foi removida!\033[m")
                return True
    return False

def detalhesDaCarona(emailMotorista, data):
    if(validacoes.validacaoData(data) == False or validacoes.validarStringVazia(emailMotorista) == False ):
        return None
    for usu in  moduloUsuario.usuariosCadastrados:
        for carona in usu["caronas"]:
            if (emailMotorista == usu["email"] and data == carona["data"]):
                return carona
    return None

def verCaronasCadatradas():
    return  moduloUsuario.usuarioLogado["caronas"]

