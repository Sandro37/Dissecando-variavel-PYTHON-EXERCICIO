texto = input("Digite Algo: ")

print("INFORMAÇÕES DA SUA ENTRADA")
print("____________________________\n")
print("o tipo primitivo é = " , type(texto))
print("Existe só espaço = ", texto.isspace())
print("É um número = " , texto.isnumeric())
print("Alfabético = ", texto.isalpha())
print("Alfanumérico = ", texto.isalnum())
print("Está em maiucula = ", texto.isupper())
print("Está em minuscula = ", texto.islower())
print("Está capitalizada = ", texto.istitle())