def vericar_input(input_string):
    if len(input_string) != 0:
        if input_string[0].isdigit():
            b= input_string.replace(',' , '.')
            c= b.replace('.' , '' , 1).isdigit()
            return c
    print('entrada invalida')
    return False

resposta = input('digite um numero: ')

print(vericar_input(resposta))