import pyx
from pyx.ui import UI, PyxElement
from pyx.components import PyxUI
from components.layout import docs_layout, Lucide
from components.ui_helpers import md_bold, make_code_block
from pyx.client import JS

def components_page():
    content = UI.div()
    
    # Header
    content.add(UI.h1("Components").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("PyX comes with a built-in premium component library inspired by Shadcn UI. These components are accessible, customizable, and ready to use.").text("lg").text("gray-600").mb(8))

    # Import
    content.add(UI.h3("Import").text("xl").font("bold").text("gray-900").mb(4))
    content.add(make_code_block('from pyx.components import PyxUI'))
    
    # --- BUTTONS ---
    content.add(UI.h2("Button").text("2xl").font("bold").mt(12).mb(4).id("button"))
    
    btn_demo = UI.div().flex().flex_wrap().gap(4).p(6).border().rounded("lg").mb(4)
    btn_demo.add(PyxUI.Button("Default"))
    btn_demo.add(PyxUI.Button("Secondary", variant="secondary"))
    btn_demo.add(PyxUI.Button("Destructive", variant="destructive"))
    btn_demo.add(PyxUI.Button("Outline", variant="outline"))
    btn_demo.add(PyxUI.Button("Ghost", variant="ghost"))
    btn_demo.add(PyxUI.Button("Link", variant="link"))
    content.add(btn_demo)
    
    content.add(make_code_block('''
PyxUI.Button("Default")
PyxUI.Button("Secondary", variant="secondary")
PyxUI.Button("Destructive", variant="destructive")
    '''))

    # --- CARD ---
    content.add(UI.h2("Card").text("2xl").font("bold").mt(12).mb(4).id("card"))
    
    card_demo = UI.div().p(6).border().rounded("lg").bg("gray-50").mb(4)
    card_demo.add(
        PyxUI.Card([
            PyxUI.CardHeader([
                PyxUI.CardTitle("Notification"),
                PyxUI.CardDescription("You have 3 unread messages.")
            ]),
            PyxUI.CardContent([
                UI.p("This is the content of the card.").text("sm").text("gray-600")
            ]),
            PyxUI.CardFooter([
                PyxUI.Button("Mark all as read", className="w-full")
            ])
        ], className="max-w-[380px]")
    )
    content.add(card_demo)
    
    content.add(make_code_block('''
PyxUI.Card([
    PyxUI.CardHeader([
        PyxUI.CardTitle("Notification"),
        PyxUI.CardDescription("You have 3 unread messages.")
    ]),
    PyxUI.CardContent([ ... ]),
    PyxUI.CardFooter([ ... ])
])
    '''))

    # --- FORMS ---
    content.add(UI.h2("Forms").text("2xl").font("bold").mt(12).mb(4).id("forms"))
    
    form_demo = UI.div().grid().cols(1).gap(4).max_w("md").p(6).border().rounded("lg").mb(4)
    form_demo.add(PyxUI.Label("Email"))
    form_demo.add(PyxUI.Input(placeholder="user@example.com", type="email"))
    form_demo.add(PyxUI.Label("Bio"))
    form_demo.add(PyxUI.Textarea(placeholder="Tell us about yourself"))
    form_demo.add(PyxUI.div([
        PyxUI.Checkbox(),
        PyxUI.Label("Accept terms", className="ml-2")
    ], className="flex items-center"))
    content.add(form_demo)
    
    content.add(make_code_block('''
PyxUI.Input(placeholder="Email")
PyxUI.Textarea(placeholder="Message")
PyxUI.Checkbox()
    '''))
    
    # --- INTERACTIVE ---
    content.add(UI.h2("Interactive").text("2xl").font("bold").mt(12).mb(4).id("interactive"))
    
    inter_demo = UI.div().flex().gap(4).p(6).border().rounded("lg").mb(4)
    
    # Dialog
    dialog = PyxUI.Dialog(
        "demo-dialog",
        PyxUI.Button("Open Dialog"),
        "Edit Profile",
        UI.div("Make changes to your profile here."),
        footer=PyxUI.Button("Save Changes", onClick=JS.close_dialog("demo-dialog")) # Hypothetical helper
    )
    
    # Sheet
    sheet = PyxUI.Sheet(
        "demo-sheet",
        PyxUI.Button("Open Sidebar", variant="outline"),
        "Menu",
        UI.div([
            PyxUI.Button("Home", variant="ghost", className="w-full justify-start"),
            PyxUI.Button("Settings", variant="ghost", className="w-full justify-start"),
        ]),
        side="right"
    )
    
    inter_demo.add(dialog)
    inter_demo.add(sheet)
    content.add(inter_demo)

    toc_items = ["Button", "Card", "Forms", "Interactive"]
    return docs_layout(content, active_nav_item="Components", toc_items=toc_items, title="Components")
