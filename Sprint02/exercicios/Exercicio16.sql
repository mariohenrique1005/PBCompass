WITH vendas_concluidas AS (
    SELECT estado, nmpro, qtd
    FROM tbvendas
    WHERE status = 'Concluído'
)
SELECT estado, nmpro, ROUND(AVG(qtd), 4) AS quantidade_media
FROM vendas_concluidas
GROUP BY estado, nmpro
ORDER BY estado ASC, nmpro ASC