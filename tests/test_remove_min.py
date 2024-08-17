from ..remove_min import remove_min


class TestRemoveMin:
    def test_remove_min(self):
        assert remove_min([4, 5, 2, 8, -2, 5, 1, 9]) == -2
        assert remove_min([0, -9, 4, 5, 2, 8, -2]) == -9
        assert remove_min([0, 4, 5, 2, 8]) == 0
        assert remove_min([1]) == 1
        assert remove_min([]) == 0
