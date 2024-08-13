from ..top_one import top_one


class TestTopOne:
    def test_top_one(self):
        assert top_one([1, 2, 1, 3, 4, 2, 2, 2]) == ([1, 2], 4)
        assert top_one([1]) == ([], 1)
        assert top_one([1, 2]) == ([], 1)
        assert top_one([]) == ()
