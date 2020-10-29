#not finished
import pytest
from Programs import route_planner
list_1 = [0, 8, 12, 2, 10, 6]
def test_route():
    assert route_planner.noreps((route_planner.route(list_1))) == [0, 8, 12]