"""Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário um número e verifica se ele é par ou ímpar."""

#pede ao usuário um número
numero = int(input("Digite um número:"))

#verifica se ele é par ou ímpar
if numero % 2 == 0:
    print("par")
