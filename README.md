# Dashboard financeiro 2023–2026

O arquivo principal é **Dashboard_v2.pbix**. Abra-o no Power BI Desktop para consultar e editar o painel.

## Conteúdo

O dashboard analisa cinco empresas presentes no CSV fornecido:

- KLBN11 — papel, celulose e embalagens;
- LREN3 — varejo de moda;
- MGLU3 — varejo geral;
- POSI3 — equipamentos e infraestrutura de tecnologia;
- TOTS3 — software e serviços de tecnologia.

As empresas são de setores diferentes. A comparação deve ser interpretada como uma análise entre empresas, não como comparação de concorrentes do mesmo ramo.

O período analisado é **2023, 2024, 2025 e 2026**. Os dados de 2026 representam os 12 meses encerrados em junho de 2026. A série diária original vai de 04/09/2023 a 04/09/2026, portanto 2023 e 2026 aparecem parcialmente no gráfico de preços.

## Indicadores

O painel utiliza somente cinco indicadores fundamentalistas:

| Indicador | Cálculo |
|---|---|
| P/L | Valor de mercado ÷ lucro da controladora |
| P/VP | Valor de mercado ÷ patrimônio líquido da controladora |
| ROE | Lucro da controladora ÷ patrimônio líquido da controladora |
| ROA | Lucro consolidado ÷ ativo total |
| Dividend Yield | Proventos por papel ÷ preço de fechamento |

P/L e P/VP são exibidos como múltiplos. ROE, ROA e Dividend Yield são exibidos como percentuais. O P/L fica em branco quando a empresa apresenta prejuízo ou lucro igual a zero.

## Funcionamento das páginas

### Visão geral

Mostra os cinco indicadores em cartões, uma tabela comparativa e um gráfico de ROE por empresa. Os filtros permitem selecionar empresa e ano.

Sem filtro de ano, os cartões utilizam 2026. Quando várias empresas estão selecionadas, os cartões mostram a mediana dos valores. Os indicadores não são somados.

### Evolução 2023–2026

Apresenta um gráfico de linha para cada indicador. O eixo horizontal contém os quatro anos e cada empresa aparece como uma série separada.

### Preços da planilha

Utiliza o histórico diário do CSV original. Selecione uma empresa para visualizar o preço de fechamento. A hierarquia de data permite navegar por ano, trimestre, mês e dia.

## Arquivos da pasta

- `Dashboard_v2.pbix`: dashboard atual;
- `Dashboard.pbix`: arquivo original;
- `planilha com dados organizados.pbix`: base organizada original;
- `db_historico_precos.csv`: CSV original;
- `metricas_analise.pdf`: enunciado da atividade;
- `COMO_FUNCIONA.md`: documentação detalhada dos dados e cálculos;
- `importarDados.py`: script original de coleta.

Para levar o trabalho a outro computador e apenas abrir ou editar o painel, copie `Dashboard_v2.pbix`. Os dados utilizados já estão incorporados no arquivo.
