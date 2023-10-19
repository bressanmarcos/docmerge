def test_docstrings_indentation():
    """This test shows that all docstrings preserve their indentation.
    We need to treat the merging of them carefully."""

    def func():
        """My first line.

        My second line.
        """

    assert func.__doc__ == (
        """My first line.

        My second line.
        """
    )


def func():
    """A docstring short summary

    More description

    Parameters
    ----------
    x : str
        A parameter
        Second line for parameter x
    y : int
        Another parameter

    Returns
    -------
    bool
        The returned value.

    Notes
    -----
    * A notes section
    """


def test_numpydoc():
    """Testing how numpydoc works."""

    from numpydoc.docscrape import NumpyDocString

    docstring = NumpyDocString(func.__doc__)
    assert docstring["Summary"] == ["A docstring short summary"]
    assert any("More description" in line for line in docstring["Extended Summary"])
    assert len(docstring["Parameters"]) == 2
    assert len(docstring["Returns"]) == 1
    assert docstring["Notes"]


def test_numpydoc_functiondoc():
    from numpydoc.docscrape import FunctionDoc

    docstring = FunctionDoc(func)

    assert docstring["Summary"] == ["A docstring short summary"]
    assert any("More description" in line for line in docstring["Extended Summary"])
    assert len(docstring["Parameters"]) == 2
    assert len(docstring["Returns"]) == 1
    assert docstring["Notes"]


def test_python_decorator_and_descriptor_changing_doc():
    class Descriptor:
        def __init__(self, method):
            self.method = method

        def __set_name__(self, owner, name):
            assert self.method.__doc__ == "Original docstring"
            self.method.__doc__ = "New docstring"
            setattr(owner, name, self.method)

    def descriptor(func):
        return Descriptor(func)

    class Parent:
        @descriptor
        def method(self):
            """Original docstring"""
            return 42

    obj = Parent()
    assert obj.method.__doc__ == "New docstring"
    assert obj.method() == 42
