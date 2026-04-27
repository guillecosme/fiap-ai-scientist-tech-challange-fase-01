# Dicionário de dados

Base: `data/raw/desafio_nps_fase_1.csv` — 2.500 linhas, 19 colunas.

## Identificadores

| Coluna | Tipo | Descrição |
|---|---|---|
| `customer_id` | int | Identificador único do cliente |
| `order_id` | int | Identificador único do pedido |

## Cliente

| Coluna | Tipo | Descrição |
|---|---|---|
| `customer_age` | int | Idade do cliente |
| `customer_region` | str | Região geográfica (Norte, Nordeste, Centro-Oeste, Sudeste, Sul) |
| `customer_tenure_months` | int | Tempo de relacionamento com a empresa, em meses |

## Pedido

| Coluna | Tipo | Descrição |
|---|---|---|
| `order_value` | float | Valor total do pedido |
| `items_quantity` | int | Quantidade de itens no pedido |
| `discount_value` | float | Valor de desconto aplicado |
| `payment_installments` | int | Número de parcelas do pagamento |

## Logística

| Coluna | Tipo | Descrição |
|---|---|---|
| `delivery_time_days` | int | Tempo total de entrega (em dias) |
| `delivery_delay_days` | int | Quantidade de dias de atraso |
| `freight_value` | float | Valor do frete |
| `delivery_attempts` | int | Número de tentativas de entrega |

## Atendimento

| Coluna | Tipo | Descrição |
|---|---|---|
| `customer_service_contacts` | int | Número de contatos com atendimento |
| `resolution_time_days` | int | Tempo para resolução de problemas (em dias) |
| `complaints_count` | int | Número de reclamações registradas |

## Indicadores internos

| Coluna | Tipo | Descrição |
|---|---|---|
| `repeat_purchase_30d` | int (0/1) | Houve recompra em até 30 dias após o pedido |
| `csat_internal_score` | float | Score interno de satisfação |

## Target

| Coluna | Tipo | Descrição |
|---|---|---|
| `nps_score` | float | Nota de NPS (0 a 10), coletada após a experiência de compra |

## Observações iniciais (a confirmar na fase 2)

- O `nps_score` aparece como **float** no CSV (ex.: 6.9, 2.4) — preciso verificar se é nota fracionada de fato ou se houve algum tratamento prévio. NPS canônico é inteiro de 0 a 10.
- `csat_internal_score` também é float, mas escala não está explícita no enunciado — checar range observado.
- `customer_service_contacts = 0` aparece em registros com `resolution_time_days > 0` — verificar consistência.
