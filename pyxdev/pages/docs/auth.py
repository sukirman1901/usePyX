from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import md_bold, make_code_block

def auth_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Features", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Authentication").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("Authentication").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Secure your PyX application with built-in authentication support.").text("lg").text("gray-600").mb(8))

    # Content
    content.add(UI.div().cls("bg-blue-50 border-l-4 border-blue-500 p-4 mb-6").add(
        UI.p("This feature is currently in beta. APIs may change.").text("blue-700").font("medium")
    ))
    
    content.add(UI.p("PyX provides hooks to integrate with standard Auth providers or custom database authentication.").text("gray-600"))

    # Layout
    return docs_layout(content, active_nav_item="Authentication")
