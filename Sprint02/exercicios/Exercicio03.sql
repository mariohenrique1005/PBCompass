select count (livro.titulo) as quantidade, editora.nome, endereco.estado, endereco.cidade
from livro
join editora on livro.editora = codeditora
join endereco on editora.endereco = codendereco
group by editora.nome, endereco.estado, endereco.cidade
order by quantidade desc
limit 5