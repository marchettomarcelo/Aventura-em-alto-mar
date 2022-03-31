from validar_input import valida_input_usuario

def avancar_ou_retroceder_fn(status_dos_jogadores,  tesouros_jogador_atual, nome_do_jogador_atual ):

    if status_dos_jogadores[nome_do_jogador_atual]["avancando"]:
            # O jogador não pode retroceder caso nao tenha tesouros
            if len(tesouros_jogador_atual) == 0:
                print( '\033[7m' '\033[91m' "Você precisa avançar nesse momento! Você não tem nenhum tesouro... " '\033[0m')
                print("")
            else:
                avancar_ou_retroceder = valida_input_usuario( '\033[93m' "Você deseja avançar (a) ou retroceder (r)? ", "a", "r" )
                print('\033[0m')
                
                # Muda o status do jogador para não poder mais avancar
                if avancar_ou_retroceder == "r":
                    status_dos_jogadores[nome_do_jogador_atual]["avancando"] = False
                else:
                    print(" "'\u001b[34m')
                    print(" ~~~~~~~~~~ Bora nadar!!! ~~~~~~~~~~  ") 
                    print('''
                                    O
                                O
                                    o  \``/
                                     /o `))
    _________         .    .        /_/\_ss))
   (..       \_    ,  |\  /|            |_ss))/|
    \       O  \  /|  \ \/ /           |__ss))_|
     \______    \/ |   \  /           |__sss))_|
        vvvv\    \ |   /  |           |___ss))\|
        \^^^^  ==   \_/   |            |_ss))
        `\_   ===    \.  |            )_s))
        / /\_   \ /      |      (`(  /_s)) 
        |/   \_  \|      /       (_\/_s))
                \________/         (\/))               

                    ''')
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("" '\033[0m')