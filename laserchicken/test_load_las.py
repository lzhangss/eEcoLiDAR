import os
import shutil
import unittest

import pytest

from laserchicken.load_las import load


class TestLoadLas(unittest.TestCase):
    _test_dir = 'TestLoad_dir'
    _test_file_name = '5points.las'
    _test_data_source = 'testdata'
    test_file_path = os.path.join(_test_dir, _test_file_name)

    def test_load_contains_x(self):
        """ Should run without exception and return points with x attributes. """
        target = os.path.join(self._test_dir, 'target.ply')
        o = load(self.test_file_path)
        self.assertIn('points', o)
        self.assertIn('x', o['points'])

    def test_load_nonexistentFile(self):
        """ Should raise exception. """
        with pytest.raises(FileNotFoundError):
            load('nonexistent.las')

    def setUp(self):
        os.mkdir(self._test_dir)
        shutil.copyfile(os.path.join(self._test_data_source, self._test_file_name), self.test_file_path)

    def tearDown(self):
        shutil.rmtree(self._test_dir)