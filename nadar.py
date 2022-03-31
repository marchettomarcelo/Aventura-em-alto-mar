
def nadar(status_dos_jogadores, nome_do_jogador_atual, mover_x_niveis):
    # Caso ele esteja avançando, irá somar a sua profundidade
    if status_dos_jogadores[nome_do_jogador_atual]["avancando"]:

        if status_dos_jogadores[nome_do_jogador_atual]["profundidade"] +  mover_x_niveis  > 32:

            status_dos_jogadores[nome_do_jogador_atual]["profundidade"] = 32

            mover_x_niveis = 0
            nova_profundidade = status_dos_jogadores[nome_do_jogador_atual]["profundidade"]
            print("A profunidade máxima é 32, por isso você não irá avançar mais nessa rodada!")

        else:
            status_dos_jogadores[nome_do_jogador_atual]["profundidade"] += mover_x_niveis
        
        # ~~~ Nova Pofundidade ~~~
            nova_profundidade = status_dos_jogadores[nome_do_jogador_atual]["profundidade"]
        # ~~~ Nova Pofundidade ~~~

            print(f"Você desceu {mover_x_niveis} agora! Sua profundidade é {nova_profundidade}" '\033[0m')
    
    # Caso ele esteja retrocedendo, irá subtrair de sua profundidade
    else:

        status_dos_jogadores[nome_do_jogador_atual]["profundidade"] -= mover_x_niveis
        # ~~~ Nova Pofundidade ~~~
        nova_profundidade = status_dos_jogadores[nome_do_jogador_atual]["profundidade"]
        # ~~~ Nova Pofundidade ~~~
    
    return nova_profundidade
