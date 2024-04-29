import pickle
import pandas as pd

def vericar_input(input_string):
    if len(input_string) != 0:
        if input_string[0].isdigit():
            b= input_string.replace(',' , '.')
            c= b.replace('.' , '' , 1).isdigit()
            return c
    return False



def pedir_parametros():
    # importa biblioteca, carregar modelo e definir variaveis
    with open('/home/brain/roberto/Desafio_01_BRAIN/desafio01/modelo_IA_e_variaveis.pkl', 'rb') as arquivo:
        dados = pickle.load(arquivo)
    IA = dados[0]
    variaveis = dados[1]

    # iniciar novo DataFrame
    df_variaveis = pd.DataFrame(columns = variaveis)
    lista_resposta = []

    # for para receber os parametros do usuario
    for features in variaveis:
        while True:
            resposta_for = input(f"Insira o valor para a coluna {features}: ")
            if vericar_input(resposta_for) == True:
                break
            else:
                print('entrada invalida, por favor digite um numero float/int')
        lista_resposta.append(resposta_for)

    df_variaveis.loc[len(df_variaveis)] = lista_resposta
    previsao_model = IA.predict(df_variaveis)
    print(f"Valor estimado: U${previsao_model.item()}")