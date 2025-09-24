from abc import ABC, abstractmethod

class Todo(ABC):
    # constructor
    def __init__(self,id,priority,name):
        self._id=id
        self._priority=priority
        self._name=name

    def __str__(self):
        return f"id:{self._id},priority:{self._priority},name:{self._name}"
    # dictionary function to convert python object to dictionary
    def to_dict(self):
        return{
            "id":self._id,
            "priority":self._priority,
            "name":self._name
        }