# Pràctica 5: Indexes & Explain/Analyze

La pràctica consisteix en entendre que són els indexes i en crear-ne alguns. Per entendre el seu funcionament, també es revisarà la comanda `explain analyze` de PostgreSQL

## 1. Planner

Consulta l'enllaç següent i explica, amb les teves pròpies paraules, que és el *planner* de PostgreSQL.

* https://www.postgresql.org/docs/12/planner-optimizer.html

## 2. Explain/Analyze

Consulta els enllaços següents i defineix, **amb les teves pròpies paraules**, que fa la comanda `explain` y que s'obté quan s'afegeix l'opció `analyze` a aquesta comanda.

* https://www.postgresql.org/docs/12/sql-explain.html
* https://thoughtbot.com/blog/reading-an-explain-analyze-query-plan

## 3. Exemple d'explain analyze

Executa la query següent sobre la teva base de dades, que t'hauria de mostrar 16 resultats:`select salary, from_date from salaries where emp_id = 400432;` 

* Què retorna aquesta consulta?

* Executa ara l'ordre `explain analyze select salary, from_date from salaries where emp_id = 400432`. Quina informació obtens? Tracta d'explicar quina informació es mostra. Fes servir la web https://explain.dalibo.com/ per tractar d'entendre que significa la part on diu *Seq Scan* 

## 4. Definició d'index

Consulta els enllaços següents i defineix, **amb les teves pròpies paraules**, que és un index, per a que serveix, quins avantatges té i quins inconvenients pot tenir:

* https://www.tutorialspoint.com/postgresql/postgresql_indexes.htm
* https://www.postgresql.org/docs/12/indexes.html

## 5. Creació d'un índex y revisar la query anteruir

` create index salaries_id on salaries(emp_id);`


## 6. Tipus d'indexes

https://www.enterprisedb.com/postgres-tutorials/overview-postgresql-indexes

## 7. Sintaxis de com crear un index y com esborrarlo

## 8. Un altre explain analyze

## 9. Index parcial

## 10. Explain analyze amb l'index anterior


