from paciente import Paciente
from funcionario import Funcionario
from enfermeiro import Enfermeiro

pacientes = []
funcionarios = []
enfermeiros = []

while True:
    print("\n--- Hospital Santa Maria ---")
    print("1. Adicionar paciente")
    print("2. Apresentar pacientes")
    print("3. Atender paciente")
    print("4. Ver histórico do paciente")
    print("5. Adicionar funcionário")
    print("6. Apresentar funcionários")
    print("7. Aumentar salário")
    print("8. Adicionar enfermeiro")
    print("9. Apresentar enfermeiros")
    print("10. Atribuir paciente a enfermeiro")
    print("11. Ver pacientes de enfermeiro")
    print("12. Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        nome = input("Nome do paciente: ")
        idade = int(input("Idade: "))
        numero = int(input("Número de utente: "))
        p = Paciente(nome, idade, numero)
        pacientes.append(p)
        print("Paciente adicionado!\n")

    elif op == "2":
        if not pacientes:
            print("Nenhum paciente registrado no sistema.")
        else:
            for i, p in enumerate(pacientes, 1):
                print(f"{i}. {p.nome} - {p.numero_utente}")

    elif op == "3":
        if not pacientes:
            print("Nenhum paciente registrado no sistema.")
        else:
            for i, pac in enumerate(pacientes, 1):
                print(f"{i}. {pac.nome}")
            n = int(input("Escolha o número do paciente: "))
            paciente = pacientes[n-1]
            desc = input("Motivo da consulta: ")
            paciente.adicionar_registro(desc)
            print("O paciente ja esta a ser atendido, obrigado!\n")

    elif op == "4":
        if not pacientes:
            print("Nenhum paciente registrado no sistema.")
        else:
            for i, pac in enumerate(pacientes, 1):
                print(f"{i}. {pac.nome}")
            n = int(input("Escolha o número do paciente: "))
            paciente = pacientes[n-1]
            paciente.mostrar_historico()

    elif op == "5":
        nome = input("Nome do funcionário: ")
        idade = int(input("Idade: "))
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))
        f = Funcionario(nome, idade, cargo, salario)
        funcionarios.append(f)
        print("Funcionário adicionado!\n")

    elif op == "6":
        if not funcionarios:
            print("Nenhum funcionário registrado no sistema.")
        else:
            for i, f in enumerate(funcionarios, 1):
                print(f"{i}. {f.nome} - {f.cargo} - {f.salario:.2f}€")

    elif op == "7":
        if not funcionarios:
            print("Nenhum funcionário registrado no sistema.")
        else:
            for i, f in enumerate(funcionarios, 1):
                print(f"{i}. {f.nome} - {f.salario:.2f}€")
            n = int(input("Escolha o número do funcionário: "))
            perc = float(input("Percentagem de aumento que que dar ao funcionário: "))
            funcionarios[n-1].aplicar_aumento(perc)
            print("Aumento realizado com sucesso!\n")

    elif op == "8":
        nome = input("Nome do enfermeiro: ")
        idade = int(input("Idade: "))
        salario = float(input("Salário base: "))
        turno = input("Turno (dia/noite): ")
        try:
            e = Enfermeiro(nome, idade, salario, turno)
            enfermeiros.append(e)
            print("Enfermeiro adicionado!\n")
        except ValueError as erro:
            print(f"Erro: {erro}\n")

    elif op == "9":
        if not enfermeiros:
            print("Nenhum enfermeiro registrado no sistema.")
        else:
            for i, enf in enumerate(enfermeiros, 1):
                print(f"{i}. {enf.nome} - Turno: {enf.turno} - Pacientes: {len(enf.pacientes)} - Salário: {enf.calcular_pagamento():.2f}€")

    elif op == "10":
        if not enfermeiros:
            print("Nenhum enfermeiro registrado no sistema.")
        elif not pacientes:
            print("Nenhum paciente registrado no sistema.")
        else:
            print("Enfermeiros disponíveis:")
            for i, enf  in enumerate(enfermeiros, 1):
                print(f"{i}. {enf.nome} - Turno: {enf.turno}")
            n_enf = int(input("Escolha o número do enfermeiro: "))
            
            print("\nPacientes disponíveis:")
            for i, pac in enumerate(pacientes, 1):
                print(f"{i}. {pac.nome}")
            n_pac = int(input("Escolha o número do paciente: "))
            
            enfermeiros[n_enf-1].adicionar_paciente(pacientes[n_pac-1])
            print(f"Paciente {pacientes[n_pac-1].nome} atribuído ao enfermeiro {enfermeiros[n_enf-1].nome}!\n")

    elif op == "11":
        if not enfermeiros:
            print("Nenhum enfermeiro registrado no sistema.")
        else:
            for i, enf in enumerate(enfermeiros, 1):
                print(f"{i}. {enf.nome} - Turno: {enf.turno}")
            n = int(input("Escolha o número do enfermeiro: "))
            print()
            enfermeiros[n-1].apresentar_pacientes()
            print()

    elif op == "12":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
