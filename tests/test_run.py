import unittest
from run import Run, Module, Task, Var

#Tests

class RunTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.run = MockRun()
        
    def test_help(self):
        self.run.help()
        
        
#Fixtures

class MockModule(Module):
    
    #Protected
    
    module_var = True
    

class MockTask(Task):
    
    #Protected
    
    def complete(self, *args, **kwargs):
        pass
    
    
class MockVar(Var):
    
    #Protected
    
    def retrieve(self, *args, **kwargs):
        pass    


class MockRun(Run):

    #Public
    
    module = MockModule()

    task = MockTask()
    var = MockVar()
    
    value_var = True
    
    def method_task(self):
        pass
    
    @property
    def property_var(self):
        pass
    
    class class_var:
        pass