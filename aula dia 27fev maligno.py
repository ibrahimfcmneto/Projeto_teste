print('calculo de perimetro do triângulo')
try:   
    n1 = float(input('primeiro lado:'))
except ValueError:
    print('O lado deve ser um número')
else:
    if n1 <= 0:
        print('O 1º lado deve ser positivo')
    else:
        try:
            n2 = float(input('Segundo lado: '))
        except ValueError:
            print('O lado deve ser um número')
        else:
            if n2 <= 0:
                print('O 2º número deve ser positivo')
            else:
                try:
                    n3 = float(input('Terceiro número: '))
                except ValueError:
                    print('O lado deve ser um número')
                else:
                    if n3 <= 0:
                        print('O 3º lado deve ser positivo')
                    else:
                        if n1 + n2 <= n3 or n1 + n3 <= n2 or n2 + n3 <= n1:
                            print('Um dos lados é muito grande')
                        else:
                            print(f'O perimetro do seu triângulo é: {n1+n2+n3}')
print('PROGRAMA TERMINADO')
                
'''
    except
n3 = float(input('terceiro lado: '))
if n1 + n2 < n3:
    print(f'erro, o terceiro ângulo é muito maior que os outros')
elif n1 + n3 < n2:
    print(f'erro o segundo ângulo é muito maior que os outros')
elif n2 + n3 < n1:
    print(f'erro o primeiro ângulo é muito maior que os outros')
else:
    soma = n1 + n2 + n3
    if soma < 0:
        print('erro')
    else:
        print(f'O perímetro dos triângulos é: {soma}')'''
