with VendasConcluidas as(
    select estado, vrunt * qtd as valor_total
    from tbvendas
    where status = 'Concluído'
)
select estado, round(avg(valor_total), 2) as gastomedio
from VendasConcluidas
group by estado
order by gastomedio desc