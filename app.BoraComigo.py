from time import sleep
import os 

import usuarios.usuarios as moduloUsuarios #importando tudo dando um apelido ao modulo
import caronas.caronas as moduloCaronas 
import validacoes.validacoes as validacoes 
import requisito_spotfy.spotfy as spotfy
import relatorios.relatorioCaronas as moduloRelatorios

usuarioLogado = moduloUsuarios.retornaUsuarioLogado()

spotfy.connectSpotfy()
moduloUsuarios.ler_usuarios()

largura = 60
print("=-" * 30)
sleep(0.5)
print("\033[1;35;43mBem Vindo\033[m ".center(largura))
sleep(1.0)
print("\033[1;35;43mBORA\033[m".center(largura))
sleep(0.5)
print("\033[1;35;43mCOMIGO?\033[m".center(largura))
print("")
print("=-" * 30)

while True:
    menuPrincipal = input("\033[1;35;43mEscolha uma das opções:\033[m \n\n" \
    "0 - Sair\n" \
    "1 - Cadastrar usuário\n" \
    "2 - Login\n\n"
    "Opção: ")
    os.system("cls" if os.name == "nt" else "clear")
    
    if(menuPrincipal == "0"):
        break
    
    if(menuPrincipal == "1"):
        while (True):
            nome = input("Digite o seu nome: ")
            while True:
                if(validacoes.validarStringVazia(nome) == False):
                    nome = input("Digite o seu nome: ")
                else:
                    break

            email = input("Digite o seu E-mail: ")
            while True:
                if(validacoes.validacaoEmail (email) == False):
                    email = input("Digite o seu E-mail: ")
                else:
                    break

            senha = input("Crie o sua senha: ") 
            while True:
                if(validacoes.validacaoSenha(senha) == False):
                    senha = input("Crie o sua senha: ") 
                else:
                    break
            if(moduloUsuarios.cadastroUsuarios(nome, email, senha)):
                break
           
    elif(menuPrincipal == "2"):
        email= input("Digite o seu E-mail: ")
        senha = input("Digite sua senha: ") 
           
        if(moduloUsuarios.loginUsuario(email, senha) == True):
            while True:
                print("")
                opcoesULogado= input("\033[1;35;43mEscolha uma das opções:\033[m \n\n" \
                "0 - Logout\n" \
                "1 - Cadastrar Carona\n" 
                "2 - Ver lista de Caronas Disponíveis\n" 
                "3 - Buscar Carona por Origem e Destino\n"
                "4 - Reservar vaga em uma Carona\n" 
                "5 - Cancelar reserva da carona\n" 
                "6 - Remover a carona\n" 
                "7 - Ver detalher da carona\n" 
                "8 - Ver caronas cadastradas\n"
                "9 - Relatório de Caronas Cadastradas\n" 
                "Opção: ")
                os.system("cls" if os.name == "nt" else "clear")
                
                if(opcoesULogado == "1"):
                    while True:
                        motoristaCadastrado = moduloUsuarios.usuarioLogado["nome"]
                        print(f"Motorista {motoristaCadastrado}. ")
                        print(f"Por favor, preencha as infomações para cadastrar sua carona: \n")
                        sleep(0.5)

                        localP = input("Informe o seu ponto de partida: ")
                        while True:
                            if(validacoes.validarStringVazia(localP) == False):
                                localP = input("Informe o seu ponto de partida: ")
                            else:
                                break
                        destino = input("Informe o local de destino: ")
                        while True:
                            if(validacoes.validarStringVazia(destino) == False):
                                destino = input("Informe o local de destino: ")
                            else:
                                break

                        data = input("Informe a data em que será feito a corrida: ")
                        while True:
                            if(validacoes.validacaoData(data) == False):
                                data = input("Informe a data em que será feito a corrida: ")
                            else:
                                break
                            
                        hora = input("Informe o horário de saída no formato HH:MM : ")
                        while True:
                            if(validacoes.validacaoHora(hora) == False):
                                hora = input("Informe o horário de saída no formato HH:MM : ")
                            else:
                                break
                        

                        qntVagas = input("Informe a quantidade de vagas disponíveis: ")
                        while True:
                            if(validacoes.validarQuantidadeVaga(qntVagas) == False):
                                qntVagas = input("Informe a quantidade de vagas disponíveis: ")
                            else:
                                break

                        valVagas =  input("Informe o valor da vaga: R$ ") 
                        while True:
                            if(validacoes.validarValorVaga(valVagas) == False):
                                valVagas =  input("Informe o valor da vaga: R$ ")
                            else:
                                break

                        motorista = motoristaCadastrado
                        reservas = [] 
                        passageiros = [] 
                        if (moduloCaronas.cadastroDeCarona(localP, destino, data, hora, qntVagas, valVagas) == True):
                            break
                    

                elif(opcoesULogado == "2"):
                    for carona in moduloCaronas.listaDeCaronasDisponiveis():
                        print("-="*30)
                        print("\033[1;35;43mLista de Caronas Disponíveis:\033[m".center(largura))
                        print("-="*30)
                        sleep(0.5)
                        print(f" Nome do motorista: {carona["motorista"]},\n"
                            f" E-mail do motorista: {carona["email"]},\n"
                            f" Local de partida: {carona["localP"]}\n"
                            f" Local de destino: {carona["destino"]}\n"
                            f" Data da carona: {carona["data"]}\n"
                            f" Horário de saída: {carona["hora"]}\n"
                            f" Quantidade de vagas: {carona["qntVagas"]}\n"
                            f" Valor da vaga: R${carona["valVagas"]}\n")
                        print("")
                
                elif(opcoesULogado == "3"):
                    locPartida = input("Digite o seu local de partida: ")
                    while True:
                            if(validacoes.validarStringVazia(destino) == False):
                                locPartida = input("Digite o seu local de partida: ")
                            else:
                                break

                    locDestino = input("Digite o seu local de destino: ")
                    while True:
                            if(validacoes.validarStringVazia(destino) == False):
                                locDestino = input("Digite o seu local de destino: ")
                            else:
                                break

                    for carona in moduloCaronas.buscarPorOrigemEDestino(locPartida, locDestino):
                        if (carona["localP"] == locPartida and carona["destino"] == locDestino):
                            print("")
                            print(f" Nome do motorista: {carona["motorista"]}\n"
                                    f" Local de partida: {carona["localP"]}\n"
                                    f" E-mail do motorista: {carona["email"]}\n"
                                    f" Local de destino: {carona["destino"]}\n"
                                    f" Data da carona: {carona["data"]}\n"
                                    f" Horário de saída: {carona["hora"]}\n"
                                    f" Quantidade de vagas: {carona["qntVagas"]}\n"
                                    f" Valor da vaga: R${carona["valVagas"]}\n")
                            print("")
                
                elif(opcoesULogado == "4"):
                    emailMotorista= input("Digite o e-mail do motorista: ")
                    while True:
                        if(validacoes.validarStringVazia(emailMotorista) == False):
                            emailMotorista= input("Digite o e-mail do motorista: ")
                        else:
                            break 

                    datacarona= input("Digite a data da carona (dd/mm/aa): ")
                    while True:
                        if(validacoes.validacaoData(data) == False):
                            data = input("Informe a data em que será feito a corrida: ")
                        else:
                            break 
                    moduloCaronas.reservarVaganaCarona(emailMotorista, datacarona)

                elif(opcoesULogado == "5"):
                    emailMotorista= input("Digite o e-mail do motorista: ")
                    while True:
                        if(validacoes.validarStringVazia(emailMotorista) == False):
                            emailMotorista= input("Digite o e-mail do motorista: ")
                        else:
                            break 

                    datacarona= input("Digite a data da carona (dd/mm/aa): ")
                    while True:
                        if(validacoes.validacaoData(data) == False):
                            data = input("Informe a data em que será feito a corrida: ")
                        else:
                            break 
                    moduloCaronas.cancelarReservaCarona(emailMotorista, datacarona)
               
                elif(opcoesULogado == "6"):
                        datacarona= input("Digite a data da carona (dd/mm/aa): ") 
                        while True:
                            if(validacoes.validacaoData(data) == False):
                                data = input("Informe a data em que será feito a corrida: ")
                            else:
                                break 
                        moduloCaronas.cancelarCarona(datacarona)

                elif(opcoesULogado == "7"):
                    emailMotorista= input("Digite o e-mail do motorista: ")
                    while True:
                        if(validacoes.validarStringVazia(emailMotorista) == False):
                            emailMotorista= input("Digite o e-mail do motorista: ")
                        else:
                            break 

                    datacarona= input("Digite a data da carona (dd/mm/aa): ")
                    while True:
                        if(validacoes.validacaoData(data) == False):
                            data = input("Informe a data em que será feito a corrida: ")
                        else:
                            break
                    carona = moduloCaronas.detalhesDaCarona(emailMotorista, datacarona)
                    if(carona == None):
                        print(f"\033[30;42mNenhuma carona foi encontrada!\033[m")
                    else:
                        print("-="*30)
                        print("\033[4;30;45mDetalhes das Caronas:\033[m".center(largura))
                        print("-="*30)
                        sleep(0.5)
                        print(f" Local de partida: {carona["localP"]}\n"
                                f" Local de destino: {carona["destino"]}\n"
                                f" Horário de saída: {carona["hora"]}\n"
                                f" Valor da vaga: R${carona["valVagas"]}\n"
                                f" Quantidade de vagas restantes: {carona["qntVagas"]}\n"
                                f" Quantidade de passageiros : {len(carona["reservas"])}\n" 
                                f" Nome dos passageiros : {carona["passageiros"]}\n" )
                        print("")
               
                elif(opcoesULogado == "8"):
                        if (len(moduloCaronas.verCaronasCadatradas()) > 0):
                            for carona in moduloCaronas.verCaronasCadatradas():
                                print("-="*30)
                                print("\033[1;35;43mSuas Caronas Cadastradas:\033[m".center(largura))
                                print("-="*30)
                                sleep(0.5)
                                print(f" Local de partida: {carona["localP"]}\n"
                                        f" Local de destino: {carona["destino"]}\n"
                                        f" Horário de saída: {carona["hora"]}\n"
                                        f" Valor da vaga: R${carona["valVagas"]}\n"
                                        f" Quantidade de vagas restantes: {carona["qntVagas"]}\n"
                                        f" Quantidade de passageiros : {len(carona["reservas"])}\n"
                                        f" Nome dos passageiros : {carona["passageiros"]}\n" )
                                print("")
                                if(carona["opPlaylist"] == 'S'): #Só se motorista quis criar playlist
                                    print(f"Link Da Playlist Criada Para Curtir Sua Viagem: {carona["playlist"]["link"]}")
                        else:
                            print("Você não possuí carona cadastrada!")

                elif(opcoesULogado == "9"):
                    if (moduloRelatorios.relatorioDasCarona()):
                        opRelatorio = input(f"Deseja gerar um documento com o relatório das suas caronas? (S/N): ").upper()
                        if(opRelatorio == "S"):
                            moduloRelatorios.salvarRelatorio()

                elif(opcoesULogado == "0"):
                    moduloUsuarios.logout()
                    print("")
                    print("\033[1;35;43mDESCONECTANDO...\033[m")
                    sleep(1.0)
                    print(f"\033[1;35;43mVolte sempre!\033[m")
                    print("")
                    break
