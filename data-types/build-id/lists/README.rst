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

    cars.append("Volkswagen Golf")
    
Terminologie
-------------------
=======================================  ==================================================================== ===============================================================
Pojem                                    Význam                                                               Příklad
=======================================  ==================================================================== ===============================================================
``element``                              ``element`` je jedna položka z listu                                 v listu ``cars`` jsou ``elementy`` "Audi", "BMW", "Škoda" atd.
``index``                                ``index`` je pozice ``elementu`` v listu                             ``element`` "Audi" v listu ``cars`` má ``index`` 0
``délka``                                ``délka`` listu označuje kolik ``elementů`` se listu nachází         ``délka`` listu ``cars`` je 6
=======================================  ==================================================================== ===============================================================

Práce s listy
-------------------

Pro názorné ukázky si declarujeme dva listy

.. code-block:: python

    fruits = ["Jablko", "Hruška", "Mandarinka"]
    vegetables = list(("Mrkev", "Okurka", "Brambora", "Rajče"))
    
list ``vegetables`` je vytvořen pomocí ``build-in`` funkce ``list``.

funkce ``list`` nám vytvoří totžný list jako ``fruits``

Tento způsob vytvoření listu se přiliš nepoužívá, ale za zmínku stojí

**Přístup k elementu:**

.. code-block:: python

    print(fruits[0]) # "Jablko"
    print(fruits[2]) # "Mandarinka"
    print(fruits[-1]) # "Mandarinka"
    print(fruits[5]) # IndexError: list index out of range
    print(vegetables[1]) # "Okurka"
    
**Změna hodnoty elementu:**

.. code-block:: python

    print(fruits) # ["Jablko", "Hruška", "Mandarinka"]
    fruits[0] = "Jablíčko"
    print(fruits) # ["Jablíčko", "Hruška", "Mandarinka"]
    
**Délka listu:**

.. code-block:: python

    print(len(fruits)) # 3
    print(len(vegetables)) # 4
    
**Přidání elementu do listu:**

- Pomocí ``append``:
    - přidá element na konec listu

.. code-block:: python

    print(fruits) # ["Jablko", "Hruška", "Mandarinka"]
    fruits.append("Pomeranč")
    print(fruits) # ["Jablko", "Hruška", "Mandarinka", "Pomeranč"]
    
- Pomocí ``insert``:
    - přidá element na konkrétní pozici v listu

.. code-block:: python

    print(fruits) # ["Jablko", "Hruška", "Mandarinka"]
    fruits.insert(1, "Pomeranč")
    print(fruits) # ["Jablko",  "Pomeranč", "Hruška", "Mandarinka"]
    
- Pomocí ``extend``:
    - přidá elementy z jednoho listu na konec druhého listu

.. code-block:: python

    print(fruits) # ["Jablko", "Hruška", "Mandarinka"]
    fruits.extend(vegetables)
    print(fruits) # ["Jablko", "Hruška", "Mandarinka", "Mrkev", "Okurka", "Brambora", "Rajče"]
    
**Odebrání elementu z listu:**

- Pomocí ``remove``:
    - Vymaže z listu ``element`` s konkrétní hodnotou

.. code-block:: python

    print(fruits) # ["Jablko", "Hruška", "Mandarinka"]
    fruits.remove("Hruška")
    print(fruits) # ["Jablko", "Mandarinka"]
    
- Pomocí ``pop``:
    - Vymaže z listu ``element`` na konkrétní pozici
    - Bez zadaní pozice vymaže z listu poslední ``element``

.. code-block:: python

    print(fruits) # ["Jablko", "Hruška", "Mandarinka"]
    fruits.pop(0)
    print(fruits) # ["Hruška", "Mandarinka"]
    fruits.pop()
    print(fruits) # ["Hruška"]
    
- Pomocí ``del``:
    - Vymaže z listu ``element`` na konkrétní pozici
    - Bez zadaní pozice vymaže kompletně celý list

.. code-block:: python

    print(fruits) # ["Jablko", "Hruška", "Mandarinka"]
    del fruits[0]
    print(fruits) # ["Hruška", "Mandarinka"]
    del fruits
    print(fruits) # NameError: name 'fruits' is not defined
    
- Pomocí ``clear``:
    - Vymaže z listu všechny ``elementy``

.. code-block:: python

    print(fruits) # ["Jablko", "Hruška", "Mandarinka"]
    fruits.clear()
    print(fruits) # []
    
**Průchod všemi ``elementy`` listu pomocí ``cyklů``:**

- Pomocí ``for``:

.. code-block:: python

    for element in fruits:
      print(element)
    
    # "Jablko"
    # "Hruška"
    # "Mandarinka"
    
    for index in range(len(fruits)):
        print(fruits[index])
        
    # "Jablko"
    # "Hruška"
    # "Mandarinka"
    
- Pomocí ``while``:
.. code-block:: python

    for element in fruits:
      print(element)
    
    # "Jablko"
    # "Hruška"
    # "Mandarinka"
    
    for index in range(len(fruits)):
        print(fruits[index])
        
    # "Jablko"
    # "Hruška"
    # "Mandarinka"
    

