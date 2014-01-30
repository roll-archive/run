from .function import FunctionTask

class MethodTask(FunctionTask):
    
    #Public
    
    def __init__(self, method, *args, **kwargs):
        super().__init__(method, *args, **kwargs)
        
    def effective_invoke(self, *args, **kwargs):
        return self._function(self.meta_module, *args, **kwargs)