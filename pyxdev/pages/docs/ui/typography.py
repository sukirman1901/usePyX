from pyx.ui import UI
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def typography_page():
    content = UI.div()
    
    # Breadcrumb
    content.add(UI.div().flex().gap(2).mb(4).add(UI.a("UI", "/docs/ui/overview").text("sm").text("gray-400")).add(UI.span("›").text("gray-400")).add(UI.span("Typography").text("sm").font("medium").text("gray-900")))
    
    content.add(UI.h1("Typography").text("3xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Headings and text utilities.").text("lg").text("gray-600").mb(8))

    # Examples
    content.add(UI.h2("Headings").text("2xl").font("bold").mb(4).mt(2))
    content.add(UI.h1("Heading 1 (4xl)").text("4xl").font("extrabold").mb(2))
    content.add(UI.h2("Heading 2 (3xl)").text("3xl").font("bold").mb(2))
    content.add(UI.h3("Heading 3 (2xl)").text("2xl").font("semibold").mb(2))
    content.add(UI.h4("Heading 4 (xl)").text("xl").font("medium").mb(6))
    
    content.add(make_code_block('ui.h1("Title").text("4xl").font("extrabold")'))

    # Text Sizes
    content.add(UI.h2("Text Customization").text("2xl").font("bold").mb(4).mt(8))
    
    sizes = UI.div().cls("space-y-4 mb-6 p-6 border rounded-xl")
    sizes.add(UI.p("This is text-xs").text("xs").text("gray-500"))
    sizes.add(UI.p("This is text-sm").text("sm").text("gray-600"))
    sizes.add(UI.p("This is text-base (default)").text("base").text("gray-700"))
    sizes.add(UI.p("This is text-lg").text("lg").text("gray-800"))
    sizes.add(UI.p("This is text-xl").text("xl").text("gray-900"))
    content.add(sizes)
    
    content.add(make_code_block('ui.text("Small text").text("sm").text("gray-600")'))
    
    # Weights & Colors
    content.add(UI.h2("Weights & Colors").text("2xl").font("bold").mb(4).mt(8))
    
    styles = UI.div().cls("space-y-2 mb-6")
    styles.add(UI.p("Thin Text (100)").font("thin"))
    styles.add(UI.p("Regular Text (400)").font("normal"))
    styles.add(UI.p("Medium Text (500)").font("medium"))
    styles.add(UI.p("Bold Text (700)").font("bold"))
    styles.add(UI.p("Extra Bold (800)").font("extrabold"))
    styles.add(UI.p("Blue Text").text("blue-600").font("medium"))
    styles.add(UI.p("Pink Text").text("pink-600").font("medium"))
    content.add(styles)
    content.add(make_code_block('ui.p("Bold Blue").font("bold").text("blue-600")'))


    return docs_layout(content, active_nav_item="Typography")
