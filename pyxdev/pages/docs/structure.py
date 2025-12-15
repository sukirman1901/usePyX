from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import md_bold, make_code_block

def structure_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Getting Started", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Structure").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Title
    content.add(UI.h1("Project Structure").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("As your PyX application grows, it's essential to organize your code effectively. PyX encourages a modular, MVC-like structure.").text("lg").text("gray-600").mb(8))

    # Tree View
    content.add(UI.h2("Recommended Layout").text("2xl").font("bold").text("gray-900").mb(4).id("layout"))
    
    tree = '''
my_app/
├── assets/             # Static files (images, css, js)
├── components/         # Reusable UI components
│   ├── __init__.py
│   ├── navbar.py
│   └── footer.py
├── pages/              # Page view functions
│   ├── __init__.py
│   ├── home.py
│   └── dashboard.py
├── state/             # Global state management (Optional)
│   ├── __init__.py
│   └── auth_state.py
├── main.py             # App entry point & Routing
└── requirements.txt
'''
    content.add(make_code_block(tree, language="bash")) # bash styling looks good for trees

    # Descriptions
    content.add(UI.h2("Key Directories").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("directories"))
    
    def item_desc(name, desc):
        row = UI.div().cls("flex flex-col md:flex-row gap-2 md:gap-8 mb-6")
        row.add(PyxElement("code").add(name).cls("text-sm font-mono text-pink-600 bg-gray-50 px-2 py-1 rounded w-fit h-fit whitespace-nowrap"))
        row.add(UI.p(desc).text("gray-600"))
        return row

    content.add(item_desc("main.py", "The entry point of your application. This is where you initialize `app = pyx.App()`, import your pages, and define routes. Keep this file clean."))
    content.add(item_desc("pages/", "Contains your page view functions. Each file usually corresponds to a specific route or section of your app (e.g., `home.py`, `about.py`)."))
    content.add(item_desc("components/", "Reusable UI parts like Navbars, Sidebars, Cards, or complex widgets. Importing them into pages keeps your page logic clean."))
    content.add(item_desc("assets/", "Store static assets like images, custom CSS files, or favicons here."))

    # Modularization Tip
    tip_box = UI.div().cls("bg-blue-50 border border-blue-100 rounded-xl p-6 mt-8")
    tip_box.add(UI.h4("💡 Best Practice: Explicit Imports").font("bold").text("blue-900").mb(2))
    tip_box.add(UI.p("Always use explicit imports when structuring your app to avoid circular dependencies.").text("blue-800").text("sm"))
    tip_box.add(PyxElement("code").add("from components.navbar import navbar").cls("block mt-2 bg-blue-100 text-blue-900 p-2 rounded text-xs font-mono"))
    content.add(tip_box)

    # Layout
    toc_items = ["Project Structure", "Recommended Layout", "Key Directories"]
    return docs_layout(content, active_nav_item="Project Structure", toc_items=toc_items)
