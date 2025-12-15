from .state import CounterState
import pyx

class CounterController:
    """
    Controller: Holds business logic and updates State.
    """
    
    @staticmethod
    def increment():
        CounterState.count += 1
        print(f"Count incremented to: {CounterState.count}")
        
    @staticmethod
    def decrement():
        CounterState.count -= 1
