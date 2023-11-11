docmerge
--------

docmerge is simple tool to merge docstrings from parent classes into child classes.


Usage
-----

1. Copy docstring from parent class

.. code-block:: python

    class Parent:
        """Parent docstring

        Parameters
        ----------
        x : str
            A parameter
            Second line for parameter x
        """

        def __init__(self, x: str):
            ...

    @docmerge
    class Child(Parent):
        ...

    assert Parent.__doc__ == Child.__doc__

2. Copy docstring from parent class method

.. code-block:: python

    class Parent:
        def method(self, x: str):
            """Parent docstring

            Parameters
            ----------
            x : str
                A parameter
                Second line for parameter x
            """

    class Child(Parent):
        @docmerge
        def method(self, x: str):
            ...

    assert Parent.method.__doc__ == Child.method.__doc__

3. Inherit docstring fields that were not set in child class

.. code-block:: python

    class Parent:
        def method(self, x: str):
            """Parent docstring

            Parameters
            ----------
            x : str
                A parameter
                Second line for parameter x
            """

    class Child(Parent):
        @docmerge
        def method(self, x: str):
            """Child docstring"""

This is equivalent to:

.. code-block:: python

    class Child(Parent):
        def method(self, x: str):
            """Child docstring

            Parameters
            ----------
            x : str
                A parameter
                Second line for parameter x
            """

4. For list-like filds (such as Parameters), docstrings can be merged together

.. code-block:: python

    class Parent:
        def __init__(self, x: str):
            """Parent docstring

            Parameters
            ----------
            x : str
                A parameter
                Second line for parameter x
            """

    class Child(Parent):
        @docmerge(union=["Parameters"])
        def __init__(self, x: str, y: int):
            """
            Parameters
            ----------
            y : int
                Another parameter
            """

This is equivalent to:

.. code-block:: python

    class Child(Parent):
        def __init__(self, x: str, y: int):
            """Parent docstring

            Parameters
            ----------
            x : str
                A parameter
                Second line for parameter x
            y : int
                Another parameter
            """


Checkout unit tests in </tests/test_docmerge.py> for an overview of supported features.
