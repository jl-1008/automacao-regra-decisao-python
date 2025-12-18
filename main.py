"""
Automação de decisão por valor de solicitação.

Este programa recebe o valor e o tipo de uma solicitação
e define automaticamente seu statuts com base em regras
de negócio e categorias emergenciais.
"""

# imports 
# (não são necessários imports adicionais nesse projeto)
# constantes (politicas de negócio)
LIMITE_APROVADO = 1000
VALOR_MAX_EMERGENCIA = 5000
TIPOS_EMERGENCIA = ["despesa_extra", "acidente", "prejuizo"]
TIPOS_VALIDOS = ["despesa_extra", "acidente", "prejuizo", "operacional", "planejada"]


def definir_status(valor, tipo_solicitacao):
    """
    Define o status da solicitação com base no valor e tipo informado.
    """
    if tipo_solicitacao in TIPOS_EMERGENCIA and valor <= VALOR_MAX_EMERGENCIA:
        return "APROVADA (EMERGÊNCIA)"
    elif valor <= LIMITE_APROVADO:
        return "APROVADA"
    else:
        return "EM ANÁLISE"
    
def main():
    while True:
        try:
           # Entrada de valor
           valor = float(input("Informe o valor da solicitação: "))

           if valor <= 0:
               print("Erro: o valor deve ser maior que zero. ")
               continue
           
           # Entrada do tipo
           tipo = input( 
                "Informe o tipo da solicitação"
                "(despesa_extra, acidente, prejuizo, operacional, planejada): "
            ).lower()
           
           if tipo not in TIPOS_VALIDOS:
              print("Erro: tipo de solicitação inválido.")
              continue
           
           # Processamento (regra de negócio)
           status = definir_status(valor, tipo)

           #saida 
           print(f"Status da solicitação: {status}")
           break

        except ValueError:
            print("Erro: informe um valor numérico válido.")


if __name__ == "__main__":
    main()