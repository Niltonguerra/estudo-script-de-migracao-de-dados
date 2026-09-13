## para que serve o ruff?
O Ruff é um linter e formatador de código Python — ele garante que o código segue boas práticas de estilo e evita erros comuns.

Ele substitui várias ferramentas de uma vez só:

Ferramenta	O que fazia	Ruff substitui?
Flake8	Detecta erros e má práticas	✅
isort	Organiza imports	✅
autopep8	Formata o código	✅
pyupgrade	Moderniza sintaxe Python	✅

Os erros que ele apontou no seu projeto são exemplos práticos do que ele faz:

I001 — imports fora de ordem
F541 — f"string" sem variável dentro (desperdício)
F401 — import não utilizado (código morto)
F821 — variável usada sem estar definida (bug real)

A grande vantagem é que é extremamente rápido (escrito em Rust) e resolve tudo com um único ruff check . --fix. Projetos profissionais costumam rodá-lo no CI para bloquear código fora do padrão antes de entrar na branch principal.