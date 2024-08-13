from ..two_sum import two_sum_sorted

class TestTwoSum:
    def test_two_sum_sorted(self):
        assert two_sum_sorted([1, 3, 4, 5, 6, 6, 7], 13) == "6 + 7 = 13"
        assert two_sum_sorted([1, 3, 4, 5, 6, 6, 7], 18) == "So, you couldn't fund your target in this list..."
        assert two_sum_sorted([1, 2], 3) == "1 + 2 = 3"
        assert two_sum_sorted([], 3) == "So, you couldn't fund your target in this list..."
        assert two_sum_sorted([1, 3, 4, 5 , 6, 6, 7], 0) == "So, you couldn't fund your target in this list..."
