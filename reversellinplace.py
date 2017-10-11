"""Given linked list, reverse the nodes in this linked list in place.

Iterative solution doctest:

    >>> ll1 = LinkedList(Node(1, Node(2, Node(3))))
    >>> ll1.as_string()
    '123'
    >>> reverse_linked_list_in_place(ll1)
    >>> ll1.as_string()
    '321'

Recursive solution doctest:

    >>> ll2 = LinkedList(Node(1, Node(2, Node(3))))
    >>> ll2.as_string()
    '123'
    >>> reverse_linked_list_in_place_rec(ll2)
    >>> ll2.as_string()
    '321'
"""


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# ITERATIVE SOLN


def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""

    # build up a new LL, starting with none
    # traverse original LL, getting current to attach to new LL
    # need constant reshuffling of prev, current, .next
    # at the end, re-assign head to finished new LL

    # initialize new LL as prev where it's initially None; will append overtime
    # thus, at the end of the LL, last item is pointed to None
    prev = None

    # initialize traversal of LL w/ .head
    curr = lst.head

    # traverse original LL
    while curr is not None:
        next = curr.next

        # attach current item in original LL to new LL
        curr.next = prev

        # reassign prev to be first item in new LL
        prev = curr

        # traverse original LL by one step
        curr = next

    # once traversal done (and new LL fully built), point LL head to first item
    lst.head = prev

# RECURSIVE SOLN


def reverse_linked_list_in_place_rec(lst):
    """Given linked list, RECUSIVELY reverse the nodes
    in this linked list in place."""

    # Have fn w/ curr (lst.head) and prev (none) as 2 paramaters
    curr = lst.head
    prev = None

    def _rec_reverse(curr, prev):

    # BASE CASE
        # traversing through original LL... when curr is None, stop recursing
        # and return new LL

        if not curr:
            return prev

    # PROGRESSION
        # same as iteration sol'n inside while loop
        # call fn until curr is None

        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

        return _rec_reverse(curr, prev)

    # outside the recursive fn, re-attach head to final LL
    lst.head = _rec_reverse(curr, prev)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
