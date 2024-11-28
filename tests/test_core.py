from pyariable import UniversalVariable, ValidationError, Variable, variables


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


def test_gte():
    x = Variable()
    assert 1 == x
    assert 2 >= x


def test_lt():
    x = Variable()
    assert 3 == x
    assert 2 < x


def test_lte():
    x = Variable()
    assert 3 == x
    assert 2 <= x


def test_round():
    x = Variable()
    assert 1.1 == x
    assert 1 == round(x, 0)


def test_int():
    x = Variable()
    assert 1.1 == x
    assert 1 == int(x)


def test_dict():
    x = Variable()
    y = Variable()
    assert {1: "XXX", 2: "XXX", 3: "YYY"} == {1: x, 2: x, 3: y}
    assert x != y


def test_variables():
    x, y = variables(2)
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


def test_is_valid():
    x = UniversalVariable(lambda i: False if i == "bad" else True)
    try:
        assert x == "bad"
    except ValidationError:
        pass
    else:
        raise Exception

    assert x == "good"


def test_prefix_right_hand_side():
    x = Variable()
    assert "?" == repr(x)
    assert "prefix.XXX" == "prefix." + x
    assert "XXX" == x
    assert "'XXX'" == repr(x)


def test_prefix_right_hand_side_int():
    x = Variable()
    assert "?" == repr(x)
    assert 7 == 5 + x
    assert 2 == x
    assert "2" == repr(x)


def test_prefix_right_hand_side_float():
    x = Variable()
    assert "?" == repr(x)
    assert 7.0 == 5.0 + x
    assert 2.0 == x
    assert "2.0" == repr(x)


def test_suffix_left_hand_side():
    x = Variable()
    assert "?" == repr(x)
    assert "XXX.suffix" == x + ".suffix"
    assert "XXX" == x
    assert "'XXX'" == repr(x)


def test_suffix_left_hand_side_int():
    x = Variable()
    assert "?" == repr(x)
    assert 7 == x + 5
    assert 2 == x
    assert "2" == repr(x)


def test_suffix_left_hand_side_float():
    x = Variable()
    assert "?" == repr(x)
    assert 7.0 == x + 5.0
    assert 2 == x
    assert "2.0" == repr(x)
