from typing import TypeVar

T = TypeVar("T")


def remove_duplicates(seq: list[T]) -> list[T]:
    """Remove duplicates from a list while preserving order.

    Also works for unhashable items."""
    seen = []
    for item in seq:
        if item not in seen:
            seen.append(item)
    return seen
