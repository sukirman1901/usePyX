from pyx.ui import UI
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def layout_ui_page():
    content = UI.div()
    
    # Breadcrumb
    content.add(UI.div().flex().gap(2).mb(4).add(UI.a("UI", "/docs/ui/overview").text("sm").text("gray-400")).add(UI.span("›").text("gray-400")).add(UI.span("Layout").text("sm").font("medium").text("gray-900")))
    
    content.add(UI.h1("Layout").text("3xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Primitives for positioning and structure.").text("lg").text("gray-600").mb(8))

    # Flexbox
    content.add(UI.h2("Flexbox").text("2xl").font("bold").mb(4))
    row = UI.div().flex().gap(4).mb(6)
    row.add(UI.div("01").bg("blue-100").text("blue-700").p(4).rounded().font("bold"))
    row.add(UI.div("02").bg("blue-200").text("blue-800").p(4).rounded().font("bold"))
    row.add(UI.div("03").bg("blue-300").text("blue-900").p(4).rounded().font("bold"))
    content.add(row)
    content.add(make_code_block('with ui.row().gap(4):\n    ui.div("01")\n    ui.div("02")'))

    # Grid System
    content.add(UI.h2("Grid System").text("2xl").font("bold").mb(4).mt(8))
    grid = UI.div().cls("grid grid-cols-3 gap-4 mb-6")
    for i in range(1, 7):
        grid.add(UI.div(f"Col {i}").bg("emerald-100").text("emerald-800").p(4).text("center").rounded().font("medium"))
    content.add(grid)
    content.add(make_code_block('with ui.grid(cols=3).gap(4):\n    ui.col("Col 1")'))

    # Stacks
    content.add(UI.h2("Stacks").text("2xl").font("bold").mb(4).mt(8))
    
    stack_area = UI.div().cls("flex gap-8 mb-6 p-6 border rounded-xl bg-gray-50")
    
    # VStack
    vs = UI.div().cls("flex flex-col gap-2 p-4 bg-white rounded shadow-sm w-32")
    vs.add(UI.div("VStack").text("xs text-gray-400 mb-1"))
    vs.add(UI.div("Item 1").bg("indigo-100").p(2).rounded().text("xs text-center"))
    vs.add(UI.div("Item 2").bg("indigo-100").p(2).rounded().text("xs text-center"))
    stack_area.add(vs)
    
    # HStack
    hs = UI.div().cls("flex flex-row items-center gap-2 p-4 bg-white rounded shadow-sm")
    hs.add(UI.div("HStack").text("xs text-gray-400 mr-2"))
    hs.add(UI.div("A").bg("purple-100").p(2).w(8).h(8).rounded().flex().items("center").justify("center").text("xs"))
    hs.add(UI.div("B").bg("purple-100").p(2).w(8).h(8).rounded().flex().items("center").justify("center").text("xs"))
    stack_area.add(hs)
    
    content.add(stack_area)
    content.add(make_code_block('ui.vstack().gap(2)\nui.hstack().gap(2)'))


    return docs_layout(content, active_nav_item="Layout")
