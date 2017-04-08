denominations = {
    "5c": 0.05,
    "10c": 0.10,
    "20c": 0.20,
    "50c": 0.50,
    "1e": 1.0,
    "2e": 2.0,
}


class CoinChanger(object):
    def __init__(self, coins=None):
        self.__coins = coins or {}

    @property
    def value(self):
        return sum(
            self.__coins[coin] * denominations[coin] for coin in self.__coins
        )

    def __getitem__(self, index):
        if index in denominations:
            return self.__coins.get(index, 0)
        raise KeyError("Money type not allowed {}".format(index))

    def __setitem__(self, index, value):
        if index in denominations:
            if index not in self.__coins:
                self.__coins[index] += 0
            self.__coins[index] += value
        else:
            raise KeyError("Money type not allowed {}".format(index))
