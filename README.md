# 🏪 Gerenciador de Estoque - Projeto Acadêmico

## 📚 Objetivo
Projeto acadêmico para demonstrar complexidades algorítmicas em operações de gerenciamento de estoque.

## 🚀 Como Usar

### **Execução Rápida:**
```bash
python main.py
```

### **Teste com Dados de Exemplo:**
```bash
cp estoque_exemplo.json estoque.json
python main.py
```

### **Menu Principal:**
```
1. 📦 Adicionar produto
2. 📋 Listar produtos (com filtro por categoria)
3. 🔍 Buscar produto
4. ✏️ Atualizar produto
5. 🗑️ Remover produto
6. 📊 Gerar relatório
7. 🔄 Ordenar produtos
8. 💾 Salvar estoque
9. 🔄 Recarregar estoque
10. 🗑️ Zerar estoque
0. 🚪 Sair
```

## 🎯 Análise de Complexidade

### **O(1) - Tempo Constante:**
- **Adicionar produto**: Inserção no final da lista
- **Zerar estoque**: Limpeza da lista

### **O(n) - Tempo Linear:**
- **Listar produtos**: Percorre todos os produtos (com filtro opcional)
- **Buscar produto**: Busca linear na lista
- **Atualizar produto**: Busca + atualização
- **Remover produto**: Busca + remoção com deslocamento
- **Relatório**: Cálculos sobre todos os produtos
- **Carregar/Salvar**: Serialização JSON

### **O(n log n) - Tempo Logarítmico Linear:**
- **Ordenar produtos**: Algoritmo Timsort

## 🔧 Funcionalidades

### **Operações Básicas:**
- ✅ **Adicionar produto** - O(1)
- ✅ **Listar produtos** - O(n) com filtro por categoria
- ✅ **Buscar produto** - O(n)
- ✅ **Atualizar produto** - O(n)
- ✅ **Remover produto** - O(n)

### **Relatórios e Análises:**
- ✅ **Relatório de estoque** - O(n) com alertas de estoque baixo
- ✅ **Ordenar produtos** - O(n log n) por nome, preço, quantidade ou categoria

### **Gerenciamento de Dados:**
- ✅ **Salvar/Carregar estoque** - O(n) com persistência JSON
- ✅ **Zerar estoque** - O(1) com dupla confirmação
- ✅ **Recarregar estoque** - O(n) com alerta de salvamento

### **Recursos Avançados:**
- ✅ **Entrada com vírgula**: Suporte a formato brasileiro (7,99)
- ✅ **Filtro por categoria**: Listagem inteligente
- ✅ **Segurança de dados**: Confirmações para operações destrutivas
- ✅ **Validação robusta**: Tratamento de erros e validação de entrada

## 🏗️ Estrutura do Projeto

```
gerenciador-estoque/
├── main.py                 # Sistema principal
├── estoque.json           # Dados do estoque (criado automaticamente)
├── estoque_exemplo.json   # Dados de exemplo para teste
└── README.md              # Documentação
```

## 📊 Exemplo de Uso

```python
# Inicialização
gerenciador = GerenciadorEstoque()

# Adicionar produto - O(1)
gerenciador.adicionar_produto()

# Listar produtos - O(n)
gerenciador.listar_produtos()

# Buscar produto - O(n)
produto = gerenciador.buscar_produto("Notebook")

# Ordenar produtos - O(n log n)
gerenciador.ordenar_produtos()

# Zerar estoque - O(1)
gerenciador.zerar_estoque()
```

## 🔍 Detalhes Técnicos

### **Estrutura de Dados:**
```json
{
  "produtos": [
    {
      "id": 1,
      "nome": "Produto",
      "preco": 100.00,
      "quantidade": 10,
      "categoria": "Categoria",
      "data_cadastro": "2024-01-15T10:30:00"
    }
  ],
  "ultima_atualizacao": "2024-01-15T10:30:00"
}
```

### **Segurança:**
- **Dupla confirmação** para operações destrutivas
- **Validação de entrada** para todos os campos
- **Alerta de salvamento** antes de recarregar
- **Confirmação por palavra** para zerar estoque

## 📈 Resumo de Complexidades

| Complexidade | Funções | Quantidade |
|--------------|---------|------------|
| **O(1)** | Adicionar produto, Zerar estoque | 2 |
| **O(n)** | Listar, Buscar, Atualizar, Remover, Relatório, Salvar/Carregar | 6 |
| **O(n log n)** | Ordenar produtos | 1 |

## 🎓 Objetivos Acadêmicos

✅ **Demonstração de complexidades**: O(1), O(n), O(n log n)  
✅ **Estruturas de dados**: Listas, dicionários, JSON  
✅ **Algoritmos**: Busca linear, ordenação Timsort  
✅ **Boas práticas**: Código modular, tratamento de erros, validação  

## 👨‍💻 Autor
Projeto desenvolvido para fins acadêmicos com foco em análise de complexidade algorítmica.

## 📝 Licença
Este projeto é de uso acadêmico e educacional.