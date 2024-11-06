select tbestoqueproduto.cdpro, tbvendas.nmpro
from tbestoqueproduto
join tbvendas ON tbestoqueproduto.cdpro = tbvendas.cdpro
where tbvendas.status = 'Concluído'
  and tbvendas.dtven between '2014-02-03' and '2018-02-02'
group by tbestoqueproduto.cdpro, tbvendas.nmpro
order by count(tbvendas.cdven) desc
limit 1