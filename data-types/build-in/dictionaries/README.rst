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

