from pyariable import Variable


def test_right_hand_side():
    x = Variable()
    assert "?" == repr(x)
    assert "XXX" == x
    assert "'XXX'" == repr(x)


def test_left_hand_side():
    x = Variable()
    assert "?" == repr(x)
    assert x == "XXX"
    assert "'XXX'" == repr(x)


def test_only_one_value():
    x = Variable()
    assert "XXX" == x
    assert "YYY" != x


def test_gt():
    x = Variable()
    assert 1 == x
    assert 2 > x


def test_lt():
    x = Variable()
    assert 1 == x
    assert 2 > x


def test_dict():
    x = Variable()
    y = Variable()
    assert {1: "XXX", 2: "XXX", 3: "YYY"} == {1: x, 2: x, 3: y}
    assert x != y


def test_list():
    x = Variable()
    y = Variable()
    assert [
        {"group_id": 590, "name": "alice"},
        {"group_id": 590, "name": "bob"},
        {"group_id": 999, "name": "charlie"},
    ] == [
        {"group_id": x, "name": "alice"},
        {"group_id": x, "name": "bob"},
        {"group_id": y, "name": "charlie"},
    ]
    assert x != y


def test_2_variables():
    x = Variable()
    y = Variable()
    assert {1: "XXX", 2: "XXX"} == {1: x, 2: y}
    assert x == y


def test_2_different_variables():
    x = Variable()
    y = Variable()
    assert 1 == x
    assert 2 == y
    assert x < y
    assert y > x


def test_assign_to_another_variable():
    x = Variable()
    y = Variable()
    assert x == y
    assert "XXX" == x
    assert "'XXX'" == repr(x)
    assert "'XXX'" == repr(y)
    assert "XXX" == y
