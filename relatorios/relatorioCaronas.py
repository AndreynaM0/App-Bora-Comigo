import caronas.caronas as modulocarona
import os 

relatorioCarona_txt = "C:\\Users\\Andreyna\\Desktop\\Faculdade P1\\python\\Projeto.AV3\\relatorios\\relatoriodasCarona.txt"
def relatorioDasCarona():
    if (len(modulocarona.verCaronasCadatradas()) >0):
        totalTodasCaronas = 0
        for carona in modulocarona.verCaronasCadatradas():
            totalCarona = carona["valVagas"] * len(carona["reservas"])
            print(f"\033[1;35;43m RELATÓRIO DAS SUAS CARONAS\033[m ")
            print("")
            print(
                f" Local de partida: {carona["localP"]}\n"
                f" Local de destino: {carona["destino"]}\n"
                f" Data da carona: {carona["data"]}\n"
                f" Horário de saída: {carona["hora"]}\n"
                f" Quantidade de vagas: {carona["qntVagas"]}\n"
                f" Valor da vaga: R${carona["valVagas"]}\n"
                f"Total à receber: R${totalCarona}")
            print("")
            totalTodasCaronas += totalCarona
        print(f"Total de todas as caronas: R${totalTodasCaronas}")
        return True
    else:
        print("\033[0;30;41mNão há caronas cadastradas!\033[m")
        return False

def salvarRelatorio():
    with open(relatorioCarona_txt, "w", encoding="utf8") as arquivo: #Adicionar no final
        totalTodasCaronas = 0
        for carona in modulocarona.verCaronasCadatradas():
            totalCarona = carona["valVagas"] * len(carona["reservas"])
            arquivo.write(f" RELATÓRIO DAS SUAS CARONAS ")
            arquivo.write("")
            arquivo.write(
                    f" Local de partida: {carona["localP"]}\n"
                    f" Local de destino: {carona["destino"]}\n"
                    f" Data da carona: {carona["data"]}\n"
                    f" Horário de saída: {carona["hora"]}\n"
                    f" Quantidade de vagas: {carona["qntVagas"]}\n"
                    f" Valor da vaga: R${carona["valVagas"]}\n"
                    f"Total à receber: R${totalCarona}\n")
            totalTodasCaronas += totalCarona
        arquivo.write("")
        arquivo.write(f"Total de todas as caronas: R${totalTodasCaronas}\n")
        arquivo.write("")
        print(f"\033[30;42mRelatório gerado com sucesso!\033[m\n"
              f"Segue o diretório:")
        print(relatorioCarona_txt)