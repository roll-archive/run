from .partial import PartialTask

class NestedTask(PartialTask):

    #Public
        
    def __init__(self, task, *args, merge=False, **kwargs):
        self._task_name = task
        self._merge = merge
        super().__init__(*args, **kwargs)       

    def effective_invoke(self, *args, **kwargs):
        if self._merge:
            #Invoke without resolving requirements, triggers
            result = self._task.invoke(*args, **kwargs)
        else:
            result = self._task(*args, **kwargs)
        return result
        
    @property
    def meta_signature(self):
        return self._task.meta_signature

    @property
    def meta_docstring(self):
        return self._task.meta_docstring
    
    #Protected
    
    @property
    def _task(self):
        task = getattr(self.meta_module, self._task_name)
        if self._merge:
            #Rebuild task with rebase on nested task module
            #TODO: use build
            task = task.meta_builder(module=self.meta_module)
        return task    