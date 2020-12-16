# encoding: utf-8

# Standard Library
# 3rd Party Library
# Current Folder
# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def chunks(collection, size: int):
    """
    Create sub-lists from the base collection with the desired size.

    Parameters:
        collection: The collection
        size: Number of items per sub-list
    """
    for index in range(0, len(collection), size):
        yield collection[index: index + size]
