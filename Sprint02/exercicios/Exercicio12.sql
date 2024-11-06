WITH total_vendas_vendedor AS (
    SELECT cdvdd, SUM(qtd * vrunt) AS valor_total_vendas
    FROM tbvendas
    WHERE status='Concluído'
    GROUP BY cdvdd
    HAVING SUM(qtd * vrunt) > 0
    ORDER BY valor_total_vendas ASC
    LIMIT 1
)
SELECT tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc, total_vendas_vendedor.valor_total_vendas
FROM tbdependente
JOIN total_vendas_vendedor ON tbdependente.cdvdd = total_vendas_vendedor.cdvdd