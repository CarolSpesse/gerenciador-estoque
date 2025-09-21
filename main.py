#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime


class GerenciadorEstoque:
     
    def __init__(self, arquivo_estoque: str = "estoque.json"):
        """
        Inicializa o gerenciador de estoque.
        
        Args:
            arquivo_estoque (str): Caminho para o arquivo JSON de estoque
        """
        self.arquivo_estoque = arquivo_estoque
        self.estoque = self.carregar_estoque()
    
    def carregar_estoque(self) -> Dict[str, Any]:
        """
        Carrega os dados do estoque do arquivo JSON.
        
        Complexidade: O(n) onde n é o número de produtos no arquivo
        - Leitura do arquivo: O(1)
        - Parsing JSON: O(n) onde n é o tamanho do arquivo
        
        Returns:
            Dict contendo os dados do estoque
        """
        try:
            if os.path.exists(self.arquivo_estoque):
                with open(self.arquivo_estoque, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    print(f"✅ Estoque carregado com sucesso! {len(dados.get('produtos', []))} produtos encontrados.")
                    return dados
            else:
                print("📁 Arquivo de estoque não encontrado. Criando novo estoque...")
                return {"produtos": [], "ultima_atualizacao": datetime.now().isoformat()}
        except Exception as e:
            print(f"❌ Erro ao carregar estoque: {e}")
            return {"produtos": [], "ultima_atualizacao": datetime.now().isoformat()}
    
    def salvar_estoque(self) -> bool:
        """
        Salva os dados do estoque no arquivo JSON.
        
        Complexidade: O(n) onde n é o número de produtos
        - Serialização JSON: O(n)
        - Escrita no arquivo: O(n)
        
        Returns:
            bool: True se salvou com sucesso, False caso contrário
        """
        try:
            self.estoque["ultima_atualizacao"] = datetime.now().isoformat()
            with open(self.arquivo_estoque, 'w', encoding='utf-8') as arquivo:
                json.dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
            print("💾 Estoque salvo com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao salvar estoque: {e}")
            return False
    
    def _converter_preco(self, preco_str: str) -> float:
        """
        Converte string de preço com vírgula para float.
        
        Args:
            preco_str (str): String do preço (ex: "7,99" ou "7.99")
            
        Returns:
            float: Preço convertido
        """
        try:
            preco_str = preco_str.replace(",", ".")
            return float(preco_str)
        except ValueError:
            raise ValueError("Formato de preço inválido")

    def adicionar_produto(self) -> bool:
        """
        Adiciona um novo produto ao estoque.
        
        Complexidade: O(1) - inserção no final da lista
        - Verificação de duplicatas: O(n) no pior caso
        - Inserção na lista: O(1)
        
        Returns:
            bool: True se adicionou com sucesso, False caso contrário
        """
        print("\n📦 ADICIONAR NOVO PRODUTO")
        print("-" * 30)
        
        try:
            nome = input("Nome do produto: ").strip()
            if not nome:
                print("❌ Nome do produto não pode estar vazio!")
                return False
            
            for produto in self.estoque["produtos"]:
                if produto["nome"].lower() == nome.lower():
                    print(f"❌ Produto '{nome}' já existe no estoque!")
                    return False
            
            preco_str = input("Preço unitário (R$ dd, ex: 7,99): ").strip()
            preco = self._converter_preco(preco_str)
            if preco < 0:
                print("❌ Preço não pode ser negativo!")
                return False
            
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade < 0:
                print("❌ Quantidade não pode ser negativa!")
                return False
            
            categoria = input("Categoria (opcional): ").strip()
            
            novo_produto = {
                "id": len(self.estoque["produtos"]) + 1,
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade,
                "categoria": categoria or "Sem categoria",
                "data_cadastro": datetime.now().isoformat()
            }
            
            self.estoque["produtos"].append(novo_produto)
            
            print(f"✅ Produto '{nome}' adicionado com sucesso!")
            print(f"   Preço: R$ {preco:.2f}")
            print(f"   Quantidade: {quantidade}")
            print(f"   Categoria: {categoria or 'Sem categoria'}")
            
            return True
            
        except ValueError as e:
            print(f"❌ Erro: {e}")
            return False
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return False
    
    def listar_produtos(self) -> None:
        """
        Lista todos os produtos do estoque com opção de filtro por categoria.
        
        Complexidade: O(n) onde n é o número de produtos
        - Iteração sobre todos os produtos: O(n)
        - Filtro por categoria: O(n)
        - Formatação de saída: O(n)
        
        """
        print("\n📋 LISTA DE PRODUTOS")
        print("=" * 80)
        
        if not self.estoque["produtos"]:
            print("📭 Nenhum produto cadastrado no estoque.")
            return
        
        print("1. Listar todos os produtos")
        print("2. Filtrar por categoria")
        
        try:
            opcao = int(input("Escolha uma opção (1-2): "))
            
            produtos_para_exibir = self.estoque["produtos"]
            
            if opcao == 2:
                categorias = list(set(produto["categoria"] for produto in self.estoque["produtos"]))
                categorias.sort()
                
                print(f"\nCategorias disponíveis:")
                for i, categoria in enumerate(categorias, 1):
                    print(f"{i}. {categoria}")
                
                try:
                    cat_opcao = int(input("Escolha a categoria (número): "))
                    if 1 <= cat_opcao <= len(categorias):
                        categoria_escolhida = categorias[cat_opcao - 1]
                        produtos_para_exibir = [p for p in self.estoque["produtos"] 
                                              if p["categoria"] == categoria_escolhida]
                        print(f"\n🔍 Filtrando por categoria: {categoria_escolhida}")
                    else:
                        print("❌ Opção inválida! Listando todos os produtos.")
                except ValueError:
                    print("❌ Opção inválida! Listando todos os produtos.")
            elif opcao != 1:
                print("❌ Opção inválida! Listando todos os produtos.")
                
        except ValueError:
            print("❌ Opção inválida! Listando todos os produtos.")
        
        if not produtos_para_exibir:
            print("📭 Nenhum produto encontrado com os critérios selecionados.")
            return
        
        print(f"\n{'ID':<4} {'Nome':<20} {'Preço':<12} {'Qtd':<6} {'Categoria':<15} {'Data Cadastro'}")
        print("-" * 80)
        
        for produto in produtos_para_exibir:
            data_cadastro = produto["data_cadastro"][:10]  # Apenas a data
            print(f"{produto['id']:<4} {produto['nome']:<20} R$ {produto['preco']:<10.2f} "
                  f"{produto['quantidade']:<6} {produto['categoria']:<15} {data_cadastro}")
        
        print(f"\n📊 Total de produtos exibidos: {len(produtos_para_exibir)}")
        if len(produtos_para_exibir) != len(self.estoque["produtos"]):
            print(f"📊 Total de produtos no estoque: {len(self.estoque['produtos'])}")
    
    def buscar_produto(self, nome: str = None) -> Optional[Dict[str, Any]]:
        """
        Busca um produto pelo nome.
        
        Complexidade: O(n) onde n é o número de produtos
        - Busca linear: O(n) no pior caso
        - Comparação de strings: O(k) onde k é o tamanho da string
        
        Args:
            nome (str, optional): Nome do produto a buscar
            
        Returns:
            Dict do produto encontrado ou None se não encontrado
        """
        if nome is None:
            print("\n🔍 BUSCAR PRODUTO")
            print("-" * 20)
            nome = input("Digite o nome do produto: ").strip()
        
        if not nome:
            print("❌ Nome do produto não pode estar vazio!")
            return None
        
        for produto in self.estoque["produtos"]:
            if produto["nome"].lower() == nome.lower():
                print(f"\n✅ Produto encontrado:")
                print(f"   ID: {produto['id']}")
                print(f"   Nome: {produto['nome']}")
                print(f"   Preço: R$ {produto['preco']:.2f}")
                print(f"   Quantidade: {produto['quantidade']}")
                print(f"   Categoria: {produto['categoria']}")
                print(f"   Data de cadastro: {produto['data_cadastro'][:10]}")
                return produto
        
        print(f"❌ Produto '{nome}' não encontrado no estoque.")
        return None
    
    def atualizar_produto(self) -> bool:
        """
        Atualiza informações de um produto existente.
        
        Complexidade: O(n) onde n é o número de produtos
        - Busca do produto: O(n)
        - Atualização: O(1)
        
        Returns:
            bool: True se atualizou com sucesso, False caso contrário
        """
        print("\n✏️ ATUALIZAR PRODUTO")
        print("-" * 20)
        
        nome = input("Digite o nome do produto a atualizar: ").strip()
        if not nome:
            print("❌ Nome do produto não pode estar vazio!")
            return False
        
        produto = None
        for p in self.estoque["produtos"]:
            if p["nome"].lower() == nome.lower():
                produto = p
                break
        
        if not produto:
            print(f"❌ Produto '{nome}' não encontrado!")
            return False
        
        print(f"\nProduto encontrado: {produto['nome']}")
        print("Deixe em branco para manter o valor atual.")
        
        try:
            novo_preco = input(f"Novo preço (atual: R$ {produto['preco']:.2f} dd): ").strip()
            if novo_preco:
                preco = self._converter_preco(novo_preco)
                if preco < 0:
                    print("❌ Preço não pode ser negativo!")
                    return False
                produto["preco"] = preco
            
            nova_quantidade = input(f"Nova quantidade (atual: {produto['quantidade']}): ").strip()
            if nova_quantidade:
                quantidade = int(nova_quantidade)
                if quantidade < 0:
                    print("❌ Quantidade não pode ser negativa!")
                    return False
                produto["quantidade"] = quantidade
            
            nova_categoria = input(f"Nova categoria (atual: {produto['categoria']}): ").strip()
            if nova_categoria:
                produto["categoria"] = nova_categoria
            
            print(f"✅ Produto '{produto['nome']}' atualizado com sucesso!")
            return True
            
        except ValueError:
            print("❌ Erro: Preço e quantidade devem ser números válidos!")
            return False
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return False
    
    def remover_produto(self) -> bool:
        """
        Remove um produto do estoque.
        
        Complexidade: O(n) onde n é o número de produtos
        - Busca do produto: O(n)
        - Remoção da lista: O(n) no pior caso (deslocamento de elementos)
        
        Returns:
            bool: True se removeu com sucesso, False caso contrário
        """
        print("\n🗑️ REMOVER PRODUTO")
        print("-" * 18)
        
        nome = input("Digite o nome do produto a remover: ").strip()
        if not nome:
            print("❌ Nome do produto não pode estar vazio!")
            return False
        
        for i, produto in enumerate(self.estoque["produtos"]):
            if produto["nome"].lower() == nome.lower():
                confirmacao = input(f"Tem certeza que deseja remover '{produto['nome']}'? (s/n): ").lower()
                if confirmacao in ['s', 'sim', 'y', 'yes']:
                    produto_removido = self.estoque["produtos"].pop(i)
                    print(f"✅ Produto '{produto_removido['nome']}' removido com sucesso!")
                    return True
                else:
                    print("❌ Operação cancelada.")
                    return False
        
        print(f"❌ Produto '{nome}' não encontrado!")
        return False
    
    def relatorio_estoque(self) -> None:
        """
        Gera um relatório completo do estoque.
        
        Complexidade: O(n) onde n é o número de produtos
        - Iteração sobre todos os produtos: O(n)
        - Cálculos estatísticos: O(n)
        
        """
        print("\n📊 RELATÓRIO DO ESTOQUE")
        print("=" * 50)
        
        if not self.estoque["produtos"]:
            print("📭 Nenhum produto cadastrado no estoque.")
            return
        
        produtos = self.estoque["produtos"]
        total_produtos = len(produtos)
        total_valor = sum(p["preco"] * p["quantidade"] for p in produtos)
        total_quantidade = sum(p["quantidade"] for p in produtos)
        
        produto_maior_preco = max(produtos, key=lambda p: p["preco"])
        produto_menor_preco = min(produtos, key=lambda p: p["preco"])
        produto_maior_qtd = max(produtos, key=lambda p: p["quantidade"])
        
        print(f"📈 Estatísticas Gerais:")
        print(f"   Total de produtos: {total_produtos}")
        print(f"   Total de itens em estoque: {total_quantidade}")
        print(f"   Valor total do estoque: R$ {total_valor:.2f}")
        
        print(f"\n🏆 Produtos em Destaque:")
        print(f"   Maior preço: {produto_maior_preco['nome']} - R$ {produto_maior_preco['preco']:.2f}")
        print(f"   Menor preço: {produto_menor_preco['nome']} - R$ {produto_menor_preco['preco']:.2f}")
        print(f"   Maior quantidade: {produto_maior_qtd['nome']} - {produto_maior_qtd['quantidade']} unidades")
        
        estoque_baixo = [p for p in produtos if p["quantidade"] < 10]
        if estoque_baixo:
            print(f"\n⚠️ Produtos com estoque baixo (< 10 unidades):")
            for produto in estoque_baixo:
                print(f"   - {produto['nome']}: {produto['quantidade']} unidades")
        else:
            print(f"\n✅ Todos os produtos estão com estoque adequado (≥ 10 unidades)")
        
        print(f"\n📅 Última atualização: {self.estoque['ultima_atualizacao'][:19]}")
    
    def ordenar_produtos(self) -> None:
        """
        Ordena os produtos por diferentes critérios.
        
        Complexidade: O(n log n) onde n é o número de produtos
        - Algoritmo de ordenação (Timsort): O(n log n)
        
        """
        print("\n🔄 ORDENAR PRODUTOS")
        print("-" * 20)
        print("1. Por nome (A-Z)")
        print("2. Por preço (menor para maior)")
        print("3. Por quantidade (maior para menor)")
        print("4. Por categoria (A-Z)")
        
        try:
            opcao = int(input("Escolha o critério de ordenação (1-4): "))
            
            if opcao == 1:
                self.estoque["produtos"].sort(key=lambda p: p["nome"].lower())
                print("✅ Produtos ordenados por nome (A-Z)")
            elif opcao == 2:
                self.estoque["produtos"].sort(key=lambda p: p["preco"])
                print("✅ Produtos ordenados por preço (menor para maior)")
            elif opcao == 3:
                self.estoque["produtos"].sort(key=lambda p: p["quantidade"], reverse=True)
                print("✅ Produtos ordenados por quantidade (maior para menor)")
            elif opcao == 4:
                self.estoque["produtos"].sort(key=lambda p: p["categoria"].lower())
                print("✅ Produtos ordenados por categoria (A-Z)")
            else:
                print("❌ Opção inválida!")
                return
            
            self.listar_produtos()
            
        except ValueError:
            print("❌ Opção deve ser um número válido!")
    
    def zerar_estoque(self) -> bool:
        """
        Remove todos os produtos do estoque.
        
        Complexidade: O(1) - limpeza da lista
        - Operação de limpeza: O(1)
        
        Returns:
            bool: True se zerou com sucesso, False caso contrário
        """
        print("\n🗑️ ZERAR ESTOQUE")
        print("-" * 20)
        
        if not self.estoque["produtos"]:
            print("📭 O estoque já está vazio!")
            return True
        
        total_produtos = len(self.estoque["produtos"])
        print(f"⚠️ ATENÇÃO: Esta operação irá remover TODOS os {total_produtos} produtos do estoque!")
        print("Esta ação NÃO pode ser desfeita!")
        
        confirmacao1 = input("Tem certeza que deseja zerar o estoque? (s/n): ").lower()
        if confirmacao1 not in ['s', 'sim', 'y', 'yes']:
            print("❌ Operação cancelada.")
            return False
        
        print(f"\n⚠️ ÚLTIMA CONFIRMAÇÃO: Digite 'ZERAR' para confirmar a remoção de {total_produtos} produtos:")
        confirmacao2 = input("Digite 'ZERAR' para confirmar: ").strip()
        
        if confirmacao2.upper() != 'ZERAR':
            print("❌ Confirmação incorreta. Operação cancelada.")
            return False
        
        # Zerar estoque - O(1)
        self.estoque["produtos"] = []
        self.estoque["ultima_atualizacao"] = datetime.now().isoformat()
        
        print(f"✅ Estoque zerado com sucesso! {total_produtos} produtos removidos.")
        return True
    
    def menu(self) -> None:
        """
        Exibe o menu principal e gerencia as operações.
        
        Complexidade: O(1) para cada operação do menu
        - A complexidade real depende da operação escolhida
        
        """
        while True:
            print("\n" + "="*50)
            print("🏪 GERENCIADOR DE ESTOQUE - MENU PRINCIPAL")
            print("="*50)
            print("1. 📦 Adicionar produto")
            print("2. 📋 Listar produtos")
            print("3. 🔍 Buscar produto")
            print("4. ✏️ Atualizar produto")
            print("5. 🗑️ Remover produto")
            print("6. 📊 Gerar relatório")
            print("7. 🔄 Ordenar produtos")
            print("8. 💾 Salvar estoque")
            print("9. 🔄 Recarregar estoque")
            print("10. 🗑️ Zerar estoque")
            print("0. 🚪 Sair")
            print("-"*50)
            
            try:
                opcao = int(input("Escolha uma opção: "))
                
                if opcao == 1:
                    self.adicionar_produto()
                elif opcao == 2:
                    self.listar_produtos()
                elif opcao == 3:
                    self.buscar_produto()
                elif opcao == 4:
                    self.atualizar_produto()
                elif opcao == 5:
                    self.remover_produto()
                elif opcao == 6:
                    self.relatorio_estoque()
                elif opcao == 7:
                    self.ordenar_produtos()
                elif opcao == 8:
                    self.salvar_estoque()
                elif opcao == 9:
                    print("\n⚠️ ATENÇÃO: Recarregar o estoque descartará todas as alterações não salvas!")
                    confirmacao = input("Deseja salvar as alterações antes de recarregar? (s/n): ").lower()
                    
                    if confirmacao in ['s', 'sim', 'y', 'yes']:
                        if self.salvar_estoque():
                            print("✅ Alterações salvas com sucesso!")
                        else:
                            print("❌ Erro ao salvar. Continuando com recarregamento...")
                    elif confirmacao in ['n', 'não', 'nao', 'no']:
                        print("⚠️ Alterações serão descartadas!")
                    else:
                        print("❌ Opção inválida! Operação cancelada.")
                        continue
                    
                    self.estoque = self.carregar_estoque()
                elif opcao == 10:
                    self.zerar_estoque()
                elif opcao == 0:
                    print("\n💾 Salvando estoque antes de sair...")
                    self.salvar_estoque()
                    print("👋 Obrigado por usar o Gerenciador de Estoque!")
                    break
                else:
                    print("❌ Opção inválida! Escolha entre 0 e 10.")
                    
            except ValueError:
                print("❌ Digite um número válido!")
            except KeyboardInterrupt:
                print("\n\n👋 Operação cancelada pelo usuário. Até logo!")
                break
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")


def main():
    """
    Função principal do programa.
    """
    print("Bem-vindo ao Gerenciador de Estoque!")
    print("="*60)
    
    gerenciador = GerenciadorEstoque()
    gerenciador.menu()


if __name__ == "__main__":
    main()
