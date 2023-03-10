def calculadora(numero1, numero2, operacao):
  if( operacao == 1):
    if( numero2 >= 0):
      print(numero1, "+", numero2, " = ", numero1 + numero2)

    else:
      print( numero1, "-", numero2/-1, " = ", numero1 + numero2)
  elif(operacao == 2):
    if( numero2 >= 0):
      print(numero1, "-", numero2, " = ", numero1 - numero2)
    else:
      print(numero1 , numero2, " = ", numero1 + numero2)

  elif(operacao == 3):
    print(numero1, "*", numero2," = ", numero1 * numero2)
    
  elif(operacao == 4):
    if(numero2 != 0):
      print(numero1, "/", numero2, " = ", numero1 / numero2)
    else:
      print("Para divisão, o segundo número não pode ser 0.")
  else:
    print(0)

print("Soma")
calculadora(7, 7 , 2)
calculadora(15, -8, 3)
calculadora(-10, -9, 4)
print()

print("Subtração")
calculadora(10, 5, 2)
calculadora(33, -9, 32)
calculadora(-30, -12, 2)
print()

print("Multiplicação")
calculadora(5, 2, 3)
calculadora(20, -30, 8)
print()

print("Divisão")
calculadora(3, 10, 4)
calculadora(32, -5, 4)
calculadora(-29, -5, 4)
calculadora(42, 0, 4)
print()

print("Opção inexistente")
calculadora(2, 10, 5)
calculadora(30, -5, 11)
calculadora(-50, -5, 7)
calculadora(4, 0, 13)