repetir = "S"
nomeCliente = input("Nome do Cliente: ")
valorCompra = float(input("Valor da compra: R$ "))
if valorCompra > 100:
    desconto = valorCompra * 0.10
else:
    desconto = 0

valorFinal = valorCompra - desconto 

print("\nCliente:" , nomeCliente)
print("Desconto: R$" , desconto)
print("Valor final: R$" , valorFinal)

repetir = input("\nDeseja relizar outro atendimento? (S/N):").upper()
print("Programa encerrado. ")
