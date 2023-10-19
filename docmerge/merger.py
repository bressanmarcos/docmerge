from .misc import remove_duplicates
from numpydoc.docscrape import NumpyDocString


def merge_docstrings(doc_1, doc_2, *, union=None):
    """
    Merge two numpy-style docstrings.

    Parameters
    ----------
    doc_1 : str
        The first docstring to merge.
    doc_2 : str
        The second docstring to merge.
    union : str or list of str, optional
        The sections to merge. If None, all sections are merged. If a string, only that section is merged.
        If a list of strings, only those sections are merged. Default is None.

    Returns
    -------
    str
        The merged docstring.

    Raises
    ------
    TypeError
        If `union` is not a string or list of strings.

    Notes
    -----
    This function uses the `NumpyDocString` class from the `numpydoc` package to parse and manipulate the docstrings.

    Examples
    --------
    >>> doc_1 = \"\"\"This is the first docstring.
    ...
    ... Parameters
    ... ----------
    ... x : int
    ...     The first parameter.
    ...
    ... Returns
    ... -------
    ... int
    ...     The result.
    ... \"\"\"
    >>> doc_2 = \"\"\"This is the second docstring.
    ...
    ... Parameters
    ... ----------
    ... y : int
    ...     The second parameter.
    ...
    ... Returns
    ... -------
    ... int
    ...     The result.
    ... \"\"\"
    >>> print(merge_docstrings(doc_1, doc_2, union="Parameters"))
    <BLANKLINE>
    This is the second docstring.
    <BLANKLINE>
    Parameters
    ----------
    x : int
        The first parameter.
    y : int
        The second parameter.
    <BLANKLINE>
    Returns
    -------
    int
        The result.
    <BLANKLINE>
    """
    
    if not doc_2:
        return doc_1
    if not doc_1:
        return doc_2

    if isinstance(union, str):
        union = [union]
    elif not union:
        union = []
    elif isinstance(union, list):
        union = union
    else:
        raise TypeError(f"union must be str or None, not {type(union)}")

    docstring_1 = NumpyDocString(doc_1)
    docstring_2 = NumpyDocString(doc_2)

    for section in docstring_2:
        if not docstring_2[section]:
            continue
        if docstring_2[section] == docstring_2.sections[section]:
            continue

        if section in union:
            all_items = docstring_1[section] + docstring_2[section]
            docstring_1[section] = remove_duplicates(all_items)
        else:
            docstring_1[section] = docstring_2[section]

    return str(docstring_1)

