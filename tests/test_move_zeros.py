from ..move_zeros import move_zeros

class TestMoveZeros:
    def test_move_zeros(self):
        assert move_zeros([0, False, 1, 0, 1, 2, 0, 1, 3, 'python', 0]) == [False, 1, 1, 2, 1, 3, 'python', 0, 0, 0, 0]
        assert move_zeros([True, 9, 0, 0, 0, -2, -4, 'Sri Lanka']) == [True, 9, -2, -4, 'Sri Lanka', 0, 0, 0]
        assert move_zeros([2, 1, 9, -4, 'GNU']) == [2, 1, 9, -4, 'GNU']
        assert move_zeros([0]) == [0]
        assert move_zeros([]) == []

