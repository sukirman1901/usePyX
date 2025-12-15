from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import md_bold, make_code_block

def ui_overview_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("User Interface", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Overview").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("User Interface").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("PyX comes with a comprehensive suite of UI components to build modern web applications quickly.").text("lg").text("gray-600").mb(8))

    # Component Categories taking user to specific docs
    categories = [
        ("Typography", "Headings, Text, Prose", "type", "/docs/ui/typography"),
        ("Forms", "Input, Select, Checkbox, Button", "edit-3", "/docs/ui/forms"),
        ("Layout", "Flex, Grid, Container, Stack", "layout", "/docs/ui/layout"),
        ("Feedback", "Alerts, Spinners, Toast", "bell", "/docs/ui/feedback"),
        ("Overlay", "Modals, Popovers, Tooltips", "maximize", "/docs/ui/overlay"),
        ("Data Display", "Tables, Lists, Cards", "list", "/docs/ui/data-display")
    ]
    
    grid = UI.div().cls("grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6")
    
    for title, desc, icon, href in categories:
        # If href is valid (not #), make it clickable
        if href != "#":
            card = PyxElement("a").attr("href", href).block().cls("p-6 border border-gray-200 rounded-xl hover:border-blue-500 hover:shadow-md transition-all cursor-pointer group bg-white")
        else:
            card = UI.div().cls("p-6 border border-gray-200 rounded-xl opacity-60 cursor-not-allowed bg-gray-50")
            
        card.add(UI.div().cls("w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center mb-4 text-blue-600").add(PyxElement("i").attr("data-lucide", icon)))
        card.add(UI.h3(title).text("lg").font("bold").text("gray-900").mb(2).group_hover("text-blue-600"))
        card.add(UI.p(desc).text("gray-500").text("sm"))
        grid.add(card)
        
    content.add(grid)
    
    # Example
    content.add(UI.h2("Component Usage").text("2xl").font("bold").text("gray-900").mt(12).mb(4))
    content.add(UI.p("All components are available via the `ui` object. They support method chaining for styling.").text("gray-600").mb(4))
    
    code = '''
with ui.card().p(6).shadow("sm"):
    ui.heading("User Profile").text("xl")
    ui.text("Manage your settings").text("gray-500").mb(4)
    
    with ui.vstack().gap(3):
        ui.input(placeholder="Username")
        ui.button("Save Changes").bg("blue-600")
'''
    content.add(make_code_block(code))

    return docs_layout(content, active_nav_item="UI Overview", title="UI Overview")
