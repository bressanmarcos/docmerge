from .merger import merge_docstrings
from functools import partial
from typing import Callable


def docmerge(obj: type | Callable | None = None, **kwargs):
    """
    Merge docstrings from parent classes or functions with the current object's docstring.

    Parameters
    ----------
    obj : Union[type, callable, None], optional
        The object to merge the docstrings with. If None, returns a partial function with the `union` argument set.
    union : Union[str, None], optional
        Fields from docstring to merge together instead of overwriting. When used for the "Parameters" section, for instance,
        the parameters from the parent class will be merged with the parameters from the child class. If some parameter name
        is repeated, the child class parameter will be used.
    **kwargs : Any
        Any other keyword argument will be passed to the :func:`docmerge.merger.merge_docstrings` function.

    Returns
    -------
    Union[callable, partial]
        The merged docstring object.

    Examples
    --------
    >>> class Parent:
    ...     '''This is the parent class docstring.'''
    ...
    >>> @docmerge
    ... class Child(Parent):
    ...     '''This is the child class docstring.'''
    ...
    >>> print(Child.__doc__)
    <BLANKLINE>
    This is the child class docstring.
    <BLANKLINE>
    """

    if obj is None:
        return partial(docmerge, **kwargs)

    if isinstance(obj, type):
        cls = obj
        parent = super(cls, cls)
        cls.__doc__ = merge_docstrings(parent.__doc__, cls.__doc__, **kwargs)
    elif callable(obj):
        func = obj
        return _MethodDocMerger(func, **kwargs)

    return obj


class _MethodDocMerger:
    def __init__(self, method, **kwargs) -> None:
        self.method = method
        self.kwargs = kwargs

    def __set_name__(self, owner, name):
        parent = super(owner, owner)
        parent_method = getattr(parent, name)

        self.method.__doc__ = merge_docstrings(
            parent_method.__doc__, self.method.__doc__, **self.kwargs
        )
        setattr(owner, name, self.method)
