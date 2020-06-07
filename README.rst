pyariable
#########

Simplify your test assertions forever.

.. code-block:: python
   :class: ignore

   from pyariable import Variable

   def test_dict():
       x = Variable()
       y = Variable()
       assert {1: "XXX", 2: "XXX", 3: "YYY"} == {1: x, 2: x, 3: y}
       assert x != y

In some tests it's common to get a random ID back from a database. Your assertions are simpler when you substitute a `Variable` object for the expected value.

.. code-block:: python
   :class: ignore

   from pyariable import Variable

   def test_list():
       x = Variable()
       y = Variable()
       assert [
           {"db_id": 590, "name": "alice"},
           {"db_id": 590, "name": "bob"},
           {"db_id": 999, "name": "charlie"},
       ] == [
           {"db_id": x, "name": "alice"},
           {"db_id": x, "name": "bob"},
           {"db_id": y, "name": "charlie"},
       ]
       assert x != y
       assert x < y


Installation
------------
.. code-block:: bash
   :class: ignore

   pip install pyariable
