select tbvendedor.nmvdd as vendedor,
	sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
	round(sum(tbvendas.qtd * tbvendas.vrunt) * tbvendedor.perccomissao/100,2) as comissao
from tbvendas
left join tbvendedor on tbvendas.cdvdd=tbvendedor.cdvdd
where tbvendas.status='Concluído'
group by tbvendedor.nmvdd
order by comissao desc