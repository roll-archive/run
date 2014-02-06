from copy import copy
from .update import AttributeBuilderSet

class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        super().__setattr__('_class', cls)
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)
        super().__setattr__('_updates', [])
        
    def __call__(self, *args, **kwargs):
        obj = self._create_object()
        self._init_object(obj, *args, **kwargs)
        self._update_object(obj)
        return obj
    
    def __getattr__(self, name):
        try:
            return getattr(self._class, name)
        except AttributeError:
            raise AttributeError(name)
        
    def __setattr__(self, name, value):
        self._updates.append(self._set_class(name, value))     
    
    #Protected
    
    _set_class = AttributeBuilderSet
             
    def _create_object(self):
        return object.__new__(self._class)
        
    def _init_object(self, obj, *args, **kwargs):
        eargs = self._args+args
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        ekwargs.update({'builder': self})
        module = ekwargs.pop('module', None)
        obj.__system_prepare__(*eargs, **ekwargs)
        if module != True:
            obj.__system_bind__(module)
            obj.__system_init__()
            obj.__system_ready__()
     
    def _update_object(self, obj):
        for update in self._updates:
            update.apply(obj)