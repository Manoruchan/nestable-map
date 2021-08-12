import collections


# def flatten(nested_list):
#   flat_list = []
#   fringe = [nested_list]

#   while len(fringe) > 0:
#       node = fringe.pop(0)
#       if isinstance(node, list):
#           fringe = node + fringe
#       else:
#           flat_list.append(node)

#   return flat_list


def flatten(l):
    """
    flatten lists
    """
    for el in l:
        if isinstance(el, collections.abc.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
