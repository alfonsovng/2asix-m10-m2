# Pràctica 6: Selects avançades

La pràctica consisteix en fer algunes consultes complexes a la nostra base de dades d'empleats. A totes cal fer joins ( o inner joins, que és el mateix)

## 1. Empleats mes joves

Busca l'empleat  més jove que és actualment a Marketing. En realitat tindràs 7 resultats, perquè han nascut el mateix dia i són els més joves.

*Indicació:*

* Fer servir `IN` d'una manera semblant a aquest exemple: https://stackoverflow.com/a/7745679


## 2. Empleat mes vell

Busca l'empleat que era mes vell en el moment de contractar-lo. El resultat és un empleat nascut el `1952-02-02`. 

*Indicació:*

* Semblant a l'anterior, fent servir `MAX` per trobar el que tingui la màxima diferencia entra la data de naixement i la de contractació.

## 3. Empleats rics

Busca els nom i el cognom dels empleats que tinguin actualment un salari superior a 150.000 $. Tindràs 9 resultats.

## 4. Salaris mitjans

Busca el salari mitjà actual de cada departament. El salari mitjà de Marketing és de $80,037.27.

*Indicacions:*

* Convertir el tipus money a enter per poder aplicar la funció `AVG`: https://stackoverflow.com/a/64751129
* Fer servir `GROUP BY`

## 5. Dones senior
Busca la data de contractació i el title dels empleats dones que el seu titol comença per 'Senior' i van ser contractades posterioment al 1 de gener del 2000. Tindràs 2 resultats.

*Indicació:*

* Fer servir `LIKE`







