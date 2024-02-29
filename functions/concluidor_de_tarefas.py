def concluir_tarefa(tarefas):
    selecionar_tarefa = input("Digite o Título da Tarefa para Concluir: ").strip().lower()
    for titulo, tarefa in tarefas.items():
        if 'Título' in tarefa and selecionar_tarefa == tarefa['Título'].lower():
            del tarefas[titulo]
            print("Parabéns. Tarefa Concluída!")
            return
    print("Tarefa Não Encontrada.")