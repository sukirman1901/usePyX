from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def overlay_page():
    content = UI.div()
    
    # Breadcrumb
    content.add(UI.div().flex().gap(2).mb(4).add(UI.a("UI", "/docs/ui/overview").text("sm").text("gray-400")).add(UI.span("›").text("gray-400")).add(UI.span("Overlay").text("sm").font("medium").text("gray-900")))
    
    content.add(UI.h1("Overlay").text("3xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Components that appear on top of other content.").text("lg").text("gray-600").mb(8))

    # Modal Example (Static)
    content.add(UI.h3("Modal").text("xl").font("bold").mb(2))
    content.add(UI.p("Modals typically use fixed positioning and a backdrop.").text("gray-600").mb(4))
    
    # Visual representation of a modal card
    modal_card = UI.div().cls("border border-gray-200 shadow-xl rounded-xl p-6 max-w-xl bg-white mx-auto md:mx-0 mb-8")
    modal_card.add(UI.h4("Confirm Action").text("lg").font("bold").mb(2))
    modal_card.add(UI.p("Are you sure you want to delete this item?").text("gray-600").mb(6))
    
    btns = UI.div().flex().justify("end").gap(3)
    btns.add(PyxElement("button").add("Cancel").cls("px-4 py-2 border border-gray-300 rounded text-gray-700 hover:bg-gray-50 hover:text-gray-900 text-sm font-medium transition-colors"))
    btns.add(UI.button("Delete").cls("px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 text-sm font-medium"))
    modal_card.add(btns)
    
    content.add(modal_card)
    
    content.add(make_code_block('ui.div().fixed().inset(0).bg("black/50") # Backdrop\nui.card().fixed().center() # Content'))
    
    # Popover
    content.add(UI.h3("Popover").text("xl").font("bold").mt(8).mb(2))
    
    # Add margin bottom to wrapper so absolute content doesn't overlap next element
    pop_wrap = UI.div().cls("relative inline-block mb-24")
    pop_wrap.add(UI.button("Click Me").bg("gray-200").px(4).py(2).rounded())
    
    # Fake popover content positioned absolute
    pop_content = UI.div().cls("absolute top-full left-0 mt-2 w-48 bg-white border rounded shadow-lg p-3 z-10")
    pop_content.add(UI.h4("Popover Title").font("bold").text("sm").mb(1))
    pop_content.add(UI.p("Here is some helpful content.").text("xs text-gray-500"))
    
    pop_wrap.add(pop_content)
    content.add(pop_wrap)
    content.add(make_code_block('ui.div().cls("absolute top-full") # Positioning logic required'))
    
    # Tooltip
    content.add(UI.h3("Tooltips").text("xl").font("bold").mt(12).mb(2))
    tool_wrap = UI.div().cls("relative inline-block group")
    tool_wrap.add(UI.button("Hover me").text("blue-600 underline"))
    
    # Tooltip (visible on hover via group-hover logic commonly used in Tailwind)
    tooltip = UI.div("This is a tooltip").cls("absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-2 py-1 bg-black text-white text-xs rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap")
    tool_wrap.add(tooltip)
    content.add(tool_wrap)
    content.add(make_code_block('ui.div("Tooltip").cls("opacity-0 group-hover:opacity-100 absolute")').mt(6))

    return docs_layout(content, active_nav_item="Overlay")
