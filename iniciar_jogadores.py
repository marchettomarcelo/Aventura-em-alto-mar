

def iniciar_jogadores():

    status_dos_jogadores = {}
    lista_de_nomes = []

    print("")
    
    n_jogadores = input("\nQuantos Jogadores vão jogar? ")
    
    while True:
        try:
            n_jogadores =  int(n_jogadores)
            
            if n_jogadores <= 0:
                raise 
            
            break

        except:
            n_jogadores =  input("Insira o número de Jogadores que vão jogar? ")


    contador = 1
    while n_jogadores >= contador:

        nome_jogador = input(f"Insira o nome do jogador número {contador}: ")
        
        status_dos_jogadores[nome_jogador] = {"profundidade" : 0, "avancando": True, "tesouros":[]}

        lista_de_nomes.append(nome_jogador)

        contador += 1

    
    return [status_dos_jogadores, lista_de_nomes, len(lista_de_nomes)]
