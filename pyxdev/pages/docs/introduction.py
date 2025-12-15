import pyx
from pyx.ui import UI, PyxElement
from components.layout import docs_layout, Lucide
from components.ui_helpers import md_bold, make_code_block

# -----------------------------------------------------------------------------
# LOCAL STATE FOR DEMO
# -----------------------------------------------------------------------------
def introduction_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Getting Started", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Introduction").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Title
    content.add(UI.h1("Introduction").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6).id("introduction"))
    
    # Intro Text
    intro_txt = "PyX is a new-generation, open-source framework for quickly building beautiful, interactive, and real-time web applications in **pure Python**."
    content.add(UI.p().add(md_bold(intro_txt)).text("lg").text("gray-600").mb(4))
    
    content.add(UI.p("PyX eliminates the pain of context switching and API boilerplate, allowing Python developers to build production-grade applications as fast as scripting, but with the quality and performance of enterprise-level tools.").text("lg").text("gray-600").mb(8))
    
    # Goals
    content.add(UI.h2("Goals").text("3xl").font("bold").text("gray-900").mb(6).id("goals"))
    
    # Feature 1
    content.add(UI.h3("Pure Python").text("xl").font("bold").text("gray-900").mb(2))
    content.add(UI.p("Use Python for everything. Don't worry about learning new languages like JavaScript, JSX, or dealing with complex bundlers.").text("gray-600").mb(6))
    
    # Feature 2
    content.add(UI.h3("Real-time by Design").text("xl").font("bold").text("gray-900").mb(2))
    content.add(UI.p().add(md_bold("The PyX architecture is **built on WebSockets** and the **Rust (Granian) engine**. This provides natively fast data updates, making it perfect for trading, live dashboards, or data monitoring.")).text("gray-600").mb(6))
    
    # Feature 3
    content.add(UI.h3("Easy to Learn (Zen Mode Simplicity)").text("xl").font("bold").text("gray-900").mb(2))
    zen_desc = 'Build and share your first app in minutes. With the imperative **Zen Mode** syntax (with `ui.card(): ui.title("Hello")`), you can build complex UIs without the nesting hell or complex class-based state management.'
    content.add(UI.p().add(md_bold(zen_desc)).text("gray-600").mb(8))
    
    # Example
    content.add(UI.p("An example: Make it count").text("lg").font("medium").text("gray-900").mb(4).id("example"))
    content.add(UI.p("Here, we go over a simple counter app that lets the user count up or down. TRY IT BELOW!").text("gray-600").mb(6))
    
    # Counter Demo (Interactive via Client-Side Logic for Docs Stability)
    demo = UI.div().flex().flex_col().sm("flex-row").items("center").gap(4).p(8).border("gray-200").cls("border-2").rounded("xl").bg("white").shadow("sm").mb(6).justify("center")
    
    # JS Handlers
    js_dec = "document.getElementById('demo-cnt').innerText = parseInt(document.getElementById('demo-cnt').innerText) - 1"
    js_inc = "document.getElementById('demo-cnt').innerText = parseInt(document.getElementById('demo-cnt').innerText) + 1"

    # Decrement Button
    demo.add(
        UI.button("Decrement", primary=False)
        .cls("bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600 active:bg-red-700 transition")
        .attr("style", "background-color: #ef4444") # Fallback
        .attr("onclick", js_dec)
    )
    
    # Count Display
    demo.add(
        UI.span("0").id("demo-cnt").text("6xl").font("mono")
    )
    
    # Increment Button
    demo.add(
        UI.button("Increment", primary=False)
        .cls("bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 active:bg-blue-700 transition")
        .attr("style", "background-color: #3b82f6") # Fallback
        .attr("onclick", js_inc)
    )
    content.add(demo)

    # Code Tabs Section - Clean Reflex-like Design
    content.add(UI.p("Here is the full code for this example, broken down by logic:").text("gray-600").mb(6))
    
    # Scripts for Tabs & Descriptions
    tab_script = """
    function openTab(evt, tabName, descId) {
        // 1. Hide all tab content
        var i, tabcontent;
        tabcontent = document.getElementsByClassName("code-tab-content");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }
        
        // 2. Hide all descriptions
        var descriptions = document.getElementsByClassName("tab-description");
        for (i = 0; i < descriptions.length; i++) {
            descriptions[i].style.display = "none";
        }

        // 3. Reset all tab links style
        var tablinks = document.getElementsByClassName("code-tab-link");
        for (i = 0; i < tablinks.length; i++) {
            // Remove active class (border-blue-600 text-blue-600)
            tablinks[i].className = tablinks[i].className.replace(" border-blue-600 text-blue-600", " border-transparent text-gray-500");
        }

        // 4. Show current tab content & description
        document.getElementById(tabName).style.display = "block";
        document.getElementById(descId).style.display = "block";
        
        // 5. Set active style to clicked tab
        evt.currentTarget.className = evt.currentTarget.className.replace(" border-transparent text-gray-500", " border-blue-600 text-blue-600");
    }
    """
    content.add(PyxElement("script").add(tab_script))

    # Tabs Header Container
    tabs = UI.div().cls("flex border-b border-gray-200 mb-6")
    
    def create_tab_btn(label, target_id, desc_id, active=False):
        # Clean Underline Style (Raw Button to avoid default UI.button styles)
        base_cls = "code-tab-link py-2 px-4 text-sm font-medium border-b-2 transition-colors duration-200 focus:outline-none bg-transparent cursor-pointer"
        active_cls = " border-blue-600 text-blue-600" if active else " border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
        
        btn = PyxElement("button").add(label).cls(base_cls + active_cls)
        btn.attr("onclick", f"openTab(event, '{target_id}', '{desc_id}')")
        return btn

    # Tabs Order: Frontend | Backend | Page (Full)
    tabs.add(create_tab_btn("Frontend", "tab-frontend", "desc-frontend", active=True))
    tabs.add(create_tab_btn("Backend", "tab-backend", "desc-backend"))
    tabs.add(create_tab_btn("Page", "tab-full", "desc-full"))
    content.add(tabs)

    # Dynamic Descriptions
    def create_desc(text, desc_id, active=False):
        d = UI.div().id(desc_id).cls("tab-description text-gray-600 mb-4 text-sm leading-relaxed")
        if not active: d.attr("style", "display:none")
        d.add(md_bold(text))
        return d

    content.add(create_desc("The **Frontend** is built declaratively using PyX UI components (Zen Mode). Data is bound directly to State variables.", "desc-frontend", active=True))
    content.add(create_desc("The **Backend** (State) holds your application logic and variables. It runs on the server and syncs with the frontend automatically via WebSockets.", "desc-backend"))
    content.add(create_desc("The **Page** combines backend state and frontend UI into a route. This is the entry point of your application.", "desc-full"))

    # Tab Contents
    
    # 1. Frontend
    frontend_code = '''
from pyx.ui import ui

def counter_page():
    """
    The UI is built using Python context managers (Zen Mode).
    Variables from State are bound automatically.
    """
    root = ui.page()
    
    with ui.vstack().items_center().gap(4):
        
        with ui.hstack().gap(4):
            # Bind click events to State methods
            ui.button("Decrement", on_click=CounterState.decrement)
            
            # Bind text directly to State variable
            ui.heading(CounterState.count).text("4xl")
            
            ui.button("Increment", on_click=CounterState.increment)

    return root
'''
    tab_front = UI.div().id("tab-frontend").cls("code-tab-content")
    tab_front.add(make_code_block(frontend_code))
    content.add(tab_front)

    # 2. Backend
    backend_code = '''
import pyx

class CounterState(pyx.State):
    """
    The State class holds all the variables that change over time.
    """
    count: int = 0
    
    def increment(self):
        # State updates are as simple as modifying the variable.
        self.count += 1
        
    def decrement(self):
        self.count -= 1
'''
    tab_back = UI.div().id("tab-backend").cls("code-tab-content hidden").attr("style", "display:none")
    tab_back.add(make_code_block(backend_code))
    content.add(tab_back)

    # 3. Full App
    full_code = '''
import pyx
from pyx.ui import ui

# 1. Backend (State)
class CounterState(pyx.State):
    count: int = 0
    
    def increment(self):
        self.count += 1
        
    def decrement(self):
        self.count -= 1

# 2. Frontend (UI)
def counter_page():
    root = ui.page()
    
    with ui.vstack().items_center().gap(4).p(8):
        ui.heading("Counter App")
        
        with ui.hstack().gap(4):
            ui.button("Decrement", on_click=CounterState.decrement).bg("red-500")
            ui.heading(CounterState.count).text("4xl")
            ui.button("Increment", on_click=CounterState.increment).bg("blue-500")

    return root

app = pyx.App()
app.add_page("/", counter_page)
'''
    tab_full = UI.div().id("tab-full").cls("code-tab-content hidden").attr("style", "display:none")
    tab_full.add(make_code_block(full_code))
    content.add(tab_full)
    
    # Structure Section
    content.add(UI.h2("The Structure of a PyX App").text("3xl").font("bold").text("gray-900").mt(16).mb(6).id("structure"))
    content.add(UI.p("Let's break down the equivalent of the simple Counter App in PyX.").text("lg").text("gray-600").mb(4))
    content.add(UI.p("PyX is architected around Stateful Controllers and Zen Mode UI, simplifying the entire data flow.").text("lg").text("gray-600").mb(8))
    
    # 1. Import
    content.add(UI.h3("1. Import").text("xl").font("bold").text("gray-900").mb(4))
    content.add(UI.p().add(md_bold("We begin by importing the pyx package. By convention, we import the core UI engine as **ui** to access the clean Zen Mode syntax.")).text("gray-600").mb(4))
    import_code = '''
import pyx
from pyx.ui import ui
    '''
    content.add(make_code_block(import_code))
    
    # 2. State
    content.add(UI.h3("2. State (Model/Stateful Controller)").text("xl").font("bold").text("gray-900").mb(4))
    content.add(UI.p().add(md_bold("In PyX, the state can be managed in a dedicated **pyx.State** class (for simplicity) or directly within the Controller function (in a more complex Modular MVC setup).")).text("gray-600").mb(4))
    content.add(UI.p().add(md_bold("For a simple app, we use **pyx.State**: ")).text("gray-600").mb(4))
    state_code = '''
# Typically stored in modules/home/state.py or router.py

class CounterState(pyx.State):
    # 'count' is the state variable (var)
    count: int = 0
    '''
    content.add(make_code_block(state_code))
    
    # 3. Event Handlers
    content.add(UI.h3("3. Event Handlers (Controller Logic)").text("xl").font("bold").text("gray-900").mb(4))
    content.add(UI.p().add(md_bold("Event handlers are the functions that exclusively modify the state variables. In PyX, these are methods within the state class or plain functions within the Controller.")).text("gray-600").mb(4))
    handler_code = '''
# Event Handlers defined within the State Class

class CounterState(pyx.State):
    count: int = 0

    # Event Handler 1: Modifies the state var 'count'
    def increment(self):
        # State mutation is direct and immediate
        self.count += 1
        # The UI updates automatically (reactively) because the state changed.

    # Event Handler 2
    def decrement(self):
        self.count -= 1
    '''
    content.add(make_code_block(handler_code))
    
    # 4. UI
    content.add(UI.h3("4. User Interface (View / Zen Mode)").text("xl").font("bold").text("gray-900").mb(4))
    content.add(UI.p().add(md_bold("The UI is defined using the **Zen Mode** syntax, which uses Python context managers (`with`) instead of nested function calls, making it highly readable.")).text("gray-600").mb(4))
    ui_code = '''
# Typically stored in modules/home/views.py or router.py

def index():
    ui.page() # Initialize the page context

    # 1. Layout using Python's 'with' statements
    with ui.col().items("center").justify("center").min_h("screen"):
        with ui.row(gap=4):

            # Button 1: Decrement
            ui.button("Decrement") \\
                .on_click(CounterState.decrement) \\
                .bg("red-600").text("white")

            # Heading: References State.count
            ui.heading(CounterState.count) \\
                .text("3xl").font("bold")

            # Button 2: Increment
            ui.button("Increment") \\
                .on_click(CounterState.increment) \\
                .bg("green-600").text("white")

    return ui.get_root() # Return the final root element
    '''
    content.add(make_code_block(ui_code))
    
    # 5. Routing
    content.add(UI.h3("6. Add pages (Routing)").text("xl").font("bold").text("gray-900").mb(4))
    content.add(UI.p("Finally, we define the application structure and routing.").text("gray-600").mb(4))
    route_code = '''
import pyx

app = pyx.App()
# The 'index' function is added to the base route "/"
app.add_page("/", index)

if __name__ == "__main__":
    app.run()
    '''
    content.add(make_code_block(route_code))

    content.add(UI.p("🎉 And that's it! You've created a simple, fully interactive, and stateful web app in pure Python using the intuitive PyX Zen Mode.").text("lg").font("medium").text("gray-900").mb(8))

    # Next Steps
    content.add(UI.h2("Next Steps").text("xl").md("text-2xl").font("bold").text("gray-900").mt(12).mb(6).id("next-steps"))
    
    next_btns = UI.div().flex().flex_col().sm("flex-row").gap(4)
    next_btns.add(
        UI.a("Installation →", "/docs/installation")
            .block().text("center").bg("blue-600").text("white").px(6).py(3).rounded("lg")
            .font("medium").hover("bg-blue-700").transition()
    )
    next_btns.add(
        UI.a("Quick Start →", "/docs/quickstart")
            .block().text("center").bg("gray-100").text("gray-700").px(6).py(3).rounded("lg")
            .font("medium").hover("bg-gray-200").transition()
    )
    content.add(next_btns)
    
    # Build Final Page using Layout
    toc_items = ["Introduction", "Goals", "Example", ("App Structure", "#structure"), ("Next Steps", "#next-steps")]
    return docs_layout(content, active_nav_item="Introduction", toc_items=toc_items, title="Introduction")

