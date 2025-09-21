# 🏪 Gerenciador de Estoque - Projeto Acadêmico

## 📚 Objetivo
Este projeto foi desenvolvido com foco acadêmico para demonstrar diferentes complexidades algorítmicas (O(1), O(n), O(n log n)) em operações de gerenciamento de estoque.

## 🚀 Funcionalidades

### 1. **Adicionar Produto** - O(1)
- **Complexidade**: O(1) para inserção + O(n) para verificação de duplicatas
- **Operação**: Adiciona novo produto ao final da lista
- **Dados**: Nome, preço (com suporte a vírgula), quantidade, categoria
- **Validação**: Verifica duplicatas e valores negativos

### 2. **Listar Produtos** - O(n)
- **Complexidade**: O(n) onde n é o número de produtos
- **Operação**: Itera sobre todos os produtos para exibição
- **Filtros**: Opção de filtrar por categoria
- **Saída**: Lista formatada com todos os dados

### 3. **Buscar Produto** - O(n)
- **Complexidade**: O(n) - busca linear
- **Operação**: Percorre a lista até encontrar o produto
- **Critério**: Busca por nome (case-insensitive)

### 4. **Atualizar Produto** - O(n)
- **Complexidade**: O(n) para busca + O(1) para atualização
- **Operação**: Localiza produto e atualiza campos específicos
- **Campos**: Preço (com suporte a vírgula), quantidade, categoria
- **Validação**: Mantém valores atuais se campo ficar em branco

### 5. **Remover Produto** - O(n)
- **Complexidade**: O(n) para busca + O(n) para remoção
- **Operação**: Remove produto da lista (deslocamento de elementos)
- **Confirmação**: Solicita confirmação antes de remover

### 6. **Relatório de Estoque** - O(n)
- **Complexidade**: O(n) para cálculos estatísticos
- **Operação**: Calcula estatísticas gerais do estoque
- **Métricas**: Total de produtos, valor total, produtos em destaque
- **Alertas**: Produtos com estoque baixo (< 10 unidades)

### 7. **Ordenar Produtos** - O(n log n)
- **Complexidade**: O(n log n) - algoritmo Timsort do Python
- **Critérios**: Nome, preço, quantidade, categoria
- **Operação**: Ordena lista in-place

### 8. **Carregar/Salvar Estoque** - O(n)
- **Complexidade**: O(n) para serialização/deserialização JSON
- **Operação**: Persistência em arquivo JSON
- **Formato**: Estrutura JSON com metadados
- **Segurança**: Alerta antes de recarregar com alterações não salvas

### 9. **Zerar Estoque** - O(1)
- **Complexidade**: O(1) - limpeza da lista
- **Operação**: Remove todos os produtos do estoque
- **Segurança**: Dupla confirmação obrigatória
- **Validação**: Verifica se estoque já está vazio

## 🏗️ Estrutura do Projeto

```
gerenciador-estoque/
├── main.py                 # Arquivo principal com todas as funções
├── estoque.json           # Arquivo de dados (criado automaticamente)
├── estoque_exemplo.json   # Arquivo de exemplo com dados de teste
├── teste_demonstracao.py  # Script para demonstrar complexidades
└── README.md              # Documentação do projeto
```

## 🎯 Análise de Complexidade

### **O(1) - Tempo Constante**
- **Adicionar produto**: Inserção no final da lista
- **Zerar estoque**: Limpeza da lista
- **Acesso por índice**: Operações diretas em listas

### **O(n) - Tempo Linear**
- **Listar produtos**: Percorre todos os produtos (com filtro opcional)
- **Buscar produto**: Busca linear na lista
- **Atualizar produto**: Busca + atualização
- **Remover produto**: Busca + remoção com deslocamento
- **Relatório**: Cálculos sobre todos os produtos
- **Carregar/Salvar**: Serialização JSON

### **O(n log n) - Tempo Logarítmico Linear**
- **Ordenar produtos**: Algoritmo de ordenação Timsort
- **Melhor caso**: O(n) para dados parcialmente ordenados
- **Pior caso**: O(n log n) para dados completamente desordenados

## 🚀 Como Executar

1. **Instalação**:
   ```bash
   # Não requer dependências externas
   # Apenas Python 3.6+ com bibliotecas padrão
   ```

2. **Execução**:
   ```bash
   python main.py
   ```

3. **Teste com dados de exemplo**:
   ```bash
   # Copie estoque_exemplo.json para estoque.json
   cp estoque_exemplo.json estoque.json
   python main.py
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

### **Estrutura de Dados**
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

### **Funcionalidades Avançadas**

#### **Entrada de Valores com Vírgula**
- Suporte a formato brasileiro: `7,99` → `7.99`
- Validação automática de formato
- Mensagens de erro claras

#### **Filtro por Categoria**
- Lista categorias disponíveis automaticamente
- Interface numerada para seleção
- Contadores de produtos exibidos vs. total

#### **Relatório Inteligente**
- Identifica produtos com estoque baixo (< 10 unidades)
- Estatísticas de produtos em destaque
- Alertas visuais para situações críticas

#### **Segurança de Dados**
- Alerta antes de recarregar estoque
- Opção de salvar alterações antes de descartar
- Confirmação para operações destrutivas
- **Zerar estoque**: Dupla confirmação obrigatória

#### **Zerar Estoque - Nova Funcionalidade**
- **Dupla confirmação**: Duas etapas de validação
- **Confirmação por palavra**: Deve digitar "ZERAR"
- **Contagem de produtos**: Mostra quantos serão removidos
- **Verificação inteligente**: Avisa se estoque já está vazio
- **Atualização automática**: Atualiza timestamp de modificação

### **Tratamento de Erros**
- Validação de entrada de dados
- Verificação de existência de arquivos
- Tratamento de exceções JSON
- Confirmações para operações destrutivas

### **Interface de Usuário**
- Menu interativo via terminal
- Formatação clara de saída
- Emojis para melhor experiência
- Mensagens de erro descritivas

## 📈 Considerações de Performance

### **Pontos de Melhoria**
1. **Busca**: Implementar busca binária para O(log n)
2. **Índices**: Usar dicionários para acesso O(1)
3. **Paginação**: Para listas muito grandes
4. **Cache**: Para operações frequentes

### **Limitações Atuais**
- Busca linear O(n) em vez de O(log n)
- Sem paginação para listas grandes
- Carregamento completo na memória
- Sem índices para busca rápida

## 🎓 Objetivos Acadêmicos Alcançados

✅ **Demonstração de complexidades**:
- O(1): Operações de inserção simples
- O(n): Operações de busca e iteração
- O(n log n): Operações de ordenação

✅ **Estruturas de dados**:
- Listas Python para armazenamento
- Dicionários para metadados
- JSON para persistência

✅ **Algoritmos implementados**:
- Busca linear
- Ordenação (Timsort)
- Cálculos estatísticos


## 🆕 Funcionalidades Adicionadas

### **Versão 2.0 - Melhorias**
- ✅ **Entrada com vírgula**: Suporte a formato brasileiro (7,99)
- ✅ **Filtro por categoria**: Listagem inteligente com filtros
- ✅ **Relatório aprimorado**: Alertas de estoque baixo
- ✅ **Segurança de dados**: Alerta antes de recarregar
- ✅ **Interface melhorada**: Mensagens mais claras e intuitivas

### **Versão 2.1 - Nova Funcionalidade**
- ✅ **Zerar estoque**: Remove todos os produtos com dupla confirmação
- ✅ **Segurança aprimorada**: Sistema de confirmação em duas etapas
- ✅ **Validação inteligente**: Verifica se estoque já está vazio

## 📝 Licença
Este projeto é de uso acadêmico e educacional.