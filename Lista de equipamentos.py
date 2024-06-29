"""
Desafio
Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

Entrada
O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

Saída
Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Antena
Roteador
Switch

Lista de Equipamentos:
- Antena
- Roteador
- Switch


Servidor
Cabinet Rack
Access Point
 	Lista de Equipamentos:
- Servidor
- Cabinet Rack
- Access Point
Edge Routers
Patch Cord
UPS

Lista de Equipamentos:
- Edge Routers
- Patch Cord
- UPS

itens = []


TESTES
 3 / 3 Testes de abertos tiveram sucesso. Clique em "ENTREGAR DESAFIO" para executar todos os testes e finalizar esse desafio.
Teste #1

Teste #2

Teste #3

Teste #4

Dúvidas ?
"""
# Cria uma Lista 'itens' para armazenar os equipamentos:
itens = []


# Cria um loop para solicitar os itens ao usuário:
for _ in range(3):
    # Solicita o item e armazena na variável "item":
    item = input()
    
    # Adiciona o item à lista "itens":
    itens.append(item)


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")