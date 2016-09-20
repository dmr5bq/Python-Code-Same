import hw2_p1
from copy import copy


class OurSet:
    """
    OurSet class:

    This class is an implementation of the Set ADT; namely, a collection of indiscriminate items such that there
    are no duplicates and the items are iterable.

    Constructor(s):
        __init__()

    Class methods:
        copy()
        clear()
        remove()
        add()
        add_list()
        __str__()
        __len__()
        __add__() ['+' operator override]
        union()
        intersection()
        __eq__()
    """

    def __init__(self):
        """
        initialized the OurSet object to a new list structure
        """
        self.items = []

    def copy(self, other_set):
        """
        turns the set into a copy of the parameter
        :param other_set:
        :return None:
        """
        self.clear()
        for item in other_set:
            self.add(item)

    def clear(self):
        """
        removes all items in the set's list, while maintaining the pointer's value
        :rtype bool:
        """
        items_copy = copy(self.items)
        for item in items_copy:
            self.items.remove(item)

        if len(self) == 0:
            return True
        else:
            return False

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            return False

    def add(self, item):
        """
        adds a single item to the set, checking to make sure that it is not there already
        :param item:
        :rtype bool:
        """
        if item not in self:
            self.items.append(item)
            return True
        else:
            return False

    def add_list(self, list):
        """
        adds a list of items to the set using the add(item) method to ensure duplicates are not added
        :param list:
        :rtype bool:
        """
        init_size = len(self.items)
        for item in list:
            self.add(item)

        if init_size < len(self.items):
            return True
        else:
            return False

    def __str__(self):
        """
        overrides the standard str function
        :rtype str:
        """
        ret_str = '<'

        if len(self.items) > 0:
            ret_str += str(self.items[0])

            for i in range(1, len(self.items)):
                ret_str += ', ' + str(self.items[i])

        ret_str += '>'

        return ret_str

    def __len__(self):
        """
        overrides the standard len function
        :rtype int:
        """
        return len(self.items)

    def __iter__(self):
        """
        returns the self.list iterator
        :rtype iter:
        """
        return iter(self.items)

    def __add__(self, other):
        """
        overrides the + operator to mimic set union
        :param other:
        :rtype OurSet:
        """
        this_list = self.items
        that_list = other.items  # assuming valid OurSet input

        ret_set = OurSet()

        ret_set.add_list(this_list)
        ret_set.add_list(that_list)

        return ret_set

    def union(self, set2):
        """
        returns the union of the set with the other_set parameter
        :param other_set:
        :rtype OurSet:
        """
        return self + other_set

    def intersection(self, set2):
        """
        returns the intersection of the set with the other_set parameter
        :param set2:
        :rtype OurSet:
        """
        ret_list = hw2_p1.common_items(self.items, set2.items)
        ret_set = OurSet()
        ret_set.add_list(ret_list)

        return ret_set

    def __eq__(self, other):
        """
        overrides the == operator to determine set equality
        :param other:
        :return:
        """
        this_list = self.items
        other_list = other.items

        return this_list == other_list

if __name__ == '__main__':
    import test_set
    test_set.run_all_tests()










        


