# 🤖 Automação de Regra de Decisão com Python

## 📌 Descrição
Projeto desenvolvido em Python para automatizar regras de decisão comuns em processos operacionais, aplicando lógica de programação, validação de dados e organização de fluxos.

O sistema simula um cenário real de aprovação de solicitações com base no valor e tipo, seguindo regras de negócio previamente definidas.

---

## 🎯 Objetivo

Reduzir erros manuais e padronizar decisões operacionais por meio de um script simples, claro e reutilizável, simulando o comportamento de sistemas corporativos.

---

## ⚙️ Regras de Negócio Implementadas

- Solicitações **emergenciais** possuem limite máximo específico.  
- Solicitações **não emergenciais** seguem um limite padrão.  
- Tipos de solicitação são validados antes do processamento.  
- Entradas inválidas não quebram o sistema (tratamento com `try/except`).  
- O programa usa menu numérico para evitar erros de digitação.  
- O fluxo permanece ativo até que uma entrada correta seja fornecida.

---

## 🧠 Conceitos Aplicados

- Lógica de programação  
- Estruturas condicionais (`if`, `elif`, `else`)  
- Estruturas de repetição (`while`)  
- Tratamento de exceções (`try`, `except`)  
- Funções e separação de responsabilidades  
- Constantes como políticas de negócio  
- Validação de dados de entrada  
- Uso de dicionário para melhorar organização de opções  
- Simulação de fluxos reais de processos operacionais

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/jl-1008/automacao-regra-decisao-python.git

Execute o programa:
python main.py

