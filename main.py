"""

Precisamos criar um função que tenha um formulario no terminal que solicite x informações ao usuario.
Relatos = Atos inseguros e condições inseguras.

"""


def main():
    
    TipoRelato = input("Qual é o tipo do relato?\n")

    if TipoRelato == "Ato Inseguro":
        Data = input("Data do ocorrido:\n")
        Local = input("Local do ocorrido:\n")
        Responsavel = input("Quem foi o responsável pelo ato ou condição?\n")
        Observado = input("O relato foi observado diretamente ou informado por terceiros?\n")
        Qual = input("Qual foi o ato inseguro observado?\n")
        Normas = input("Havia normas ou procedimentos que não foram seguidos?\n")
        Risco = input("O ato inseguro representava um risco imediato?\n")
        Impacto = input("Qual foi o impacto do ato inseguro?\n")
        Descricao = input("Descrição do ocorrido:\n")
    elif TipoRelato == "Condição Insegura":
        Data = input("Data do ocorrido:\n")
        Local = input("Local do ocorrido:\n")
        Responsavel = input("Quem foi o responsável pelo ato ou condição?\n")
        Observado = input("O relato foi observado diretamente ou informado por terceiros?\n")
        Qual = input("Qual foi a condição insegura observada?\n")
        Antes = input("Essa condição já havia sido relatada anteriormente?\n")
        Risco = input("Qual é o nível de risco da condição insegura?\n")
        Incidente = input("Houve algum incidente associado a essa condição insegura?\n")
        Descricao = input("Descrição do ocorrido:\n")
    else:
        print("Você digitou um tipo de relato invalido.\nTipo Validos:  'Ato Inseguro' e 'Condição Insegura'\nTente novamente...")
        main()

main()
