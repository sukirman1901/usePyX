from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import md_bold, make_code_block

def quickstart_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Getting Started", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Quick Start").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Title
    content.add(UI.h1("Quick Start").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Get up and running with PyX in less than 5 minutes.").text("lg").text("gray-600").mb(8))

    # 1. Prerequisites (Short)
    content.add(UI.h2("1. Prerequisites").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("prereq"))
    content.add(UI.p().add("Ensure you have Python 3.9+ installed.").text("gray-600").mb(2))
    content.add(UI.a("Full Installation Guide ->", "/docs/installation").text("blue-600").font("medium").hover("underline").mb(4).block())

    # 2. Create Hello World
    content.add(UI.h2("2. Create Your First App").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("create"))
    content.add(UI.p("Create a file named ").add(PyxElement("code").add("app.py").cls("bg-gray-100 px-1 py-0.5 rounded text-sm font-mono text-pink-500")).add(" and paste the following code:").text("gray-600").mb(4))

    code_hello = '''
import pyx
from pyx.ui import ui

app = pyx.App()

def index():
    # Zen Mode UI: Simple, Declartive, Pythonic
    root = ui.page()
    
    with ui.center().h_screen().bg("gray-50"):
        with ui.card().p(8).shadow("lg").bg("white").gap(4):
            ui.title("Hello, World! 🌍").text("3xl")
            ui.text("Welcome to your first PyX app.").text("gray-500")
            ui.button("Click Me").bg("blue-600").text("white")
            
    return root

app.add_page("/", index)
'''
    content.add(make_code_block(code_hello))
    
    # 3. Run It
    content.add(UI.h2("3. Run It").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("run"))
    content.add(UI.p("Run the app using the PyX CLI:").text("gray-600").mb(4))
    content.add(make_code_block("pyx run app.py", language="bash"))
    
    content.add(UI.div().cls("bg-green-50 border border-green-200 rounded-lg p-4 mt-6").add(
        UI.p("🎉 Success! Your app is running at http://localhost:8020").text("green-800").font("medium")
    ))

    # Next Steps
    content.add(UI.h2("What's Next?").text("2xl").font("bold").text("gray-900").mt(12).mb(4).id("next"))
    cards = UI.div().cls("grid grid-cols-1 md:grid-cols-2 gap-6")
    
    def next_card(title, desc, href):
        c = PyxElement("a").attr("href", href).block().cls("group p-6 border border-gray-200 rounded-xl hover:border-blue-500 hover:shadow-md transition-all duration-200")
        c.add(UI.h4(title).text("lg").font("bold").text("gray-900").group_hover("text-blue-600").mb(2))
        c.add(UI.p(desc).text("gray-600").text("sm"))
        return c

    cards.add(next_card("App Structure", "Learn how to organize larger PyX projects.", "/docs/structure"))
    cards.add(next_card("Core Concepts", "Understand State, Routing, and Components.", "/docs/introduction"))
    
    content.add(cards)

    # Layout
    toc_items = ["Quick Start", "Prerequisites", "Create App", "Run It", "What's Next?"]
    return docs_layout(content, active_nav_item="Quick Start", toc_items=toc_items)
