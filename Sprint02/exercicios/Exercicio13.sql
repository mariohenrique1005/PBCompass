select vendas.cdpro, vendas.nmcanalvendas, vendas.nmpro, sum(vendas.qtd) as quantidade_vendas
from tbvendas as vendas
where vendas.status = 'Concluído' and vendas.nmcanalvendas in ('Ecommerce', 'Matriz')
group by vendas.cdpro, vendas.nmcanalvendas, vendas.nmpro
order by quantidade_vendas asc
limit 10