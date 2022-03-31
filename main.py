from dados import dados
from tesouros import recompensa_do_tesouro

from validar_input import valida_input_numero_usuario
from validar_input import valida_input_usuario
from validar_input import valida_input_numero_menor_que_quatro

from calcula_pontos import calcula_pontos

from iniciar_jogadores import iniciar_jogadores

from nadar import nadar

from caca_ao_tesouro import caca_ao_tesouro

from loading import loadingfn

from avancar_ou_retroceder import avancar_ou_retroceder_fn

while True:
    acabar_com_o_jogo = False

    # Pontos de todos os jogadores
    pontos_totais = 0

    jogadores_que_pararam = []

    nivel_de_oxigenio = 25
    profundidade = 0

    # Inicia e termina um jogo
    esta_jogando = True

    rodada = 0
    
    print('\u001b[1m')
    print("")
    print("INICIANDO O JOGO:")
    print("")
    loadingfn()

    # Funcao que inicia o jogo, pergunta quantos jogadores tem, seus nomes e retorna as seguintes informacoes.
    status_dos_jogadores, lista_de_nomes, numero_de_jogadores = iniciar_jogadores()
    # [
    #   {
    #      'Marcelo': {'profundidade': 0, 'avancando': True, 'tesouros': []}, 
    #      'Thomaz': {'profundidade': 0, 'avancando': True, 'tesouros': []}, 
    #      'Arthur': {'profundidade': 0, 'avancando': True, 'tesouros': []}, 
    #      'Rafael': {'profundidade': 0, 'avancando': True, 'tesouros': []}
    #   }, 
    #   
    #   ['Marcelo', 'Thomaz', 'Arthur', 'Rafael'], 
    #   
    #   4
    # ]

    print("")
    loadingfn()
    

    print('''

    \f Neste jogo, o jogador é um mergulhador em busca de tesouros escondidos no fundo do mar. Porém, o tanque de oxigênio não é grande o suficiente para possibilitar um mergulho tranquilo. Com a fonte de oxigênio escassa, os mergulhadores precisam gerenciar bem o tempo debaixo da água. Quanto mais fundo o mergulhador for, maior é a chance de encontrar tesouros mais valiosos. Além disso, a quantidade de tesouros que o mergulhador carrega afeta sua mobilidade. O objetivo do jogo é conseguir trazer para o submarino o maior valor em tesouros.
    
    ''')

    loadingfn()
    print("")

    numero_do_jogador_que_esta_jogando = 0

    print(''' 
                      | \
                     '.|
     _-   _-    _-  _-||    _-    _-  _-   _-    _-    _-
       _-    _-   - __||___    _-       _-    _-    _-
    _-   _-    _-  |   _   |       _-   _-    _-
      _-    _-    /_) (_) (_\        _-    _-       _-
              _.-'           `-._      ________       _-
        _..--`                   `-..'       .'
    _.-'  o/o      BOA SOTE        o/o`-..__.'        ~  ~
 .-'      o|o   MERGULHADORES!    o|o      `.._.  // ~  ~
 `-._     o|o                     o|o        |||<|||~  ~
     `-.__o\o                     o|o       .'-'  \\ ~  ~
          `-.______________________\_...-``'.       ~  ~
                                    `._______`
LGB
    
    ''')

    print('\u001b[0m')

    # COMECA DE FATO O JOGO
    while esta_jogando:

        
        # Obtem as informaçōes do jogador que está jogando na rodada atual
        nome_do_jogador_atual = lista_de_nomes[numero_do_jogador_que_esta_jogando]
        tesouros_jogador_atual = status_dos_jogadores[nome_do_jogador_atual]["tesouros"]
        profundidade_jogador_atual = status_dos_jogadores[nome_do_jogador_atual]["profundidade"]
        avancando_jogador_atual = status_dos_jogadores[nome_do_jogador_atual]["avancando"]

        # Reduzir oxigênio
        nivel_de_oxigenio -= len( tesouros_jogador_atual )


        # ---- Parar ou continuar o jogo -----
        # Caso o oxigenio acabe, o jogo acaba
        if nivel_de_oxigenio <= 0:
            print('\u001b[31m' '\u001b[1m' )
            print("Você perdeu o jogo! O nível de oxigênio chegou a 0!")
            print('\u001b[0m')
            esta_jogando = False

            print("" '\033[93m')
            jogar_novamente = valida_input_usuario( "Você deseja jogar novamente? Digite sim (s) ou não (n)", "s", "n" )
            print("" '\033[0m')
            
            if jogar_novamente == "s":
                break

            else:
                acabar_com_o_jogo = True
                print("Obrigado por jogar! ")
                break


        # Caso o jogador esteja retrocedendo e chegou com sucesso a superficie esse if é executado
        if not avancando_jogador_atual and 0 >= profundidade_jogador_atual:

            
            jogadores_que_pararam.append(nome_do_jogador_atual)
            pontos_do_jogador = calcula_pontos(tesouros_jogador_atual)
            pontos_totais += pontos_do_jogador

            # Muda o jogador atual 
            if len(lista_de_nomes) == 1:
                nome_do_jogador_atual = lista_de_nomes[0]
                del lista_de_nomes[numero_do_jogador_que_esta_jogando]
            else:
                del lista_de_nomes[numero_do_jogador_que_esta_jogando]
                nome_do_jogador_atual = lista_de_nomes[0]

            numero_do_jogador_que_esta_jogando = 0

            numero_de_jogadores -= 1

            print("Você terminou o jogo!")
            print(''' 
                                _
                        | \
                        '.|
        _-   _-    _-  _-||    _-    _-  _-   _-    _-    _-
        _-    _-   - __||___    _-       _-    _-    _-
        _-   _-    _-  |   _   |       _-   _-    _-
        _-    _-    /_) (_) (_\        _-    _-       _-
                _.-'           `-._      ________       _-
            _..--`                   `-..'       .'
        _.-'  o/o       SEJA           o/o`-..__.'        ~  ~
    .-'      o|o     BEM - VINDO       o|o      `.._.  // ~  ~
    `-._     o|o     NOVAMENTE!           o|o        |||<|||~  ~
        `-.__o\o                     o|o       .'-'  \\ ~  ~
            `-.______________________\_...-``'.       ~  ~
                                        `._______`.
            
            
            ''')
            
            print(f"Você conseguiu os seguintes tesouros: { tesouros_jogador_atual }")
            print(f"Sua pontuação final é: {pontos_do_jogador}")
            
            
        if len(jogadores_que_pararam) == len(status_dos_jogadores):

            print("  ")
            print("o|o o|o o|o o|o o|o o|o o|o o|o o|o o|o o|o ")
            print("  ")
            print(f"A pontuaçao total foi {pontos_totais} ")
            print("  ")
            print("o|o o|o o|o o|o o|o o|o o|o o|o o|o o|o o|o ")
            print("  ")


            esta_jogando = False

        # Coso o jogador deseje jogar novamente, quebra o loop do jogo e volta para o primeiro loop
        if not esta_jogando:

            print("" '\033[93m')
            jogar_novamente = valida_input_usuario( "Você deseja jogar novamente? Digite sim (s) ou não (n)", "s", "n" )
            print("" '\033[0m')
            
            if jogar_novamente == "s":
                break

            else:
                acabar_com_o_jogo = True
                print("Obrigado por jogar! ")
                break
        
    
        # Atualiza as informacoes do jogador atual para o código em seguida executar corretamente

        nome_do_jogador_atual = lista_de_nomes[numero_do_jogador_que_esta_jogando]
        tesouros_jogador_atual = status_dos_jogadores[nome_do_jogador_atual]["tesouros"]
        profundidade_jogador_atual = status_dos_jogadores[nome_do_jogador_atual]["profundidade"]
        avancando_jogador_atual = status_dos_jogadores[nome_do_jogador_atual]["avancando"]


        # -------- Introduz o jogo----------
        print(" " '\033[92m' '\u001b[1m')
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(" ")
        print(f"Agora é a vez do jogador: { nome_do_jogador_atual }!")
        print(" ")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_" '\033[0m')
        print(" ")

        # ------------- Respirar -------------
        input( '\033[94m' "Pressione ENTER para respirar! " '\033[0m')
        
        # Informa o jogador a respeito das informaçōes da rodada
        print(" ")
        print( '\033[7m' '\033[1m' f" #############  Rodada atual: {rodada} ##################### ")
        print("")
        print(f" Seu nível atual de oxigênio é: {nivel_de_oxigenio}. ")
        print(f" Você tem os seguintes tesouros {tesouros_jogador_atual}. ")
        print(f" Sua profundidade atual é {profundidade_jogador_atual} ")
        print("")
        print(" #################################################### " '\033[0m')
        
        print(" ")


        # -------- Avançar ou retroceder --------

        avancar_ou_retroceder_fn(status_dos_jogadores, tesouros_jogador_atual, nome_do_jogador_atual)


        # ---------------- Nadar ----------------
        # Descobre quantas posiçōes o jogador vai se movimentar

        dado1 = dados()
        dado2 = dados()

        lancamento_de_dados = dado1 + dado2
        nado = lancamento_de_dados - len(tesouros_jogador_atual)
        
        # Checar casos onde a profundidade vai ficar negativa
        mover_x_niveis = nado if nado > 0 else 0 
        
        print( '\u001b[47;1m' '\033[1m' '\u001b[30;1m' f" Dois dados de 1 a 3 foram lançados! O primeiro resultado foi {dado1} e o segundo {dado2}. A soma de suas pontuações é {lancamento_de_dados}! Você tem {len(tesouros_jogador_atual)} tesouros. Subtraindo a pontuação dos dados da quantidade de tesouros você obteve {mover_x_niveis} !" '\033[0m')

        print("")



        nova_profundidade = nadar(status_dos_jogadores, nome_do_jogador_atual, mover_x_niveis)

        if nova_profundidade <= 0:
            continue


        # ----------- Caça ao tesouro -----------
        print("")
        print('\033[93m')
        procurar_ou_soltar = valida_input_usuario( "Deseja procurar (p) mais tesouros ou soltar um (s)? ", "p", "s" )
        print('\033[0m')

        caca_ao_tesouro(procurar_ou_soltar, tesouros_jogador_atual, status_dos_jogadores, nova_profundidade, nome_do_jogador_atual )

        
        rodada += 1


        # Muda o jogador que esta jogando no momento
        if numero_de_jogadores - 1 == numero_do_jogador_que_esta_jogando:
            numero_do_jogador_que_esta_jogando = 0
        else:
            numero_do_jogador_que_esta_jogando += 1

    # Caso o jogo tenha terminado, quebra o loop
    print('\033[0m')
    if acabar_com_o_jogo:
        break

print("Art by Shanaka Dias")
print("Loading Bar: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html")