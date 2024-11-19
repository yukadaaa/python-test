import pytest
from calculations import multiply, divide, distance, solve_quadratic, geometric_sum
#Кадочников Александр 
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 10) == 0
    assert multiply(7, -3) == -21
    assert multiply(1, 1) == 1

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, -3) == -3
    assert divide(0, 1) == 0
    assert divide(5, 5) == 1
    with pytest.raises(ValueError):
        divide(10, 0)  

def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(1, 1, 4, 5) == 5
    assert distance(-1, -1, -4, -5) == 5
    assert distance(0, 0, 0, 0) == 0
    assert distance(2, 3, 2, 3) == 0

def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (2, 1)  # Roots are 2 and 1
    assert solve_quadratic(1, -2, 1) == (1,)     # One root: 1
    assert solve_quadratic(1, 0, -4) == (2, -2)  # Roots are 2 and -2
    assert solve_quadratic(1, 1, 1) == None      # No real roots
    assert solve_quadratic(0, 1, -4) == (4,)     # Linear equation

def test_geometric_sum():
    assert geometric_sum(1, 2, 3) == 7
    assert geometric_sum(1, 1, 5) == 5
    assert geometric_sum(2, 3, 2) == 8
    assert geometric_sum(1, 0.5, 3) == 1.75
    assert geometric_sum(10, 2, 4) == 150
