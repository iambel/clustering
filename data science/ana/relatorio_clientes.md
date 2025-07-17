# Estratégia de Tratamento

## `geral`

após um consenso, foram removidas tabelas desnecessárias para a clusterizção e mantidas as seguintes tabelas:

| df_categorias | df_clientes | df_produtos | df_unidades | df_vendas | df_vendedores |
| :-----------: | ----------- | ----------- | ----------- | --------- | ------------- |

## `df_clientes.z`

na tabela `df_clientes.z` há várias tabelas nulas, parecem ser criptografadas. para facilitar as próximas tasks, optei pela remoção e mantendo somente as seguintes colunas:

| df_clientes.z >> | codigo | id_fiscal | nome | nome_fantasia | natureza_juridica | id_fiscal_2 | id_fiscal_3 | contribuinte_icms | pdc | vendedor | cst |
| :--------------: | ------ | --------- | ---- | ------------- | ----------------- | ----------- | ----------- | ----------------- | --- | -------- | --- |

passou a possuir **3132 rows × 11 columns**

colunas removidas: `'tidfiscs','ccnae','dnasc','itemt','iprz','ccrm1','nctx','ccrm2','nctx-2','ccrm3','ccrm4','nctx-4','nctx-4','nctx-5','ccrm6','nctx-6','crota','nctx-3','ccrm5','crota_idol'`

### obs.:

- logo após, foi feito o tratamento na coluna `vendedor`, ao que parece, os valores são os mesmos presentes na tabela `df_vendedor.z`. foi coletado os valores e aplicados por meio de uma função na tabela nos valores faltantes.

- coluna `crota_idol` foi removida por não acrescentar em nada a tabela, todos os valores eram 0.

- além disso, foi encontrado um valor nulo na coluna `id_fiscal` (CNPJ ou CPF), foi aplicado o valor 0 no local, por não conhecer o id do cliente.

- em relação a uniformização de categorias e formatos, todos estão legíveis, apenas as colunas `pdc` e `vendedor` foram passadas para o tipo `int64`.

---

## `comparação`

### pré-tratamento

#### leitura do arquivo `[clientes]`

| coluna            | valores nulos |
| ----------------- | ------------- |
| codigo            | 0             |
| id_fiscal         | 1             |
| nome              | 0             |
| nome_fantasia     | 0             |
| natureza_juridica | 0             |
| id_fiscal_2       | 0             |
| id_fiscal_3       | 0             |
| tidfiscs          | 3131          |
| contribuinte_icms | 0             |
| ccnae             | 3131          |
| dnasc             | 3124          |
| pdc               | 0             |
| itemt             | 3129          |
| iprz              | 3132          |
| ccrm1             | 3131          |
| nctx              | 3131          |
| ccrm2             | 3131          |
| nctx-2            | 3131          |
| ccrm3             | 3132          |
| nctx-3            | 3132          |
| ccrm4             | 3132          |
| nctx-4            | 3132          |
| ccrm5             | 3132          |
| nctx-5            | 3132          |
| ccrm6             | 3132          |
| nctx-6            | 3132          |
| crota             | 3132          |
| crota_idol        | 6             |
| vendedor          | 260           |
| cst               | 0             |

### pós-tratamento

#### leitura do arquivo `[clientes]`

| coluna            | valores nulos |
| ----------------- | ------------- |
| codigo            | 0             |
| id_fiscal         | 0             |
| nome              | 0             |
| nome_fantasia     | 0             |
| natureza_juridica | 0             |
| id_fiscal_2       | 0             |
| id_fiscal_3       | 0             |
| contribuinte_icms | 0             |
| pdc               | 0             |
| vendedor          | 0             |
| cst               | 0             |
