#!/usr/bin/env python3
"""Simple helper function for pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple (start_index, end_index) where:
            - start_index is the index where the page starts
            - end_index is the index where the page ends (exclusive in slicing)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
