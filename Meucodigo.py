import json

#Definir as opções do menu principal
a = 'Menu do estudante'
b = 'Menu do professor'
c = 'Menu da disciplina'
d = 'Menu da turma'
e = 'Menu da matrícula'

#funções:

#Função para ler e retornar o arquivo json.
def ler_json(nome_do_arquivo):
    try:
        with open(nome_do_arquivo + ".json", 'r', encoding="utf-8") as arquivo:
                leitura_json = json.load(arquivo)
                arquivo.close()
                return leitura_json
    except:
                return []
        
        
#Função para escrever no arquivo json.
def escrever_json(lista, nome_do_arquivo):
    with open(nome_do_arquivo + ".json", 'w', encoding="utf-8") as arquivo:
        json.dump(lista, arquivo)
        arquivo.close()


#função para apresentar o menu de principal.
def menu_principal():
    print('\n*** Menu Principal ***\n\n Escolha a opção: \n\n (a) estudante\n (b) professor \n (c) disciplina\n (d) turma\n (e) matrícula\n ')
    return None

#função para apresentar o menu de ação.
def menu_de_acao():
    print('\n-----------------\n', escolha ,'\n\n Escolha a ação:\n\na. incluir\nb. listar\nc. excluir\nd. alterar\ne. Voltar ao menu principal\n')
    return None

# função para manter a lista ordenada numericamente
        
def ordenar(lista):
    for item in lista:
        item['codigo'] = lista.index(item) + 1
    

#função para incluir um usuário.
def incluir(nome_do_arquivo, escolha, nome_do_arquivo2 = None, nome_do_arquivo3 = None):
    print('\n Incluir \n')
    #***incluir professores ou alunos***
    if escolha == a or escolha == b:
        lista = ler_json(nome_do_arquivo)

        codigo = 0
        nome = input('digite o nome do usuário:')
        cpf = input('digite o cpf nome do usuário:')
        
        #estrutura de tupla para cadastrar os usuários
        aux = {'codigo': codigo,
            'nome': nome,
            'cpf': cpf}
        #adiciona à lista e ordena em ordem crescente
        lista.append(aux)
        ordenar(lista)

        escrever_json(lista, nome_do_arquivo)
        return lista
    


    #***incluir disciplinas***
    elif escolha == c: 
        lista = ler_json(nome_do_arquivo)

        codigo = 0
        nome = input('digite o nome da disciplina:')

         #estrutura de tupla para cadastrar os usuários
        aux = {'codigo': codigo,
            'nome': nome,
                        }
        
        #adiciona à lista e ordena em ordem crescente
        lista.append(aux)
        ordenar(lista)

        escrever_json(lista, nome_do_arquivo)
        return lista



    #***incluir Turmas***
    elif escolha == d:
        lista = ler_json(nome_do_arquivo)
        lista_professores = ler_json(nome_do_arquivo2)
        lista_disciplinas = ler_json(nome_do_arquivo3)

        codigo = 0

        #validar se professor e disciplina existem
        val1 = False
        val2 = False

        while val1 == False:
            codigo_professor = int(input('digite o código do professor: '))
            
            for item in lista_professores:
                if item['codigo'] == codigo_professor:
                    val1 = True
            if val1 == False:
                print('professor não existe.')

        while val2 == False:
            codigo_disciplina = int(input('digite o código da disciplina: '))
            
            for item in lista_disciplinas:
                if item['codigo'] == codigo_disciplina:
                    val2 = True
            if val2 == False:
                print('disciplina não existe.')

        #estrutura de tupla para cadastrar os usuários
        aux = {'codigo': codigo,
            'codigo_professor': codigo_professor,
            'codigo_disciplina': codigo_disciplina}
        
        #adiciona à lista e ordena em ordem crescente
        lista.append(aux)
        ordenar(lista)

        escrever_json(lista, nome_do_arquivo)
        return lista
    


        #***incluir matrículas***
    elif escolha == e:
        lista = ler_json(nome_do_arquivo)
        lista_turmas = ler_json(nome_do_arquivo2)
        lista_alunos = ler_json(nome_do_arquivo3)

        codigo = 0

        #validar se turma e aluno existem
        val1 = False
        val2 = False

        while val1 == False:
            codigo_turma = int(input('digite o código da turma: '))
            
            for item in lista_turmas:
                if item['codigo'] == codigo_turma:
                    val1 = True
            if val1 == False:
                print('turma não existe.')

        while val2 == False:
            codigo_aluno = int(input('digite o código do aluno: '))
            
            for item in lista_alunos:
                if item['codigo'] == codigo_aluno:
                    val2 = True
            if val2 == False:
                print('aluno não existe.')

        #estrutura de tupla para cadastrar os usuários
        aux = {'codigo': codigo,
            'codigo_turma': codigo_turma,
            'codigo_aluno': codigo_aluno}
        
        #adiciona à lista e ordena em ordem crescente
        lista.append(aux)
        ordenar(lista)

        escrever_json(lista, nome_do_arquivo)
        return lista
        
                

#função de listar os usuarios.
def listar(nome_do_arquivo, escolha, nome_do_arquivo2 = None, nome_do_arquivo3 = None):
    print('\n listar \n')

    lista = ler_json(nome_do_arquivo)
    #listar professores ou estudantes
    if escolha == a or escolha == b:
        #mostrar os elementos presentes na lista
        if len(lista) < 1:
            print('-----------------')
            print('\n-----------------\n Não há usuários cadastrados.')
        else:
            print('Os usuários incluídos são:')
            for i in lista:
                print('* {} - {} - {}'.format(i['codigo'], i['nome'], i['cpf']))
        return lista
    
    #listar disciplinas
    elif escolha == c:
        #mostrar os elementos presentes na lista
        if len(lista) < 1:
            print('-----------------')
            print('\n-----------------\n Não há disciplinas cadastradas.')
        else:
            print('As disciplinas incluídas são:')
            for i in lista:
                print('* {} - {}'.format(i['codigo'], i['nome']))
        return lista
    
    #listar turmas
    elif escolha == d:
        lista_professor = ler_json(nome_do_arquivo2)
        lista_disciplina = ler_json(nome_do_arquivo3)
        #mostrar os elementos presentes na lista
        if len(lista) < 1:
            print('-----------------')
            print('\n-----------------\n Não há turmas cadastradas.')
        else:
            print('As turmas incluídas são:')
            for i in lista:
                for item in lista_professor:
                    if i['codigo_professor'] == item['codigo']:
                        nome_professor = item['nome']
                        break
                for item in lista_disciplina:
                    if i['codigo_disciplina'] == item['codigo']:
                        nome_disciplina = item['nome']
                        break    
                print('* turma: {} - professor: {} - disciplina: {}'.format(i['codigo'], nome_professor, nome_disciplina))
        return lista
    
    #listar matrículas
    elif escolha == e:
        lista_turmas = ler_json(nome_do_arquivo2)
        lista_estudantes = ler_json(nome_do_arquivo3)
        #mostrar os elementos presentes na lista
        if len(lista) < 1:
            print('-----------------')
            print('\n-----------------\n Não há turmas cadastradas.')
        else:
            print('As matrículas incluídas são:')
            for i in lista:
                for item in lista_turmas:
                    if i['codigo_turma'] == item['codigo']:
                        nome_turma = item['codigo']
                        break
                for item in lista_estudantes:
                    if i['codigo_aluno'] == item['codigo']:
                        nome_aluno = item['nome']
                        break    
                print('*matricula: {} - turma: {} - aluno: {}'.format(i['codigo'], nome_turma, nome_aluno))
        return lista

#função de excluir um usuario.
def excluir(nome_do_arquivo):

    lista = ler_json(nome_do_arquivo)

    code = int(input('Digite o código do usuário que deseja excluir: '))
    achou = False
    #Verificar se o codigo existe e excluir
    for item in lista:
        if item['codigo'] == code:
            print('\n Excluindo... \n')
            lista.remove(item)
            achou = True
            break
        if not achou:
            print('usuário não encontrado.')
    
    ordenar(lista)
    escrever_json(lista, nome_do_arquivo)
    return lista



#função de editar um usuario.
def editar(nome_do_arquivo, escolha, nome_do_arquivo2 = None, nome_do_arquivo3 = None):

    #***Editar professor ou aluno***
    if escolha == a or escolha == b:
        lista = ler_json(nome_do_arquivo)

        code = int(input('Digite o código do usuário que deseja editar: '))
        achou = False

        #Verificar se o codigo existe e pedir os novos dados
        for item in lista:
            if item['codigo'] == code:

                print('\n Insira os novos dados a seguir: \n')
                item['nome'] = input('Insira o nome do usuário: ')
                item['cpf'] = input('Insira o cpf do usuário: ')

                achou = True
                break
            if not achou:
                print('usuário não encontrado.')

        escrever_json(lista, nome_do_arquivo)

        return lista
    

        #***Editar disciplina***
    if escolha == c:
        lista = ler_json(nome_do_arquivo)

        code = int(input('Digite o código da disciplina que deseja editar: '))
        achou = False

        #Verificar se o codigo existe e pedir os novos dados
        for item in lista:
            if item['codigo'] == code:

                print('\n Insira os novos dados a seguir: \n')
                item['nome'] = input('Insira o nome do usuário: ')

                achou = True
                break
            if not achou:
                print('disciplina não encontrada.')

        escrever_json(lista, nome_do_arquivo)

        return lista
    

    #***Editar turma***
    if escolha == d:
        lista = ler_json(nome_do_arquivo)
        lista_professores = ler_json(nome_do_arquivo2)
        lista_disciplinas = ler_json(nome_do_arquivo3)

        code = int(input('Digite o código da turma que deseja editar: '))
        achou = False

        #Verificar se o codigo existe e pedir os novos dados
        for item in lista:
            if item['codigo'] == code:

                print('\n Insira os novos dados a seguir: \n')

                #validar se professor e disciplina existem
                val1 = False
                val2 = False

                while val1 == False:
                    codigo_professor = int(input('digite o código do professor: '))
                    
                    for i in lista_professores:
                        if i['codigo'] == codigo_professor:
                            item['codigo_professor'] = codigo_professor
                            val1 = True
                    if val1 == False:
                        print('professor não existe.')

                while val2 == False:
                    codigo_disciplina = int(input('digite o código do disciplinas: '))
                    
                    for i in lista_disciplinas:
                        if i['codigo'] == codigo_disciplina:
                            item['codigo_disciplina'] = codigo_disciplina
                            val2 = True
                    if val2 == False:
                        print('disciplina não existe.')

                achou = True
                break
            if not achou:
                print('turma não encontrada.')

        escrever_json(lista, nome_do_arquivo)
        return lista
            

    #***Editar matrícula***
    if escolha == e:
        lista = ler_json(nome_do_arquivo)
        lista_turmas = ler_json(nome_do_arquivo2)
        lista_alunos = ler_json(nome_do_arquivo3)

        code = int(input('Digite o código da matrícula que deseja editar: '))
        achou = False

        #Verificar se o codigo existe e pedir os novos dados
        for item in lista:
            if item['codigo'] == code:

                print('\n Insira os novos dados a seguir: \n')

                #validar se turma e aluno existem
                val1 = False
                val2 = False

                while val1 == False:
                    codigo_turma = int(input('digite o código da turma: '))
                    
                    for i in lista_turmas:
                        if i['codigo'] == codigo_turma:
                            item['codigo_turma'] = codigo_turma
                            val1 = True
                    if val1 == False:
                        print('turma não existe.')

                while val2 == False:
                    codigo_aluno = int(input('digite o código do aluno: '))
                    
                    for i in lista_alunos:
                        if i['codigo'] == codigo_aluno:
                            item['codigo_aluno'] = codigo_aluno
                            val2 = True
                    if val2 == False:
                        print('aluno não existe.')

                achou = True
                break
            if not achou:
                print('matrícula não encontrada.')

        escrever_json(lista, nome_do_arquivo)
        return lista

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Apresentar o menu principal
#loop While até que o usuário não queira mais retornar ao menu principal
while True:
    menu_principal()

  #Definir e apresentar o menu secundário com base na opção escolhida
    escolha = input('Digite aqui: ')
    if escolha == 'a':
        escolha = a

    elif escolha == 'b':
        escolha = b
        
    elif escolha == 'c':
        escolha = c

    elif escolha == 'd':
        escolha = d

    elif escolha == 'e':
        escolha = e

    #caso o usuário escolha uma opção invalida no menu principal 
    else:
        print('\n-----------------\nOpção inválida, tente novamente.\n-----------------\n')

    #Caso o usuário digite a opção estudante:
    if escolha == a:
        # Loop para apresentar o menu de ação.
        while True:
            menu_de_acao()
            acao = input('Digite aqui: ')
        
            #ação de incluir usuário 
            if acao == 'a':
                while True:
                    incluir("estudantes", a)
                    #verificar se quer adicionar mais um
                    try:
                        listest = int(input('\nDeseja acrescentar mais algum usuário? \n1- Sim 2- Não: \n'))
                    except ValueError:
                        print('Valor inválido!')
                        break
                    if listest != 1 and listest != 2:
                        print('Valor inválido!')
                        break
                    elif listest == 2:
                        break

            #ação de listar usuário
            elif acao == 'b':
                listar("estudantes", a)

            #Excluir
            elif acao == 'c':
                excluir("estudantes")

            #Editar
            elif acao == 'd':
                editar("estudantes", a)

            #retornar ao menu principal
            elif acao == 'e':
                break

    #Caso o usuário digite a opção professor:
    if escolha == b:
        # Loop para apresentar o menu de ação.
        while True:
            menu_de_acao()
            acao = input('Digite aqui: ')
        
            #ação de incluir professor 
            if acao == 'a':
                while True:
                    incluir("professores", b)
                    #verificar se quer adicionar mais um
                    try:
                        listest = int(input('\nDeseja acrescentar mais algum professor? \n1- Sim 2- Não: \n'))
                    except ValueError:
                        print('Valor inválido!')
                        break
                    if listest != 1 and listest != 2:
                        print('Valor inválido!')
                        break
                    elif listest == 2:
                        break

            #ação de listar professores
            elif acao == 'b':
                listar("professores", b)

            #Excluir
            elif acao == 'c':
                excluir("professores")

            #Editar
            elif acao == 'd':
                editar("professores", b)

            #retornar ao menu principal
            elif acao == 'e':
                break

    #Caso o usuário digite a opção disciplina:
    if escolha == c:
        # Loop para apresentar o menu de ação.
        while True:
            menu_de_acao()
            acao = input('Digite aqui: ')
        
            #ação de incluir usuário 
            if acao == 'a':
                while True:
                    incluir("disciplinas", c)
                    #verificar se quer adicionar mais um
                    try:
                        listest = int(input('\nDeseja acrescentar mais alguma disciplina? \n1- Sim 2- Não: \n'))
                    except ValueError:
                        print('Valor inválido!')
                        break
                    if listest != 1 and listest != 2:
                        print('Valor inválido!')
                        break
                    elif listest == 2:
                        break

            #ação de listar disciplina
            elif acao == 'b':
                listar("disciplinas", c)

            #Excluir
            elif acao == 'c':
                excluir("disciplinas")

            #Editar
            elif acao == 'd':
                editar("disciplinas", c)

            #retornar ao menu principal
            elif acao == 'e':
                break
            

        #Caso o usuário digite a opção turma:
    if escolha == d:
        # Loop para apresentar o menu de ação.
        while True:
            menu_de_acao()
            acao = input('Digite aqui: ')
        
            #ação de incluir turma 
            if acao == 'a':
                while True:
                    incluir("turmas", d, "professores", "disciplinas")
                    #verificar se quer adicionar mais um
                    try:
                        listest = int(input('\nDeseja acrescentar mais alguma turma? \n1- Sim 2- Não: \n'))
                    except ValueError:
                        print('Valor inválido!')
                        break
                    if listest != 1 and listest != 2:
                        print('Valor inválido!')
                        break
                    elif listest == 2:
                        break

            #ação de listar turmas
            elif acao == 'b':
                listar("turmas", d, "professores", "disciplinas")

            #Excluir
            elif acao == 'c':
                excluir("turmas")

            #Editar
            elif acao == 'd':
                editar("turmas", d, "professores", "disciplinas")

            #retornar ao menu principal
            elif acao == 'e':
                break


    #Caso o usuário digite a opção matrícula:
    if escolha == e:
        # Loop para apresentar o menu de ação.
        while True:
            menu_de_acao()
            acao = input('Digite aqui: ')
        
            #ação de incluir turma 
            if acao == 'a':
                while True:
                    incluir("matriculas", e, "turmas", "estudantes")
                    #verificar se quer adicionar mais um
                    try:
                        listest = int(input('\nDeseja acrescentar mais alguma matricula? \n1- Sim 2- Não: \n'))
                    except ValueError:
                        print('Valor inválido!')
                        break
                    if listest != 1 and listest != 2:
                        print('Valor inválido!')
                        break
                    elif listest == 2:
                        break

            #ação de listar matricula
            elif acao == 'b':
                listar("matriculas", e, "turmas", "estudantes")

            #Excluir
            elif acao == 'c':
                excluir("matriculas")

            #Editar
            elif acao == 'd':
                editar("matriculas", e, "turmas", "estudantes")

            #retornar ao menu principal
            elif acao == 'e':
                break

            #caso o usuário escolha uma opção invalida no menu de ação
            else:
                print('\n-----------------\nAção inválida, tente novamente.\n-----------------\n')

    