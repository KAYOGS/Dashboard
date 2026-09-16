# Como o Dashboard_v3 funciona

O arquivo principal atual é `Dashboard_v3.pbix`. O `Dashboard_v2.pbix` foi mantido como versão anterior.

## Base de dados

O painel utiliza duas estruturas de dados incorporadas no PBIX:

1. O histórico diário do arquivo `db_historico_precos.csv`, com 3.750 registros, cinco empresas e datas entre 04/09/2023 e 04/09/2026.
2. Uma tabela anual de fundamentos, com 20 registros, formada por cinco empresas nos anos de 2023, 2024, 2025 e 2026.

O CSV original repete a mesma fotografia de P/L, P/VP, ROE, ROA e Dividend Yield em todas as datas de cada empresa. Por isso, essas colunas não foram usadas para construir a evolução anual. A série anual utiliza os resultados contábeis e as cotações correspondentes a cada período.

## Empresas analisadas

| Código | Empresa | Atividade principal |
|---|---|---|
| KLBN11 | Klabin | Papel, celulose e embalagens |
| LREN3 | Lojas Renner | Varejo de moda |
| MGLU3 | Magazine Luiza | Varejo geral |
| POSI3 | Positivo Tecnologia | Equipamentos e infraestrutura de tecnologia |
| TOTS3 | TOTVS | Software e serviços de tecnologia |

As cinco empresas não pertencem ao mesmo ramo. Os resultados servem para observar diferenças financeiras entre empresas e setores. Não representam uma comparação direta entre concorrentes equivalentes.

## Períodos

- **2023, 2024 e 2025:** resultado do exercício, balanço de encerramento e preço do último pregão do ano.
- **2026:** lucro e proventos dos 12 meses entre julho de 2025 e junho de 2026, com balanço e preço de 30/06/2026.

O período de 2026 é TTM, ou seja, doze meses móveis. Ele não representa o exercício completo de 2026. Os resultados de 2025 e 2026 compartilham seis meses de dados.

## Cálculos

O valor de mercado aproximado é calculado pela multiplicação do preço de fechamento pela quantidade de papéis equivalentes. Para KLBN11 foi aplicada a proporção de cinco ações por unit.

### P/L

`Valor de mercado ÷ lucro da controladora`

Indica quanto o mercado atribui de valor para cada unidade de lucro. Quando o lucro é negativo ou zero, o indicador fica em branco.

### P/VP

`Valor de mercado ÷ patrimônio líquido da controladora`

Compara o valor de mercado com o patrimônio líquido contábil da empresa.

### ROE

`Lucro da controladora ÷ patrimônio líquido da controladora`

Mede o retorno contábil obtido sobre o patrimônio dos acionistas.

### ROA

`Lucro consolidado, incluindo não controladores ÷ ativo total`

Mede o retorno contábil produzido pelos ativos da empresa.

### Dividend Yield

`Proventos por papel nos 12 meses ÷ preço de fechamento do período`

Os proventos são agrupados pela data ex. O resultado é uma aproximação e pode não coincidir com o fluxo efetivamente recebido no mesmo ano.

P/L e P/VP são formatados como múltiplos. ROE, ROA e Dividend Yield são formatados como percentuais.

## Indicadores complementares

A página **Balanço e despesas** utiliza também os campos já existentes na base diária:

- `LiquidezCorrente`: indicador de capacidade de pagamento no curto prazo;
- `Divida_Patrimonio`: relação entre dívida e patrimônio;
- `PVP`: preço em relação ao valor patrimonial;
- `MargemOperacional%`: margem obtida pelas operações da empresa;
- `MargemLiquida%`: parcela da receita convertida em resultado líquido;
- `ROE%`: retorno sobre o patrimônio;
- `ROA%`: retorno sobre os ativos;
- `Date` e `Close`: data e preço de fechamento usados no histórico de preços.

Como os indicadores fundamentalistas da base diária se repetem ao longo das datas de cada empresa, os gráficos comparativos usam um valor representativo por companhia, evitando a soma incorreta dessas métricas.

## Filtros e medidas

Os filtros de empresa e ano controlam os cartões, a tabela e os gráficos.

Nos cartões, a medida utiliza o maior ano selecionado. Sem seleção de ano, o resultado exibido é o de 2026. Quando apenas uma empresa está selecionada, aparece o indicador dessa empresa. Quando várias empresas estão selecionadas, aparece a mediana. A mediana evita a soma incorreta de múltiplos e percentuais.

Nos gráficos de evolução, cada ponto utiliza o indicador da empresa e do ano correspondente. No gráfico de preços, cada período mostra o fechamento do último pregão disponível.

## Páginas

### Visão geral

Contém cinco cartões, uma tabela com os indicadores das empresas e um gráfico de barras de ROE. Essa página resume o último ano selecionado.

### Evolução 2023–2026

Contém cinco gráficos de linha, um para cada indicador. As empresas aparecem como séries separadas.

### Preços da planilha

Contém o histórico de fechamento da empresa selecionada e uma tabela diária. O usuário pode expandir a data de ano para trimestre, mês e dia.

### Balanço e despesas

Página adicionada no `Dashboard_v3.pbix`, composta por:

- gráfico de balanço patrimonial com liquidez corrente, dívida sobre patrimônio e P/VP por empresa;
- gráfico de despesas e lucro com margem operacional, margem líquida, ROE e ROA por empresa;
- gráfico de linha com o preço de fechamento por data;
- filtro de empresa aplicado às visualizações da página.

Essa página reúne, em uma única visão, indicadores de saúde financeira, rentabilidade e comportamento do preço das ações.

## Limitações

- As empresas são de setores diferentes.
- A série diária começa em setembro de 2023 e termina em setembro de 2026.
- O período fundamentalista de 2026 termina em junho.
- Os dados complementares foram obtidos pelo Yahoo Finance e não passaram por reconciliação independente integral com a CVM.
- O cálculo de KLBN11 utiliza uma aproximação para converter ações em units.
- Os dados podem ter sido reapresentados posteriormente pelo fornecedor.

O dashboard é adequado para a atividade acadêmica e para análise exploratória. Ele não deve ser apresentado como recomendação de investimento ou como base contábil auditada.
