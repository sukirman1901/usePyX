from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def data_display_page():
    content = UI.div()
    
    # Breadcrumb
    content.add(UI.div().flex().gap(2).mb(4).add(UI.a("UI", "/docs/ui/overview").text("sm").text("gray-400")).add(UI.span("›").text("gray-400")).add(UI.span("Data Display").text("sm").font("medium").text("gray-900")))
    
    content.add(UI.h1("Data Display").text("3xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Structures for presenting data collections.").text("lg").text("gray-600").mb(8))

    # Table Example
    content.add(UI.h3("Tables").text("xl").font("bold").mb(2))
    
    table = PyxElement("table").cls("min-w-full divide-y divide-gray-200 border rounded-lg overflow-hidden mb-8")
    thead = PyxElement("thead").cls("bg-gray-50")
    row_head = PyxElement("tr")
    row_head.add(PyxElement("th").add("Name").cls("px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"))
    row_head.add(PyxElement("th").add("Status").cls("px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"))
    thead.add(row_head)
    table.add(thead)
    
    tbody = PyxElement("tbody").cls("bg-white divide-y divide-gray-200")
    
    def add_row(name, status, status_cls):
        tr = PyxElement("tr")
        tr.add(PyxElement("td").add(name).cls("px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"))
        tr.add(PyxElement("td").add(PyxElement("span").add(status).cls(f"px-2 inline-flex text-xs leading-5 font-semibold rounded-full {status_cls}")))
        tbody.add(tr)
        
    add_row("Server A", "Active", "bg-green-100 text-green-800")
    add_row("Server B", "Down", "bg-red-100 text-red-800")
    table.add(tbody)
    
    content.add(table)
    
    content.add(make_code_block('ui.element("table").cls("divide-y divide-gray-200")'))
    
    # Lists
    content.add(UI.h3("Lists").text("xl").font("bold").mt(8).mb(2))
    ul = PyxElement("ul").cls("list-disc list-inside space-y-1 text-gray-600 bg-white p-6 border rounded-xl")
    ul.add(PyxElement("li").add("First item"))
    ul.add(PyxElement("li").add("Second item"))
    ul.add(PyxElement("li").add("Third item"))
    content.add(ul)
    content.add(make_code_block('ui.element("ul").cls("list-disc").add(ui.element("li").add("Item"))').mt(6))
    
    # Cards
    content.add(UI.h3("Cards").text("xl").font("bold").mt(8).mb(2))
    card_grid = UI.div().cls("grid grid-cols-1 md:grid-cols-2 gap-4")
    
    # Simple Card
    c1 = UI.div().p(6).shadow("sm").bg("white").border().rounded("xl")
    c1.add(UI.h4("Simple Card").font("bold").mb(2))
    c1.add(UI.p("This is a basic card component used for grouping content.").text("gray-500 text-sm"))
    card_grid.add(c1)
    
    # Image Card
    c2 = UI.div().cls("border rounded-xl overflow-hidden shadow-sm bg-white")
    c2.add(UI.div().cls("h-32 bg-gray-200")) # Placeholder image
    c2_body = UI.div().p(4)
    c2_body.add(UI.h4("Image Card").font("bold").mb(2))
    c2_body.add(UI.p("A card with a media area on top.").text("gray-500 text-sm"))
    c2.add(c2_body)
    card_grid.add(c2)
    
    content.add(card_grid)
    content.add(make_code_block('ui.card().p(6).shadow("sm")').mt(6))

    return docs_layout(content, active_nav_item="Data Display")
