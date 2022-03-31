from tesouros import recompensa_do_tesouro
from validar_input import valida_input_usuario
from validar_input import valida_input_numero_usuario
from validar_input import valida_input_numero_menor_que_quatro

def caca_ao_tesouro(procurar_ou_soltar, tesouros_jogador_atual, status_dos_jogadores, nova_profundidade,nome_do_jogador_atual ):
    if procurar_ou_soltar == "p":

            #calcula o valor dad recombensa baseado em sua profundidade
            valor_da_recompensa = recompensa_do_tesouro(nova_profundidade)
            
            print(" ")
            print('\033[92m' f" ~~~~ O valor da recompensa encontrada é {valor_da_recompensa} ~~~~" '\033[0m')
            print(" ")

            print(f"Você tem os seguintes tesouros: {tesouros_jogador_atual}")

            print('\033[93m')
            deseja_ficar_com_o_tesouro = valida_input_usuario( "Você deseja ficar com o tesouro encontrado? Digite sim (s) ou não (n)!", "s", "n" )
            print('\033[0m')

            if deseja_ficar_com_o_tesouro == "s" and len(tesouros_jogador_atual) < 4:
                status_dos_jogadores[nome_do_jogador_atual]["tesouros"].append(valor_da_recompensa)

            elif deseja_ficar_com_o_tesouro == "s" and len(tesouros_jogador_atual) == 4:

                #Consertar essa funcao aqui dps! o ususrio pode colocar numeros fora do range da lista
                indice_tesouro_a_ser_removido = valida_input_numero_usuario('\033[93m' "Para pegar esse tesouro, você terá que deixar um deles de lado... Digite o índice daquele que você deseja trocar.", "0","1","2","3" '\033[0m')
                status_dos_jogadores[nome_do_jogador_atual]["tesouros"][indice_tesouro_a_ser_removido] = valor_da_recompensa
            
    elif procurar_ou_soltar == "s" and len(tesouros_jogador_atual) > 0:

        print(f"Você tem os seguintes tesouros: {tesouros_jogador_atual}")

        indice_tesouro_a_ser_removido = valida_input_numero_menor_que_quatro('\033[93m' "Para deixar um tesouro de lado, digite o índice do que você deseja trocar. ", len(tesouros_jogador_atual))
        del status_dos_jogadores[nome_do_jogador_atual]["tesouros"][indice_tesouro_a_ser_removido]
    else:
        print("Você não pode soltar nenhum tesouro uma vez que você não tem nenhum!")
