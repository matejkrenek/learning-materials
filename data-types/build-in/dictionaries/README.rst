Dictionary
####

- python ``dictionary`` se používá k uložení key:value dat

Zadání
-------------------
Řekněme, že máme sbírku několika aut. O každém autu potřebujeme ale vědět hned několik informací:
Název auto, barvu auta, rok výroby

Bez použití ``dictionary``
-------------------
Bez použití ``dictionary`` bychom jedno auto zapsali asi tímto způsobem

.. code-block:: python

  car_name = "BMW"
  car_color = "red"
  car_year = 1923
  
Pro každý parameter auto tedy declarujeme vlastní proměnnou.
Co když bychom chtěli nějaký parametr auta upravit ?
Museli bychom přepsat hodnotu existující proměnné, která náleží danému parametru:

.. code-block:: python

  car_color = "blue"
  
Problém s tímto provedením
-------------------
1. Parametry auta mezi sebou nemají žádný vzah
2. Aut v naší sbírce může být několik
3. Složitá úprava či přidání parametru auta, právě kvůli problému 1.

Řešení těchto problému je jednoduché.

Použít python ``dictionary``.

S použitím ``dictionary``
-------------------
.. code-block:: python

    car = {
      "name": "BMW",
      "color": "red",
      "year": 1923
    }
    
Chceme-li změnit nějaký parametr auta:

.. code-block:: python

  car["color"] = "blue"
  
Chceme-li přidat nějaký nový parametr auta:

.. code-block:: python

  car["owner"] = "Matěj Křenek"
  
Vytvoření kolekce aut
-------------------
- Python ``dictionary`` můžeme zkombinovat z jakýmkoliv python datovým typem
- V příkladu u ``listů`` jsme vytvořili list elementů, kde každý element korespondoval s jedním autem. Auto jsme zapsali v datovém typu ``string``.
- Pomocí ``dictionary`` ale můžeme naší kolekci auto zapsat praktičteji a podrobněji

.. code-block:: python

  cars = [{"name": "BMW", "color": "red", "year": 1923}, {"name": "Audi", "color": "blue", "year": 2013}]
  cars.append({"name": "Trabant", "color": "blue", "year": 1956})
  
Elementy tohoto listu jsou ``dictionaries``
