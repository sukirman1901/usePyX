from pyx import State

class CounterState(State):
    """
    Model (State): Holds the reactive data.
    """
    count: int = 0
