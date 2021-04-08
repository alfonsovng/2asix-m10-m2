# Pràctica 7: Auditoria de canvis en BD

L'auditoria de canvis en bases de dades és el procés que permet mesurar, assegurar, demostrar, monitoritzar i registrar els accessos a la informació emmagatzemada en les bases de dades, incloent la capacitat de determinar:

* Qui accedeix a les dades
* Quan s'ha accedit
* L'origen
* Sentència executada
* Efecte de l'accés

Per poder fer una auditoria completa de la nostra base de dades, anem a registrar tots els canvis de la nostra base de dades creant una sèrie de taules per guardar els canvis i fer servir *triggers* per a que s'emmagatzemin de manera automàtica els canvis a aquestes taules.

## 1. Creació d'un nou schema

Amb l'usuari `postgres`, crea un nou schema que es digui `audit` i modifica els permisos d'aquest schema per a que ningú pugui crear taules en aquest schema.

## 2. Nova taula employees_log

Crea el tipus de dades i la taula següent al nou schema:

```sql
    CREATE TYPE audit.dml_type AS ENUM ('INSERT', 'UPDATE', 'DELETE');
	
    CREATE TABLE IF NOT EXISTS audit.employees_audit_log (
        emp_id int NOT NULL,
        old_row_data jsonb,
        new_row_data jsonb,
        dml_type audit.dml_type NOT NULL,
        dml_timestamp timestamp NOT NULL,
        dml_created_by TEXT NOT NULL,
        PRIMARY KEY (emp_id, dml_type, dml_timestamp)
    );
```
Fixa't que el nom de la taula i el del tipus de dades comencen per `audit.` per a que aquests siguin creats a l'schema `audit`.

Si executes `\d` al client psql no veuràs la nova taula. Per a que surti al llistat, pos executar:

	\d audit.*

També, per comoditat, pots fer que per defecte també es mostrin els elements del nou schema. Executa:

	SET search_path TO public, audit; 

Ara, fent `\d`, veuràs les taules dels schemas `public`i `audit`. Comprova-ho.

## 3. Tipus de dades jsonb

A la taula anterior has fet servir el tipus de de dades `jsonb`. Busca informació sobre aquest tipus de dades de postgresql, per a que serveix i en que es diferència del tipus de dades `json`.

## 4. Afegim triggers

Fixa't en el següent article i adapta la funció i el trigger per a que les accions es registrin a la taula `audit.employees_audit_log`:

https://vladmihalcea.com/postgresql-audit-logging-triggers/

Prova-ho fent un update, un insert i un delete a la taula `employees`. Comprova que cada acció suposa una nova fila a la taula `audit.employees_audit_log`. 

*ATENCIÓ!* Si et dona un error:

	ERROR:  syntax error at or near "current_setting"
	LINE 1: current_setting('myapp.userid')

substitueix aquesta part de la funció per `session_user::text`.

*[Si el link anterior no està disponible, tens aquí el mateix article en format PDF](https://github.com/alfonsovng/2asix-m02-m10/files/6137259/vladmihalcea.com-PostgreSQL.audit.logging.using.triggers.pdf)*

## 5. PgSQL i triggers

Fes un petita explicació, amb les teves pròpies paraules, de que és PgSQL, el llenguatge de programació amb el que s'ha implementat la funció del punt anterior: https://es.wikipedia.org/wiki/PL/PgSQL

Fes també un petit resum de la sintaxis per a crear un trigger que inclogui les opcions que indiquen el moment en que s'executa i amb quins events.

## 6. Replicar-ho amb la taula departments

Replica els mateixos passos que has fet amb la taula `employees` aquest cop amb la taula `departments`. 

## 7. Log de totes les consultes

Per acabar, pots també registrar totes les consultes que es fan a la base de dades. Per fer-ho, posa el valor del paràmetre `log_statement`  a `all` al fitxer de configuració `postgresql.conf` del teu cluster i reinicia la base de dades. Desprès, fes una consulta i comprova que apareix al fitxer de logs. 

## 8. Rotació del log

Per a no omplir el disc de logs, implantaràs un sistema de rotació de logs setmanal. Això vol dir, que es guardaran els logs d'una setmana, la resta s'aniran sobreescrivint. Segueix la següent pàgina i comprova que funciona: 

https://docs.microfocus.com/UCMDB/11.0/ucmdb-docs/docs/eng/doc_lib/Content/database/PostgreSQL_config_log_file_rotate.htm

*[Si el link anterior no està disponible, tens aquí el mateix article en format PDF](https://github.com/alfonsovng/2asix-m02-m10/files/6137261/docs.microfocus.com-How.to.Configure.PostgreSQL.Log.Files.Rotation.by.Size.pdf)*
