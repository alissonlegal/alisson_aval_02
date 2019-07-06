'''
fup em python para simular o atendimento num posto de vacinacao. lembre-se que a inclusao é feita no fim
(ex: f.append(elem) )
e a remocao é feita no inicio
(ex  f.pop(0) )
'''

fila = []

while True:
    # print(fila)
    opcao = input("Para adicionar paciente na fila digite 1 \nou para remover o primeira da fila digite 2: ")
    if opcao == '1':
        paciente = input("Insira o nome do paciente: ")
        fila.append(paciente)
    elif opcao == '2' and fila == []:
        print("\n           Fila ja esta vazia!      ")

    elif opcao == '2':
        fila.pop(0)

    else:
        break
    print(fila)
    print("\n_____________________________________________")
