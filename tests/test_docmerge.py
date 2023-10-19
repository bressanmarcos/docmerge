from docmerge import docmerge
from numpydoc.docscrape import FunctionDoc


def test_docmerge_inherit_class_docstring():
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


def test_docmerge_inherit_method_docstring():
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


def test_docmerge_inherit_empty_method_docstring_keeps_the_same():
    class Parent:
        def method(self, x: str):
            ...

    class Child(Parent):
        @docmerge
        def method(self, x: str):
            """Child docstring

            Parameters
            ----------
            x : str
                A parameter
                Second line for parameter x
            """

    assert Parent.method.__doc__ == None


def test_docmerge_inherit_method_docstring_merging_except_summary():
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

    assert FunctionDoc(Parent.method)["Summary"] == ["Parent docstring"]
    assert FunctionDoc(Child.method)["Summary"] == ["Child docstring"]
    assert (
        FunctionDoc(Child.method)["Parameters"]
        == FunctionDoc(Parent.method)["Parameters"]
    )


def test_docmerge_inherit_method_docstring_merging_union_of_parameters():
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

    assert (
        FunctionDoc(Parent.__init__)["Summary"]
        == FunctionDoc(Child.__init__)["Summary"]
        == ["Parent docstring"]
    )
    assert {param.name for param in FunctionDoc(Child.__init__)["Parameters"]} == {
        "x",
        "y",
    }


def test_docmerge_inherit_method_docstring_merging_union_of_parameters_with_common_parameter():
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
        def __init__(self, x: int, y: int):
            """
            Parameters
            ----------
            x : int
                A different parameter with another type
            y : int
                Another parameter
            """

    assert (
        FunctionDoc(Parent.__init__)["Summary"]
        == FunctionDoc(Child.__init__)["Summary"]
    )
    assert {param.name for param in FunctionDoc(Child.__init__)["Parameters"]} == {
        "x",
        "y",
    }
    FunctionDoc(Child.__init__)["Parameters"][0].type == "int"


def test_docmerge_inherit_empty_method_docstring_keeps_the_same():
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
            """Child docstring

            The child class provides more details.
            """

    assert FunctionDoc(Parent.method)["Summary"] == ["Parent docstring"]
    assert FunctionDoc(Child.method)["Summary"] == ["Child docstring"]
    assert (
        FunctionDoc(Parent.method)["Parameters"]
        == FunctionDoc(Child.method)["Parameters"]
    )
    assert FunctionDoc(Child.method)["Extended Summary"] == [
        "            The child class provides more details."
    ]
