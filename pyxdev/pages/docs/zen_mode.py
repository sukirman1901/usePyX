from pyx.ui import UI, PyxElement, ui
from components.layout import docs_layout
from components.ui_helpers import md_bold, make_code_block

def zen_mode_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Core Concepts", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Zen Mode").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("Zen Mode UI").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Zen Mode is the idiomatic way to build user interfaces in PyX. It uses Python's `with` statements (context managers) to represent the hierarchy of your UI components visually in your code.").text("lg").text("gray-600").mb(8))

    # 1. The Concept
    content.add(UI.h2("The Concept").text("2xl").font("bold").text("gray-900").mb(4).id("concept"))
    content.add(UI.p("In traditional frameworks, you often pass children as a list argument or chain methods endlessly. In PyX Zen Mode, indentation defines structure.").text("gray-600").mb(6))

    # Comparison Tabs (Standard vs Zen)
    # Reusing the Clean Tabs Logic (inline script for simplicity in this page too, or we could move it to layout global script later)
    
    # Simple Tabs Implementation for Comparison
    tab_script = """
    function openZenTab(evt, tabId) {
        var i, contents, links;
        contents = document.getElementsByClassName("zen-tab-content");
        for (i = 0; i < contents.length; i++) { contents[i].style.display = "none"; }
        
        links = document.getElementsByClassName("zen-tab-link");
        for (i = 0; i < links.length; i++) { 
            links[i].className = links[i].className.replace(" border-blue-600 text-blue-600", " border-transparent text-gray-500");
        }
        
        document.getElementById(tabId).style.display = "block";
        evt.currentTarget.className = evt.currentTarget.className.replace(" border-transparent text-gray-500", " border-blue-600 text-blue-600");
    }
    """
    content.add(PyxElement("script").add(tab_script))
    
    tabs = UI.div().cls("flex border-b border-gray-200 mb-4")
    def tab_btn(label, target, active=False):
        cls = "zen-tab-link py-2 px-4 text-sm font-medium border-b-2 transition-colors duration-200 focus:outline-none bg-transparent cursor-pointer"
        active_cls = " border-blue-600 text-blue-600" if active else " border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
        btn = PyxElement("button").add(label).cls(cls + active_cls)
        btn.attr("onclick", f"openZenTab(event, '{target}')")
        return btn

    tabs.add(tab_btn("Zen Mode (Recommended)", "code-zen", active=True))
    tabs.add(tab_btn("Standard / Chained", "code-standard"))
    content.add(tabs)

    # Zen Code
    code_zen = '''
with ui.card().p(8).shadow("lg"):
    ui.title("Welcome Back")
    
    with ui.vstack().gap(4):
        ui.input(placeholder="Email")
        ui.input(placeholder="Password", type="password")
        
        with ui.hstack().justify_end():
            ui.button("Login").bg("blue-600")
'''
    div_zen = UI.div().id("code-zen").cls("zen-tab-content")
    div_zen.add(make_code_block(code_zen))
    content.add(div_zen)

    # Standard Code
    code_standard = '''
# Without context managers, structure is less visible
card = ui.card().p(8).shadow("lg")
card.add(ui.title("Welcome Back"))

form = ui.vstack().gap(4)
form.add(ui.input(placeholder="Email"))
form.add(ui.input(placeholder="Password", type="password"))

actions = ui.hstack().justify_end()
actions.add(ui.button("Login").bg("blue-600"))

form.add(actions)
card.add(form)
'''
    div_std = UI.div().id("code-standard").cls("zen-tab-content hidden").attr("style", "display:none")
    div_std.add(make_code_block(code_standard))
    content.add(div_std)


    # 2. Supported Components
    content.add(UI.h2("Supported Components").text("2xl").font("bold").text("gray-900").mt(12).mb(4).id("components"))
    content.add(UI.p("Most layout components in PyX support Zen Mode:").text("gray-600").mb(4))
    
    grid = UI.div().cls("grid grid-cols-2 md:grid-cols-3 gap-4")
    comps = ["ui.div", "ui.row", "ui.col", "ui.card", "ui.center", "ui.vstack", "ui.hstack", "ui.grid", "ui.form"]
    for c in comps:
        grid.add(UI.div().cls("bg-gray-50 border border-gray-200 rounded p-3 text-sm font-mono text-pink-600 text-center").add(c))
    content.add(grid)

    # 3. Mixing Styles
    content.add(UI.h2("Mixing Styles").text("2xl").font("bold").text("gray-900").mt(12).mb(4).id("mixing"))
    content.add(UI.p("You can mix Zen Mode with standard method chaining. For example, leaf nodes (like buttons or inputs) are usually one-liners, while containers use `with`.").text("gray-600").mb(4))
    
    mix_code = '''
with ui.row().items_center().justify_between().p(4).bg("white"):
    # Leaf node (one-liner)
    ui.title("Dashboard").text("xl")
    
    # Leaf node
    ui.button("Settings").variant("outline")
'''
    content.add(make_code_block(mix_code))

    # Layout
    toc_items = ["Zen Mode UI", "The Concept", "Supported Components", "Mixing Styles"]
    return docs_layout(content, active_nav_item="Zen Mode", toc_items=toc_items)
