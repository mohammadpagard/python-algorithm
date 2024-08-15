from ..rotate import rotate_string

class TestRotate:
    def test_rotate_string(self):
        assert rotate_string('Github', 3) == 'hubGit'
        assert rotate_string('Github', 6) == 'Github'
        assert rotate_string('Github', 7) == 'ithubG'
        assert rotate_string('Github', -1) == ''
        assert rotate_string('Github', -3) == ''
        assert rotate_string('', 3) == ''
        assert rotate_string('', -3) == ''
