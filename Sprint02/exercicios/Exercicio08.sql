select tbvendedor.cdvdd, tbvendedor.nmvdd
from tbvendedor
join tbvendas on tbvendedor.cdvdd=tbvendas.cdvdd
where tbvendas.status = 'Concluído'
group by tbvendedor.cdvdd, tbvendedor.nmvdd
order by COUNT(tbvendas.cdven) desc
limit 1