from pyx.ui import UI
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def email_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Features", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Email").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("Email Sending").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Send transactional emails easily directly from your PyX application.").text("lg").text("gray-600").mb(8))

    content.add(UI.div().cls("bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-6").add(
        UI.p("This module requires an SMTP server configuration.").text("yellow-700")
    ))

    return docs_layout(content, active_nav_item="Email")
