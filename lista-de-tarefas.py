rich = True

#importando recursos do rich
try:
    from rich.console import Console
    from rich.table import Table
    from rich import box
except ImportError:
    print("A biblioteca Rich não está instalada. Rode: pip install rich ou prossiga sem estilização.")
    rich = False

console = Console()

# lista que armazena as tarefas
tarefas = []

#função para exibir tabelas com rich

def exibirTabela(lista, titulo):
    table = Table(
    title=titulo,
    box=box.ASCII2,
    title_style="bold blue",
    header_style="bold white on blue",
    border_style="bright_blue",
)
    for coluna in lista[0].keys():
        table.add_column(coluna.capitalize())

    for item in lista:
        table.add_row(*[str(valor) for valor in item.values()])

    console.print(table)

#exibir separação entre sessões
def separar():
    if rich == False:
        print("\n","+---------------+------------------+", "\n")
    else:
        console.print("\n","+---------------+------------------+", "\n", style="bold blue")

# função para cadastrar nova tarefa
def cadastrarNovaTarefa():
    separar()
    titulo = input("Digite título da tarefa: ")
    data = input("Digite a data de execução da tarefa: ")
    detalhes = input("Descrição da tarefa: ")
    tarefas.append({"titulo": titulo,"data": data, "detalhes": detalhes})

#Lista as tarefas cadastradas 
def listarTarefas(tarefas):
    separar()
    if rich == True:
        exibirTabela(tarefas, "Listas de Tarefas Cadastradas")
    else:
        print("Listas de tarefas cadastradas:")
        for tarefa in tarefas:
            print("Tarefa nº ", index(tarefa) + 1,":", " \n Título:", tarefa["titulo"],"\n Data de execução:", tarefa["data"],"\n Detalhes:", tarefa["detalhes"])

#Exclui uma tarefa pelo nome
def excluirTarefa():
    separar()
    titulo = input("Digite o título da tarefa: ")
    for tarefa in tarefas:
        if tarefa["titulo"] == titulo:
            tarefas.remove(tarefa)
            print("Tarefa excluída com sucesso!")

#Menu principal
def menu():
    while True:
        separar()
        print("Seja bem vindo ao nosso sistema! O que deseja realizar?", "1. Cadastrar tarefa", "2. Verificar tarefa cadastrados", "3. Excluir tarefa", "4. Sair", sep="\n")
        opcao = int(input("Digite aqui: "))

        if opcao == 1:
            cadastrarNovaTarefa()
        elif opcao == 2:
            listarTarefas(tarefas)
        elif opcao == 3:
            excluirTarefa()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Por favor, digite uma opção válida.")
            

#chama o menu principal
menu()

    