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