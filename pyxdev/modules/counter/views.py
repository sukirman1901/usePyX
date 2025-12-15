from pyx.ui import UI
from pyx.components import PyxUI
from .state import CounterState
from .controller import CounterController

def counter_view():
    """
    View: Pure UI function bound to State and Controller.
    """
    return PyxUI.Card([
        PyxUI.CardHeader([
            PyxUI.CardTitle("MVC Counter Demo"),
            PyxUI.CardDescription("This component is built using Modular MVC architecture.")
        ]),
        PyxUI.CardContent([
            UI.div([
                PyxUI.Button("-", variant="outline", onClick=CounterController.decrement),
                
                # Direct binding to State variable
                UI.span(CounterState.count).className("text-4xl font-mono font-bold mx-8"),
                
                PyxUI.Button("+", onClick=CounterController.increment)
            ], className="flex items-center justify-center py-8")
        ])
    ], className="w-full max-w-md mx-auto mt-10")
