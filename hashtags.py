#         setattr(self, i[0], i[1][:-1])
        #         elementos = elementos + i[1][:-1]
        #         argumentos.append(i[1][-1]) # somente o -1

        # lc = [j for i in elementos for j in i]
        # largs = [ j for i in argumentos for j in i ] 
        
        # variaveis = list(zip(*elementos)[1]) 
        # args = list(itertools.chain(*[[a]*len(c) for a, c in zip(largs, lc)]))

        # parametroEtipo = [e + [arg] for e, arg in zip(elementos, args)]

        # print("\n\nelementos")
        # print(elementos)
        # print()
        # print("\n\nargumentos")
        # print(argumentos)
        # print()
        # print("\n\nlc")
        # print(lc)
        # print()
        # print("\n\nlargs")
        # print(largs)
        # print()
        # print("\n\nvariaveis")
        # print(variaveis)
        # print()
        # print("\n\nparametroEtipo")
        # print(parametroEtipo)

        # params = [ arcpy.Parameter(displayName=texto(i[0]),name=i[1], parameterType=i[2], **i[3]
        #     ) for i in parametroEtipo]

                        # print("parametros.append(arcpy.Parameter(displayName=texto{},name={}, parameterType={}, **{}))".format(j[0],j[1],j[2],i[1][-1]))
# setattr(objeto, 'nome', 'valor')
    # getattr(objeto, 'nome')

    # t = Teste()
    # setattr(t, 'novo_atributo', ['lista','de','string'])


    # Para poder mudar um atributo é necessario instanciar a classe
    # for i in inspect.getmembers(t):
    #     if not i[0].startswith("_"):
    #         print(i)


    # print('Iniciando Testes')

    # teste = Teste()
    # campos = Campos()
    # elementos = []

    # # SETANDO TODOS OS ATRIBUTOS DE UMA CLASSE EM OUTRA
    # # ASSIM COMO FAZER UMA SUPER LISTA
    # for i in inspect.getmembers(campos):
    #     if not i[0].startswith("_"):
    #         nome = i[0]
    #         valor = i[1][:-1]
    #         setattr(teste, nome, valor)
    #         elementos = elementos + valor
    
    # print("ATRIBUTOS DE TESTE")
    # for i in inspect.getmembers(campos):
    #     if not i[0].startswith("_"):
    #         print(i)

    # print("\nA SUPER LISTA\n")
    # print(elementos)
