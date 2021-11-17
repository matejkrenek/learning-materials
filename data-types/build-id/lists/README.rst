Listy
####

Listy se používají k uložení více prvků do jedné proměné

Zadání
-------------------
Řekněme, že máme sbírku 5 aut, které potřebujeme v pythnu nějákým způsobem uložit

Bez použití listů
-------------------
Bez použití listů bychom postupovali nejspíše tímto způsobem:

.. code-block:: python

    car1 = "Audi"
    car2 = "BMW"
    car3 = "Škoda"
    car4 = "Volkswagen"
    car5 = "Renault"

Pro každé auto ve sbírce deklarujeme vlastní proměnnou

Co když se do naší sbírky ale přidá další auto?
Musíme logicky pro toto auto deklarovat další proměnnou:

.. code-block:: python

    ...
    car6 = "Volkswagen Golf"

Problém s tímto provedením
-------------------
1. Je velice nepravděpodobné, že znáte přesný počet všech položek v jakémkoliv listu
2. Mezi jednotlivými proměnnými všech aut není žádný vztah, přestože patří do stejné sbírky
3. Je v podstatě nemožné odstranit auto ze sbírky nebo jej přeřadit na jinou pozici a to právě kvůli problému 2.

Řešení těchto problému je jednoduché.

Použít python ``list``.

S použitím listů
-------------------
.. code-block:: python

    cars = ["Audi", "BMW", "Škoda", "Volkswagen", "Renault"]
   
Potrřebujeme-li do sbírky přidat další auto:

.. code-block:: python

    ...
    cars.append("Volkswagen Golf")
