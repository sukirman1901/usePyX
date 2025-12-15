from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import md_bold, make_code_block

def routing_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Core Concepts", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Routing").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("Routing").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Routing maps URLs to your PyX page functions. PyX uses a simple, explicit routing API.").text("lg").text("gray-600").mb(8))

    # 1. Basic Routing
    content.add(UI.h2("1. Basic Routing").text("2xl").font("bold").text("gray-900").mb(4).id("basic"))
    content.add(UI.p("Routes are defined in your main application file (usually `main.py` or `app.py`) using the `app.add_page()` method.").text("gray-600").mb(4))
    
    code_basic = '''
def home_page():
    return ui.text("Welcome Home")

def about_page():
    return ui.text("About Us")

app = pyx.App()

# Map routes to functions
app.add_page("/", home_page)
app.add_page("/about", about_page)
'''
    content.add(make_code_block(code_basic))

    # 2. Dynamic Routing (Conceptual / Future)
    # Assuming basic dynamic routing using standard {param} syntax common in web frameworks
    content.add(UI.h2("2. Dynamic Routes").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("dynamic"))
    content.add(UI.p("You can create dynamic routes by using curly braces `{}` in the route path. The parameters will be passed to your page function.").text("gray-600").mb(4))
    
    code_dyn = '''
def user_profile(user_id):
    return ui.text(f"Profile for user: {user_id}")

# Route with a parameter
app.add_page("/user/{user_id}", user_profile)
'''
    content.add(make_code_block(code_dyn))
    
    content.add(UI.div().cls("bg-yellow-50 border-l-4 border-yellow-400 p-4 mt-4 mb-6").add(
        UI.p().add(md_bold("Note: Dynamic routing support depends on the underlying Granian/Starlette configuration. Ensure your handlers accept the arguments.")).text("sm").text("yellow-700")
    ))

    # 3. Navigation
    content.add(UI.h2("3. Navigation").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("navigation"))
    content.add(UI.p("To navigate between pages, use standard HTML `<a>` tags or the `UI.a()` helper (or `ui.link` if preferred).").text("gray-600").mb(4))
    
    code_nav = '''
# Simple Link
ui.a("Go to About", href="/about")

# Styled Link (Button-like)
ui.a("View Profile", href="/user/123").cls("bg-blue-600 text-white px-4 py-2 rounded")
'''
    content.add(make_code_block(code_nav))

    # Layout
    toc_items = ["Routing", "Basic Routing", "Dynamic Routes", "Navigation"]
    return docs_layout(content, active_nav_item="Routing", toc_items=toc_items)
