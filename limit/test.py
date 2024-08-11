import unittest
import pytest
from .limit import limit_struct


class TestLimit:
    def test_limit_struct(self):
        assert limit_struct([1, 2, 3, 4, 5], min=3) == [3, 4, 5]
        assert limit_struct([1, 2, 3, 4, 5], max=3) == [1, 2, 3]
        assert limit_struct([1, 2, 3, 4, 5], min=3, max=3) == [3]
        assert limit_struct([]) == []
