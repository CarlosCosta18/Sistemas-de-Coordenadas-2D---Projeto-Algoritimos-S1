import math

contador = 0
pontos = 0

#Variaveis Quadrantes
Q1, Q2, Q3, Q4 = 0, 0, 0, 0

 #Variaveis que pegam os maiores e menores pontos em relação a distancia do ponto transladado
Pontodistante = 0



#Contadores e pontos definidos como 0 inicialmente
print("---===Sistemas de Coordenadas 2D-------")
print("Insira as coordenadas da origem transladada")

X = float(input("Digite a coordenada X: "))
Y = float(input("Digite a coordenada Y: "))

contador = int(input("Quantos pontos serão lidos?: "))

#Coordenada transladada X e Y
ctx = X
cty = Y

#Aqui começa a repetição segundo o numero que o usuario informou
while pontos < contador:
    pontos += 1
    print("Escreva o Ponto ", pontos)
    X = int(input("Digite a coordenada X: "))
    Y = int(input("Digite a coordenada Y: "))
    
#identificador de Quadrantes1

    if ctx == X or cty == Y:
        print("Pontos", "(", X, ",", Y, ")", "Estão no eixo de coordenadas")
        
  
    elif X > 0 and Y > 0:
        print("Pontos", "(", X, ",", Y, ")", "Esta no 1º Quadrante")
        Q1 += 1
        
    elif X < 0 and Y > 0:
        print("Pontos", "(", X, ",", Y, ")", "Esta no 2º Quadrante")
        Q2 += 1
        
    elif X < 0 and Y < 0:
        print("Pontos", "(", X, ",", Y, ")", "Esta no 3º Quadrante")
        Q3 += 1  
        
    elif X > 0 and Y < 0:
        print("Pontos1", "(", X, ",", Y, ")", "Esta no 4º Quadrante")
        Q4 += 1   
        
    
    #Diferença =  Distancia entre pontos
    Diferenca = math.sqrt(((ctx - X)**2) + ((cty - Y)**2))

   
    
   
    #Identificado de pontos proximos e distantes
    if Diferenca >= Pontodistante:
        Pontodistante = Diferenca
        Xpontodistante = X
        Ypontodistante = Y 
        
        
    if Diferenca <= Diferenca:
        Pontoproximo = Diferenca
        Xpontoproximo = X
        Ypontoproximo = Y
        
        
    print("A distancia entre pontos é:", Diferenca)
    
 
 

    
    

print(f"Os Pontos ({Xpontoproximo}, {Ypontoproximo}) são os mais próximos, distância: {Pontoproximo:.2f}")
print(f"Os Pontos ({Xpontodistante}, {Ypontodistante}) são os mais distantes, distância: {Pontodistante:.2f}")

#Parte final, demonstrador de quadrantes   
if(Q1 == 0):
    print("Não há pontos no 1º Quadrante")
else:
    print("Há", Q1, "Ponto(s) no 1º Quadrante")
    
if(Q2 == 0):
    print("Não há pontos no 2º Quadrante")
else:
    print("Há", Q2, "Ponto(s) no 2º Quadrante")

if(Q1 == 0):
    print("Não há pontos no 3º Quadrante")
else:
    print("Há", Q3, "Ponto(s) no 3º Quadrante")

if(Q1 == 0):
    print("Não há pontos no 4º Quadrante")
else:
    print("Há", Q4, "Ponto(s) no 4º Quadrante")
    
    
    
print("----------------------------------------------------------------")   
print("--------------------Andador de Coordenadas----------------------")
#Parte B do projeto

#zerando o valor das variaveis
X = 0
Y = 0
ctx = 0
cty = 0
contador = 0
pontos = 0

#Aqui começa a parte B
print("Insira as coordenadas da origem transladada")

X = float(input("Digite a coordenada X: "))
Y = float(input("Digite a coordenada Y: "))

#Verificador se as Coordenadas não são negativas, caso sejam, o programa continuara a solicitar coordenadas positivas
while X and Y < 0:
    print("Insira Coordenadas positivas somente")
    X = float(input("Digite a coordenada X: "))
    Y = float(input("Digite a coordenada Y: "))
    

ctx = X
cty = Y

#Mesma proposta de contador, mas dessa vez significando segundos
contador = int(input("Por quanto tempo o robô irá caminhar?: "))


while pontos < contador:
    pontos  += 1
    for X in range(1, contador, 3):
        X += 2
        
  
    for Y in range(2, contador, 3):
        Y += 1
    
    

    
    



print("O robo parou em:", "(", X, ",", Y, ")")
  







