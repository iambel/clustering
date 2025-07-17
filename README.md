<div align="center">

# Clusterização de Clientes por Comportamento de Compra - UNIGEX

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/Scikit--Learn-Clustering-orange)
![KMeans](https://img.shields.io/badge/K--Means-Algoritmo-blue)
![PCA](https://img.shields.io/badge/PCA-Visualização-ff69b4)

|           ÍNDICE            |
| :-------------------------: |
| [Visão Geral](#visão-geral) |
|   [Estrutura](#estrutura)   |
| [Tecnologias](#tecnologias) |
| [Metodologia](#metodologia) |
| [Entregáveis](#entregáveis) |

</div>

## Visão Geral

Este projeto tem como objetivo segmentar clientes da plataforma **UNIGEX** com base em seus padrões de compra, por meio de técnicas de **clusterização não supervisionada**. A análise foi desenvolvida em colaboração com a **UECE (Universidade Estadual do Ceará)**, visando identificar **grupos de clientes com comportamentos de consumo semelhantes**, de forma a subsidiar estratégias de marketing mais direcionadas e personalizadas.

## Estrutura

```
├── 📂 data science
│   ├── 📂 ana # pasta com os notebooks de ana
│   ├── 📂 ariel # pasta com os notebooks de ariel
│   ├── 📂 eliza # pasta com os notebooks de eliza
│   ├── 📂 erivando # pasta com os notebooks de erivando
└── 📂 util # recursos compartilhados
    ├── 📂 data # dados brutos
    ├── 📂 document # toda documentação técnica do projeto
    │   ├── 📄 Doc 1 Escopo Completo Projeto 5 - Unigex.pdf
    │   ├── 📄 Doc 2 Escopo de Aprovação 18_UNIGEX_CLUSTER_Projeto05.pdf
    │   ├── 📄 Relatório_Equipe_9_2.pdf # relatório final entregue
    │   └── 📄 Slides da apresentação.pdf
    └── 📄 README.md # readme geral do projeto

```

## Tecnologias

### Pré-processamento e Análise

- `Python`
- `pandas` e `numpy` para organização dos dados
- Normalização e tratamento de variáveis numéricas

### Algoritmos de Clusterização

- `K-Means`
- `DBSCAN`
- `Agglomerative Clustering` como algoritmo para comparação adicional

### Visualização e Avaliação

- Redução de dimensionalidade com `PCA` para visualização dos grupos
- Validação dos clusters com **Silhouette Score**

## Metodologia

1. **Coleta e Análise de Dados**: Extração de dados de vendas do sistema WEBGEX
2. **Pré-processamento**: Seleção de variáveis como frequência, valor de compra e categorias
3. **Clusterização**: Aplicação de pelo menos 3 algoritmos de agrupamento
4. **Visualização dos Grupos**: Uso de PCA para representar clusters em 2D
5. **Validação dos Resultados**: Métricas de coesão e separação (Silhouette)

## Entregáveis

- Scripts de segmentação e visualização
- Comparação entre diferentes algoritmos de clusterização
- Relatório com insights sobre perfis de clientes
- Recomendações de ações de marketing por segmento

---

<div align="center">

Fique à vontade para abrir uma _issue_ ou entrar em contato.

<img src="https://c.tenor.com/cDsTyrhlS94AAAAC/tenor.gif">

</div>
