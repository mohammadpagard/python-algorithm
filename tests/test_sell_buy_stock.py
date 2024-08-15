from ..sell_buy_stock import max_profit

class TestSellBuyStock:
    def test_max_profit(self):
        assert max_profit([7, 1, 5, 3, 6, 4]) == 5
        assert max_profit([9, 7, 6, 4, 3, 1]) == 0
        assert max_profit([-1, -3, -6]) == 0
        assert max_profit([]) == 0
        assert max_profit([1, 1]) == 0
