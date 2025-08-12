consultas = []
lista_medicos = []
lista_pacientes = []
lista_enfermeiros = []

inicial = """
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Bem-Vindo! Qual sistema você deseja?
    Digite 1 para marcar uma consulta
    Digite 2 para realizar um exame
    Digite 3 para prescrever um medicamento
    Digite 4 para aplicar uma injeção
    Digite 5 para sair
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """

class Funcionario():
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def marcar_consulta(self, formacao, paciente, data_consulta):
        consultas.append(((self.nome, formacao), paciente, data_consulta))
        print(f'consulta marcada para o paciente {paciente} para a data {data_consulta} com o médico/enfermeiro {self.nome}')

    def realizar_exame(self, paciente, data_exame):
        for consulta in consultas:
            if consulta[1] == paciente and consulta[2] == data_exame:
                print('consulta realizada com sucesso!')
                consultas.remove(consulta)
                break
        else:
            print('consulta não encontrada')

class Medico(Funcionario):
    def __init__(self, nome, especialidade, crm):
        super().__init__(nome, especialidade)
        self.crm = crm

    def prescrever_medicamento(self, paciente, medicamento):
        paciente.historico_medico.append(medicamento)
        print(f'medicamento {medicamento} prescrito para o paciente {paciente.nome}')

class Enfermeiro(Funcionario):
    def __init__(self, nome, especialidade, coren):
        super().__init__(nome, especialidade)
        self.coren = coren

    def aplicar_injecao(self, paciente, injecao):
        paciente.historico_medico.append(injecao)
        print(f'injeção {injecao} aplicada no paciente {paciente.nome}')

class Paciente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_medico = []

qtd_pacientes = int(input('Digite a quantidade de pacientes: '))

for paciente in range(qtd_pacientes):
    nome_paciente = input('Digite o nome do paciente: ')
    idade_paciente = int(input('Digite a idade do paciente: '))

    paciente = Paciente(nome_paciente, idade_paciente)
    lista_pacientes.append(paciente)

qtd_medicos = int(input('Digite a quantidade de médicos: '))

for medico in range(qtd_medicos):
    nome_medico = input('Digite o nome do médico: ')
    especialidade = input('Digite a especialidade do médico: ')
    crm = input('Digite o CRM do médico: ')

    medico = Medico(nome_medico, especialidade, crm)
    lista_medicos.append(medico)

qtd_enfermeiros = int(input('Digite a quantidade de enfermeiros: '))

for enfermeiro in range(qtd_enfermeiros):
    nome_enfermeiro = input('Digite o nome do enfermeiro: ')
    especialidade = input('Digite a especialidade do enfermeiro: ')
    coren = input('Digite o COREN do enfermeiro: ')

    enfermeiro = Enfermeiro(nome_enfermeiro, especialidade, coren)
    lista_enfermeiros.append(enfermeiro)

while True:
    print(inicial)
    escolha_usuario = int(input("Digite a opção desejada: "))

    if escolha_usuario == 1:
        tipo_funcionario = input('Quem fará a consulta é um médico ou enfermeiro? ').lower()

        if tipo_funcionario == 'médico':
            nome_funcionario = input('Qual o nome do médico? ')
            for m in lista_medicos:
                if m.nome == nome_funcionario:
                    nome_paciente = input('A consulta será realizada com qual paciente? ')
                    for p in lista_pacientes:
                        if p.nome == nome_paciente:
                            data = input('Qual será a data da consulta? digite nesse formato: dd/mm/yyyy: ')
                            m.marcar_consulta('médico', p.nome, data)
                            continue
                        else:
                            print('Paciente não encontrado!')
                    break
            else:
                print('Médico não encontrado!')

        if tipo_funcionario == 'enfermeiro':
            nome_funcionario = input('Qual o nome do enfermeiro? ')
            for e in lista_enfermeiros:
                if e.nome == nome_funcionario:
                    nome_paciente = input('A consulta será realizada com qual paciente? ')
                    for p in lista_pacientes:
                        if p.nome == nome_paciente:
                            data = input('Qual será a data da consulta? digite nesse formato: dd/mm/yyyy: ')
                            e.marcar_consulta('enfermeiro', p.nome, data)
                            continue
                        else:
                            print('Paciente não encontrado!')
                    break
            else:
                print('Enfermeiro não encontrado!')

    if escolha_usuario == 2:
        responsavel = input('Qual será o profissional responsável por essa consulta? ')
        paciente = input('Qual o paciente dessa consulta? ')
        data_consulta = input('Qual a data dessa consulta? ')

        for consulta in consultas:
            if consulta[0][0] == responsavel and consulta[1] == paciente and consulta[2] == data_consulta:
                if consulta[0][1] == 'médico':
                    for m in lista_medicos:
                        if m.nome == responsavel:
                            m.realizar_exame(paciente, data_consulta)
                            break
                elif consulta[0][1] == 'enfermeiro':
                    for e in lista_enfermeiros:
                        if e.nome == responsavel:
                            e.realizar_exame(paciente, data_consulta)
                            break
                break
        else:
            print('Consulta não encontrada!')

    if escolha_usuario == 3:
        medico = input('Qual é o médico que irá prescrever o medicamento? ')
        for m in lista_medicos:
            if m.nome == medico:
                paciente = input('Qual é o paciente? ')
                for p in lista_pacientes:
                    if p.nome == paciente:
                        medicamento = input('Qual o medicamento prescrito? ')
                        m.prescrever_medicamento(p, medicamento)
                        break
                    else:
                        print('Paciente não encontrado!')
            else:
                print('Médico não encontrado!')
    
    if escolha_usuario == 4:
        enfermeiro = input('Qual é o enfermeiro que irá aplicar a injeção? ')
        for e in lista_enfermeiros:
            if e.nome == enfermeiro:
                paciente = input('Qual é o paciente? ')
                for p in lista_pacientes:
                    if p.nome == paciente:
                        injecao = input('Qual é a injeção que será aplicada? ')
                        e.aplicar_injecao(p, injecao)
                        print(p.historico_medico)
                        break
                    else:
                        print('Paciente não encontrado!')
            else:
                print('Enfermeiro não encontrado!')

    if escolha_usuario == 5:
        print("Encerrando programa...")
        break