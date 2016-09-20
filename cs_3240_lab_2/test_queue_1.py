__author__ = 'cs3240'

from ourqueue import OurQueue

def test_front_empty():
    """Q1: test calling front on empty queue"""
    q1 = OurQueue()
    res = q1.front()
    assert res == None

def test_remove_empty():
    """Q2: test calling remove on empty queue"""
    q1 = OurQueue()
    res = q1.remove()
    assert res == None, "removing from empty Queue should return None"
    assert len(q1) == 0,  "removing from empty Queue should leave len==0"

def test_remove_size1():
    """Q3: test calling remove on queue of size 1"""
    q1 = OurQueue([1])
    res = q1.remove()
    assert res == 1
    assert len(q1) == 1


def test_front_empty():
    """Q5: test calling front on queue of size 0"""
    q1 = OurQueue()
    res = q1.front()
    assert res is None


def test_front_size1():
    """Q6: test calling front on queue of size 1"""
    q1 = OurQueue([1])
    res = q1.front()
    assert res == 1


def test_init():
    list1 = [1]
    q1 = OurQueue(list1)
    list1[0] = 2
    assert q1.front() == 1, "failed Q7"

