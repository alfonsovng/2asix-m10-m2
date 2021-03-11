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

Executa la query següent sobre la teva base de dades, que t'hauria de mostrar 16 resultats: `select salary, from_date from salaries where emp_id = 400432;` 

* Què retorna aquesta consulta?

* Executa ara l'ordre `explain analyze select salary, from_date from salaries where emp_id = 400432`. Quina informació obtens? Tracta d'explicar quina informació es mostra. Fes servir la web https://explain.dalibo.com/ per tractar d'entendre que significa la part on diu *Seq Scan* 

## 4. Definició d'index

Consulta els enllaços següents i defineix, **amb les teves pròpies paraules**, que és un index, per a que serveix, quins avantatges té i quins inconvenients pot tenir:

* https://www.tutorialspoint.com/postgresql/postgresql_indexes.htm
* https://www.postgresql.org/docs/12/indexes.html

## 5. Creació d'un índex

Crea l'index següent que impactarà en la manera d'executar-se la consulta del punt 3:

    create index salaries_id on salaries(emp_id);

Torna a executar la consulta del punt 3. Notes alguna diferència? Torna a executar l'ordre d'explain/analyze i indica quines diferències hi ha en la sortida. Tracta d'explicar en que consisteixen aquestes diferències. Fes servir de nou la web https://explain.dalibo.com/  per obtenir més informació.

## 6. Tipus d'indexes

Revisa l'enllaç següent i detalla quins tipus d'indexes permet PostgreSQL:
https://www.enterprisedb.com/postgres-tutorials/overview-postgresql-indexes

## 7. Sintaxis de com crear un index i com esborrarlo

Explica la sintaxis per a crear un índex a PostgreSQL. Inclou informació sobre els paràmetres `UNIQUE` i `CONCURRENTLY`. Explica també la sintaxis per esborrar un índex. Consulta els enllaços següents per a fer aquest apartat:

* https://www.postgresql.org/docs/12/sql-createindex.html
* https://www.postgresql.org/docs/12/sql-dropindex.html

Finalment, esbrina com fer un llistat des del client `psql` de tots els indexes existents.

## 8. Un altre explain analyze

Executa la consula següent a la base de dades, que t'hauria de retornar 9 resultats:

	select e.first_name, e.last_name, s.salary from employees as e join salaries as s on e.id = s.emp_id where s. salary > '$150,000' and s.to_date is NULL; 

* Quina informació retorna aquesta consulta?

* Executa ara la consulta amb la comanda `explain analyze` davant i, com en els punts anteriors, explica quina informació obtens.

## 9. Index parcial

Consulta els enllaços següents i explica amb les teves paraules que és un **índex parcial**:

* https://www.postgresql.org/docs/12/indexes-partial.html
* https://www.postgresqltutorial.com/postgresql-indexes/postgresql-partial-index/

Crea un índex parcial per indexar la columna `salary` de la taula `salaries` quan la columna `to_date` es nul·la.

## 10. Explain analyze amb l'index anterior

Amb l'index del punt anteruir, creat, torna a executar la consulta del punt 8 i torna a fer l'explain/analyze. Compara els resultats i tracta d'explicar quins canvis s'han produït.

