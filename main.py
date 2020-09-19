from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List

class Subject(ABC):
    def addObserver(self,observer):
        pass
    def removeObserver(self,observer):
        pass
    def notifyObservers(self):
        pass
    
class ConcreteSubject(Subject):
    _observers = []
    
    _state = "my current state"
    
    def addObserver(self,observer):
        self._observers.append(observer)
    
    def removeObserver(self,observer):
        self._observers.remove(observer)
    
    def notifyObservers(self):
        for observer in self._observers:
            observer.update()
            
    def dosomething(self):
        print("I am doing something which will change my state ")
        self._state = "subject state has been changed"
        print("notifying observers")
        self.notifyObservers()
            
            
class Observer(ABC):
    def update(self):
        pass
    
class ConcreteObserver(Observer):
    def __init__(self,subject):
        self._subject = subject
        
    def update(self):
        print(self._subject._state)
        
concretesubject = ConcreteSubject()
observer1 = ConcreteObserver(concretesubject)
observer2 = ConcreteObserver(concretesubject)

concretesubject.addObserver(observer1)
concretesubject.addObserver(observer2)


concretesubject.dosomething()








        
    
    
    
    
