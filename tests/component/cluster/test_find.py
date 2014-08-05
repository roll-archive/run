import unittest
from unittest.mock import Mock, ANY
from run.cluster.find import find

class find_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.find = self._make_mock_find()

    def test(self):
        result = self.find()
        self.assertEqual(result, self.find._find_objects.return_value)
        # Check find_objects call
        self.find._find_objects.assert_called_with(
            basedir='default_basedir',
            filename='default_file',
            notfilename='default_exclude',
            filepath=None,
            notfilepath=None,
            maxdepth=None,
            mappers=ANY,
            getfirst_exception=self.find._getfirst_exception)

    def test_with_filenames(self):
        self.find(
            file='file',
            exclude='exclude')
        # Check find_objects call
        self.find._find_objects.assert_called_with(
            basedir='default_basedir',
            filename='file',
            notfilename='exclude',
            filepath=None,
            notfilepath=None,
            maxdepth=None,
            mappers=ANY,
            getfirst_exception=self.find._getfirst_exception)

    def test_with_filepathes_not_recursively(self):
        self.find(
            file='dir/file',
            exclude='dir/exclude',
            recursively=False)
        # Check find_objects call
        self.find._find_objects.assert_called_with(
            basedir='default_basedir',
            filename=None,
            notfilename=None,
            filepath='dir/file',
            notfilepath='dir/exclude',
            maxdepth=None,
            mappers=ANY,
            getfirst_exception=self.find._getfirst_exception)

    # Protected

    def _make_mock_find(self):
        class mock_find(find):
            # Public
            default_basedir = 'default_basedir'
            default_exclude = 'default_exclude'
            default_file = 'default_file'
            default_names = 'default_names'
            default_recursively = 'default_recursively'
            default_tags = 'default_tags'
            # Protected
            _find_objects = Mock()
        return mock_find
