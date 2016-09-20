from hw2_set import OurSet


def test_copy_and_equals():
    set1 = OurSet()
    set2 = OurSet()

    assert set1 == set2

    set1.add_list(['a', 'b', 'c'])

    assert set1 != set2

    set2.copy(set1)

    assert set1 == set2


def test_add():
    set = OurSet()
    set.add(0)
    assert len(set.items) == 1, 'too short'
    assert set.items[0] == 0, 'wrong data'

    set.add(0)
    assert len(set.items) == 1, 'too short'
    assert set.items[0] == 0, 'wrong data'

    set.clear()


def test_add_list():
    set = OurSet()
    set.add_list([0,1])
    assert len(set.items) == 2, 'wrong len'
    assert set.items[1] == 1, 'wrong data'

    set.add_list([0,1,2])
    assert len(set.items) == 3, 'wrong length'
    assert set.items[2] == 2

    set.clear()

    set.add_list(['a', 'b', 'c'])

    assert len(set) == 3


def test_str():
    set = OurSet()
    assert str(set) == "<>", 'wrong str'
    set.add_list([0,0,0,0,1,2,3,4,4,4,5,5,0])
    assert str(set) == '<0, 1, 2, 3, 4, 5>', 'wrong str'


def test_len():
    set = OurSet()

    assert len(set) == 0

    set.add_list([0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 5, 5, 0])
    assert len(set) == 6


def test_iter():
    set = OurSet()

    set.add_list([0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 5, 5, 0])

    itr = iter(set)
    assert itr.next() == 0
    assert itr.next() == 1
    assert itr.next() == 2


def test_add_op():
    set1 = OurSet()
    set2 = OurSet()

    assert len(set1 + set1) == len(set1)

    set1.add_list([0, 1, 2, 3, 4, 5, 6])
    set2.add_list([4, 5, 6, 7, 8, 9])

    assert len(set1 + set2) == 10, 'failed add_op'


def test_intersection():
    set1 = OurSet()
    set2 = OurSet()
    blank_set = OurSet()

    set1.add_list([0, 1, 2, 3, 4, 5, 6])
    set2.add_list([4, 5, 6, 7, 8, 9])

    assert len(set1.intersection(set2)) == 3
    assert len(set1.intersection(blank_set)) == len(blank_set)


def run_all_tests():
    test_add()
    test_add_list()
    test_str()
    test_len()
    test_iter()
    test_add_op()
    test_intersection()
    test_copy_and_equals()