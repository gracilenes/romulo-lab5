"""Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. Se sim, determine se é um triângulo equilátero, isósceles ou escaleno."""

print("Verificação dos lados do triângulo")
ladoA = int(input("Digite o lado A:"))
ladoB = int(input("Digite o lado A:"))
ladoC = int(input("Digite o lado A:"))

if ladoA >= ladoB + ladoC or ladoB >= ladoA + ladoC or ladoC >= ladoA + ladoB:
    print("Não é um triâmgulo válido") 
    
if ladoA == ladoB and ladoA == ladoC:
    print("EQUILÁTERO")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("iSÓSCELES")
else:
    print("ESCALENO")