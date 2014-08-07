from ..task import TaskPrototype, build
from .spawn import spawn


class ModulePrototype(TaskPrototype):

    # Protected

    _TaskPrototype = TaskPrototype

    def _create_task(self):
        spawned_class = spawn(self._class)
        task = spawned_class.__create__(self)
        return task

    def _initiate_task(self, task, module):
        for name in dir(type(task)):
            attr = getattr(type(task), name)
            if isinstance(attr, self._TaskPrototype):
                nested_task = build(attr, task)
                setattr(type(task), name, nested_task)
        return super()._initiate_task(task, module)

    def _update_task(self, task):
        for nested_task in task.meta_tasks.values():
            nested_task.__update__()
        return super()._update_task(task)
