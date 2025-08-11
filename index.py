consultas = []
lista_medicos = []
lista_pacientes = []

inicial = """
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Bem-Vindo! Qual sistema você deseja?
    Digite 1 para marcar uma consulta
    Digite 2 para realizar um exame
    Digite 3 para prescrever um medicamento
    Digite 4 para sair
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """

class Funcionario():
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def marcar_consulta(self, paciente, data_consulta):
        consultas.append((self.nome, paciente, data_consulta))
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


class Paciente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_medico = []

while True:
    qtd_pacientes = int(input('Digite a quantidade de pacientes: '))

    for paciente in range(qtd_pacientes):
        nome_paciente = input('Digite o nome do paciente: ')
        idade_paciente = int(input('Digite a idade do paciente: '))

        paciente = Paciente(nome_paciente, idade_paciente)
        lista_pacientes.append((paciente))

    qtd_medicos = int(input('Digite a quantidade de médicos: '))

    for medico in range(qtd_medicos):
        nome_medico = input('Digite o nome do médico: ')
        especialidade = input('Digite a especialidade do médico: ')
        crm = input('Digite o CRM do médico: ')

        medico = Medico(nome_medico, especialidade, crm)
        lista_medicos.append(medico)

    print(inicial)
    escolha_usuario = int(input("Digite a opção desejada: "))

    if escolha_usuario == 1:
        tipo_funcionario = input('Quem fará a consulta é um médico ou enfermeiro? ').lower()
        if tipo_funcionario == 'médico':
            nome_funcionario = input('Qual o nome do médico? ')
            for m in lista_medicos:
                if m.nome_medico == nome_funcionario:
                    paciente = input('A consulta será realizada com qual paciente? ')
            else:
                print('médico não encontrado!')

    if escolha_usuario == 4:
        print("Encerrando programa...")
        break


# medico1 = Medico('Drauzio Varela', 'cardiologista' ,'111')

# medico1.marcar_consulta(paciente.nome, '12/08/2026')
# medico1.marcar_consulta(paciente.nome, '12/08/2025')
# print(consultas)
# medico1.realizar_exame(paciente.nome, '12/08/2025')
# medico1.prescrever_medicamento(paciente, 'dorflex')
# print(consultas)
# print(paciente.historico_medico)