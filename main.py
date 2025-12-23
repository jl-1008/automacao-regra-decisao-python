"""
Automação de decisão por valor de solicitação.

Este programa recebe o valor e o tipo de uma solicitação
e define automaticamente seu status com base em regras
de negócio e categorias emergenciais.
"""
# imports 
# (não são necessários imports adicionais nesse projeto)

# ---------------------------
# CONSTANTES (políticas da empresa)
# ---------------------------

LIMITE_APROVADO = 1000
VALOR_MAX_EMERGENCIA = 5000

TIPOS_EMERGENCIA = ["despesa_extra", "acidente", "prejuizo"]
#TIPOS_VALIDOS = ["despesa_extra", "acidente", "prejuizo", "operacional", "planejada"]

# ---------------------------
# FUNÇÃO DE REGRA DE NEGÓCIO
# ---------------------------

def definir_status(valor, tipo_solicitacao):
    """
    Retorna o status da solicitação com base nas regras de negócio.

    Regras:
        1. Até LIMITE_APROVACAO → aprovado automaticamente
        2. Se for emergência e <= VALOR_MAX_EMERGENCIA → aprovado emergencialmente
        3. Acima disso → encaminhado para análise da gerência
    """
    # Regra 1: aprovação automática
    if valor <= LIMITE_APROVADO:
       return "Aprovada automaticamente"
    
    # Regra 2: emergência aprovada
    if tipo_solicitacao in TIPOS_EMERGENCIA and valor <= VALOR_MAX_EMERGENCIA:
        return "Aprovada (EMERGÊNCIA)"
    
    # Regra 3: análise necessária
    return "EM ANÁLISE"
    
# ---------------------------
# FUNÇÃO PRINCIPAL (main)
# ---------------------------

def main():
    while True:
        try:
           valor = float(input("Informe o valor da solicitação: "))

           #Menu de tipos
           print("\nSelecione o tipo da solicitacção")
           print("1 - Despesa extra")
           print("2 - Acidente")
           print("3 - Prejuízo")
           print("4 - Operacional")
           print("5 - Planejada")

           tipo_opcao = input("Digite o número correspondente ao tipo: ")

           TIPO_MAPEADO = {
               "1": "despesa_extra",
               "2": "acidente",
               "3": "prejuizo",
               "4": "operacional",
               "5": "planejada",
           }

           # Converte a opção em texto
           tipo = TIPO_MAPEADO.get(tipo_opcao)

           # Validação do tipo
           if not tipo:
               print("⚠ Tipo inválido. Escolha uma opção de 1 a 5.\n")
               continue
           
           # Processamento (chamada da regra de negócio)
           status = definir_status(valor, tipo)

           # Saida 
           print(f"\nStatus da solicitação: {status}\n")
           break # Sai do loop após sucesso

        except ValueError:
            print("⚠ Valor inválido. Digite apenas números.\n")

# PONTO DE ENTRADA DO PROGRAMA

if __name__ == "__main__":
    main()