import unittest
from unittest.mock import Mock
from run.task.method import MethodTask

class MethodTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.function = Mock(return_value='value')
        self.task = MethodTask(self.function, module='module', build=True)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}        
        
    def test_invoke(self):        
        self.assertEqual(self.task.invoke(*self.args, **self.kwargs), 'value')
        self.function.assert_called_with('module', *self.args, **self.kwargs)