import pytest
from function import*

def test_feature():
    assert feature() == True

def test_number_of_above_averages():
    assert number_of_above_averages(2, 2, [[1,1],[2,4]])==1
    assert number_of_above_averages(2, 3, [[1,2,3],[4,5,6]])==3

def test_common_elements():
    assert common_elements([3,1,2], [2,4,3])==[2,3]
    assert common_elements([3,3,2], [3,3,4,5])==[3]

t789 = ManhattanTaxi(5, 5, 1, 30)

def test_ManhattanTaxi():
    assert t789.moveto(3,9)==True
    assert t789._pos[0]==3 and t789._pos[1]==9
    assert abs(t789._fuel - 24) < 0.01

def test_shortest_continuous_segment():
    assert shortest_continuous_segment([1,1,2,2,2,1,1,1])==(1,2)
    assert shortest_continuous_segment([5,5,5,2,2,2,2,3,3,3])==(5,3)