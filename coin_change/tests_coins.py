import pytest
from coins import CoinChanger

cases = [
    None,
    {'5c': 1, },
]
expected_values = [
    0.0,
    0.05,
]


@pytest.mark.parametrize(
    "case, expected_value",
    zip(cases, expected_values)
)
def test_init(case, expected_value):
    coin_changer = CoinChanger(case)

    klass = type(coin_changer)
    msg = "Wrong instance: {}".format(klass)
    assert isinstance(coin_changer, CoinChanger), msg

    msg = "coin_changer value should be {}, instead of {}"
    msg = msg.format(expected_values, coin_changer.value)
    assert coin_changer.value == expected_value, msg


def test_wrong_denomination():
    coin_changer = CoinChanger()
    msg = "Key error on wrong denomination expected"
    with pytest.raises(KeyError, message=msg):
        coin_changer["1d"]
