import sys

from lexer import LudiCodeLexer
from parse import LudiCodeParser
from interpreter import LudiCodeInterpreter


def compilar_e_executar(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            codigo_fonte = arquivo.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' nao foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    print("--- [1] Iniciando Analise Lexica ---")
    lexer = LudiCodeLexer()
    
    print("\n--- [2] Iniciando Analise Sintatica ---")
    parser = LudiCodeParser()
    ast = parser.parse(lexer.tokenize(codigo_fonte))

    if ast is None:
        print("Execucao interrompida devido a erros sintaticos.")
        return

    print("Arvore de Sintaxe Abstrata (AST) gerada:")
    print(ast)

    print("\n--- [3] Execucao / Interpretador ---")
    try:
        interpretador = LudiCodeInterpreter()
        resultado = interpretador.run(ast)

        print("\nSaida do programa:")
        for item in resultado["saida"]:
            print(item)

        print("\nEstado final:")
        print("Variaveis:", resultado["variaveis"])
        print("Sensores:", resultado["sensores"])
        print("Motores:", resultado["motores"])
        print("Eventos:", resultado["eventos"])

    except Exception as e:
        print(f"Erro durante a execucao: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arquivo_alvo = sys.argv[1]
    else:
        arquivo_alvo = "estrategia.ludi"

    compilar_e_executar(arquivo_alvo)