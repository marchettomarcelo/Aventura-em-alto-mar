
def valida_input_usuario(pergunta, respota1, respota2):

    input_do_usuario = input(pergunta)
    while True:

        if input_do_usuario == respota1 or input_do_usuario == respota2:
            return input_do_usuario
        else:
            input_do_usuario =  input(f"Escolha uma dessas duas respostas: {respota1} ou {respota2}!")

def valida_input_numero_usuario(pergunta, respota1, respota2, respota3, respota4):

    input_do_usuario = input(pergunta)
    while True:

        if input_do_usuario == respota1 or input_do_usuario == respota2 or input_do_usuario == respota3 or input_do_usuario == respota4:
            return int(input_do_usuario)
        else:
            input_do_usuario =  input(f"Escolha uma dessas quatro respostas: {respota1} ou {respota2} ou {respota3} ou {respota4}!")

def valida_input_numero_menor_que_quatro(pergunta, n):

    input_do_usuario = input(pergunta)
    while True:

        try:
            input_do_usuario = int(input_do_usuario)
            if input_do_usuario >=0 and input_do_usuario < n :
                return input_do_usuario
            else:
                input_do_usuario =  input(f"Escolha um número maior ou igual a 0 e menor que {n}!")
            
        except:

            input_do_usuario = input(f"Escolha um número maior ou igual a 0 e menor que {n}!")

        