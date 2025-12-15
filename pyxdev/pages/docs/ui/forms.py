from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def forms_page():
    content = UI.div()
    
    # Breadcrumb
    content.add(UI.div().flex().gap(2).mb(4).add(UI.a("UI", "/docs/ui/overview").text("sm").text("gray-400")).add(UI.span("›").text("gray-400")).add(UI.span("Forms").text("sm").font("medium").text("gray-900")))
    
    content.add(UI.h1("Forms").text("3xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Input components for data entry.").text("lg").text("gray-600").mb(8))

    # Text Inputs
    content.add(UI.h2("Text Inputs").text("2xl").font("bold").mb(4))
    form_box = UI.div().cls("space-y-4 max_w-md p-6 border rounded-xl mb-8")
    form_box.add(UI.label("Email Address").cls("block text-sm font-medium text-gray-700"))
    form_box.add(UI.input(placeholder="you@example.com").cls("w-full border p-2 rounded focus:ring-2 focus:ring-blue-500 outline-none"))
    
    form_box.add(UI.label("Description").cls("block text-sm font-medium text-gray-700 mt-4"))
    form_box.add(PyxElement("textarea").attr("placeholder", "Tell us about yourself...").cls("w-full border p-2 rounded h-24 focus:ring-2 focus:ring-blue-500 outline-none"))
    content.add(form_box)
    
    content.add(make_code_block('ui.input(placeholder="Email").cls("w-full border p-2")'))

    # Select & Checkbox
    content.add(UI.h2("Select & Checkbox").text("2xl").font("bold").mb(4).mt(8))
    misc_box = UI.div().cls("space-y-6 max_w-md p-6 border rounded-xl mb-8")
    
    # Select
    sel_wrap = UI.div()
    sel_wrap.add(UI.label("Role").cls("block text-sm font-medium text-gray-700 mb-1"))
    sel = PyxElement("select").cls("w-full border p-2 rounded bg-white text-gray-700")
    sel.add(PyxElement("option").add("Admin"))
    sel.add(PyxElement("option").add("User"))
    sel.add(PyxElement("option").add("Guest"))
    sel_wrap.add(sel)
    misc_box.add(sel_wrap)
    
    # Checkbox
    chk_wrap = UI.div().flex().items("center").gap(2)
    chk_wrap.add(PyxElement("input").attr("type", "checkbox").cls("w-4 h-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500"))
    chk_wrap.add(UI.label("I agree to terms").cls("text-sm text-gray-900"))
    misc_box.add(chk_wrap)
    
    content.add(misc_box)
    
    # Updated Code Block for Select/Checkbox
    content.add(make_code_block('''# Select
ui.element("select").add(ui.element("option").add("Admin"))

# Checkbox
ui.input(type="checkbox")'''))

    # Button Variants
    content.add(UI.h2("Buttons").text("2xl").font("bold").mb(4).mt(8))
    btn_grid = UI.div().flex().flex_wrap().gap(4).mb(6)
    
    btn_grid.add(UI.button("Primary").bg("blue-600").text("white").px(4).py(2).rounded("md"))
    btn_grid.add(UI.button("Secondary").bg("gray-200").text("gray-800").px(4).py(2).rounded("md").hover("bg-gray-300"))
    btn_grid.add(UI.button("Destructive").bg("red-600").text("white").px(4).py(2).rounded("md").hover("bg-red-700"))
    btn_grid.add(UI.button("Outline").cls("border border-gray-300 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-50"))
    btn_grid.add(UI.button("Ghost").cls("text-blue-600 hover:bg-blue-50 px-4 py-2 rounded-md"))
    
    content.add(btn_grid)
    content.add(make_code_block('ui.button("Primary").bg("blue-600").text("white")'))

    return docs_layout(content, active_nav_item="Forms")
