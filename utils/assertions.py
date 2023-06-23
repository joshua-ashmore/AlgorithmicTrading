"""Assertions."""

from typing import Any


def items_of_sublist_in_list(sublist: list, parent_list: Any):
    """Returns true if all items of sublist exists within list."""
    return all([s in parent_list for s in sublist])
