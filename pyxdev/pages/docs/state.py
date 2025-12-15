from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import md_bold, make_code_block

def state_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Core Concepts", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("State Management").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("State Management").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("State allows your application to be interactive. When the state changes, the UI updates automatically.").text("lg").text("gray-600").mb(8))

    # 1. State Basics
    content.add(UI.h2("1. The State Class").text("2xl").font("bold").text("gray-900").mb(4).id("basics"))
    content.add(UI.p("In PyX, state is typically organized in classes that inherit from `pyx.State`. Variables defined in these classes become reactive.").text("gray-600").mb(4))
    
    code_state = '''
import pyx

class CounterState(pyx.State):
    # Reactive variable
    count: int = 0
    
    # Event Handler
    def increment(self):
        self.count += 1
'''
    content.add(make_code_block(code_state))

    # 2. Binding to UI
    content.add(UI.h2("2. Binding to UI").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("binding"))
    content.add(UI.p("You can bind state variables directly to UI components. PyX handles the synchronization.").text("gray-600").mb(4))
    
    code_bind = '''
def index():
    # Pass the variable, not the value!
    ui.heading(CounterState.count)
    
    # Bind handlers
    ui.button("Increment", on_click=CounterState.increment)
'''
    content.add(make_code_block(code_bind))

    # 3. Events
    content.add(UI.h2("3. Events").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("events"))
    content.add(UI.p("Event handlers are methods within your State class. They can modify state variables, triggering UI updates.").text("gray-600").mb(4))
    
    content.add(UI.div().cls("bg-blue-50 border border-blue-200 rounded-lg p-4").add(
        UI.p("All state updates run on the server. The updated UI is sent to the client via WebSockets (Granian). This keeps your logic secure and Python-native.").text("blue-800")
    ))

    # Layout
    toc_items = ["State Management", "The State Class", "Binding to UI", "Events"]
    return docs_layout(content, active_nav_item="State Management", toc_items=toc_items)
