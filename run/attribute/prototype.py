from copy import copy
from .update import AttributeSet

class AttributePrototype:

    #Public
    
    def __init__(self, cls, updates, *args, **kwargs):
        super().__setattr__('_class', cls)
        super().__setattr__('_updates', updates)        
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)   
        if self._updates == None:
            super().__setattr__('_updates', []) 
    
    def __getattr__(self, name):
        try:
            return getattr(self._class, name)
        except AttributeError:
            raise AttributeError(                
                'AttributePrototype "{prototype}" has no attribute "{name}"'.
                format(prototype=self, name=name))
        
    def __setattr__(self, name, value):
        self._updates.append(self._set_class(name, value))
     
    def __call__(self, module):
        """Build attribute"""
        attribute = self._create_attribute()
        self._init_attribute(attribute, module)
        self._update_attribute(attribute)
        return attribute
        
    def __copy__(self):
        """Copy prototype"""
        return type(self)(
            self._class, copy(self._updates), 
            *self._args, **self._kwargs)
     
    #Protected
    
    _set_class = AttributeSet
          
    def _create_attribute(self):
        return object.__new__(self._class)
        
    def _init_attribute(self, attribute, module):
        attribute.__meta_init__(module, *self._args, **self._kwargs)
        
    def _update_attribute(self, attribute):
        for update in self._updates:
            update.apply(attribute)