# Pràctica 4: Importar i exportar CSV

La pràctica consisteix en importar i exportar fitxers de dades CSV a la nostra base de dades PostgreSQL. Les dades les heu d'importar a la vostra base de dades, que en el meu cas es diu `dbcristianoronaldo`.

Els fitxers CSV han d'estar a l'equip on teniu el cliente `psql`, idealment a la vostra màquina real. El mès fàcil és que els descarregueu a una carpeta i executeu `psql` dins d'aquesta carpeta. Així és com ho he fet jo a les captures de pantalla.

## 1. Importa el fitxer d'empleats en format CSV empleats.CSV

Per fer-ho, situat dins del client PSQL i executa la comanda `\copy`:

![images/apartat1.png](images/apartat1.png)

## 2. Importa ara dept_manager

Fixa't en que he afegit la indicació de que consideri el text 'NULL' present al CSV com un NULL, no com una cadena de text.

![images/apartat2.png](images/apartat2.png)

## 3. Importa el CSVs de dept_emp, titles i salaries

Les dades de `salaries` les tens en dos fitxers comprimits amb gzip. Hauràs de tenir cura dels NULL com a l'apartat anterior.

## 4. Corregeix els seqüencials

Igual que a la pràctica anterior, quan s'inserten dades a una columna associada a un seqüencial, cal modificar el seqüencial per a que retorni valors que no coincideixin amb els valors ja inserits.

La captura següent és un exemple que jo he fet amb la seqüència `employees_id_seq` associada a la columna `id` de la taula `employees`:

![images/apartat4.png](images/apartat4.png)

## 5. Prova d'exportació amb CSV

Fes una prova d'exportació. Per exemple, exporta tots els first_name i last_name DIFERENTS d'empleats que el nom comença per Z i el cognom acaba per z. Has de tenir 97 resultats.

Et deixo alguns enllaços que et poden ajudar:

* [Exportar CSV](https://dataschool.com/learn-sql/export-to-csv-from-psql/)
* [Fer servir LIKE per buscar patrons en cadenes de text](https://www.tutorialspoint.com/postgresql/postgresql_like_clause.htm)
* [Fer servir el DISTINCT](https://www.postgresqltutorial.com/postgresql-select-distinct/)

## 6. Comanda \copy

Revisa la documentació de [\copy](https://www.postgresql.org/docs/12/app-psql.html#APP-PSQL-META-COMMANDS-COPY). Quina diferència hi ha amb la comanda [COPY](https://www.postgresql.org/docs/12/sql-copy.html)? Quins formats de sortida permet?

## 7. Còpia de seguretat

Fes una còpia de seguretat de la base de dades amb `pg_dump` des de la teva màquina real. L'objectiu és fer un script per a poder automatizar les còpies de seguretat, per tant, ens hauriem de pode connectar sense fer servir un password. Farem servir la cadena de connexió:

    pg_dump --dbname=postgresql://username:password@127.0.0.1:5432/databasename

**Atenció!** Si estas fent servir una màquina fixa de l'aula 110, has de fer:

    ./run.sh pg_dump --dbname=postgresql://cristianoronaldo:mir@172.17.0.1:5432/dbcristianoronaldo

Fes una còpia de seguretat de la base de dades comprimida amb gzip. En aquest enllaç tens una indicació de com fer-ho: [https://gist.github.com/atenni/a73cfbec1b7fd367b833](https://gist.github.com/atenni/a73cfbec1b7fd367b833)

## 8. Restaura la còpia de seguretat

Crea una base de dades novas anomenada `backup_test` i restaura la còpia de seguretat que has fet en el punt anterior. Al mateix link que abans tens com restaurar un backup comprimit amb gzip: [https://gist.github.com/atenni/a73cfbec1b7fd367b833](https://gist.github.com/atenni/a73cfbec1b7fd367b833)

Comprova que les dades s'han restaurat i, un cop comprovat, esborra la base de dades.

## 9. Script de backup

Ara fes un script amb la comanda de backup del punt 7, però de manera que el nom de fitxer afegeixi la data i hora quan s'ha fet la còpia de seguretat. Al link següent tens una ajuda de coom afegir el timestamp al nom d'un fitxer: [https://www.cyberciti.biz/faq/unix-linux-appleosx-bsd-shell-appending-date-to-filename/](https://www.cyberciti.biz/faq/unix-linux-appleosx-bsd-shell-appending-date-to-filename/).

## 10. Dades en format HTML

El client `psql` et permet mostrar els resultats d'una consulta en format HTML. Mira com fer-ho i prova de fer una consulta, com per exemple tenir totes les dades de la taula `departments` en format HTML.
