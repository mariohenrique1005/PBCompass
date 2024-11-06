select autor.codautor,autor.nome, count (livro.autor) as quantidade_publicacoes
from autor
left join livro on autor.codautor=livro.autor
group by autor.codautor, autor.nome
having count (livro.cod)= (
    select max (contador) 
    from (
        select count(livro.cod) as contador
        from autor
        join livro ON autor.codautor = livro.autor
        group by autor.codautor
    ) as subquery
)