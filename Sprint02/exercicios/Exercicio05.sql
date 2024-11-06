select distinct autor.nome
from autor
left JOIN livro on autor.codautor=livro.autor
left JOIN editora ON livro.editora=editora.codeditora
left JOIN endereco ON editora.endereco=endereco.codendereco
WHERE endereco.estado NOT IN ('PARANÁ','SANTA CATARINA','RIO GRANDE DO SUL')
order by autor.nome ASC