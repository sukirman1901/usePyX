from pyx.ui import UI
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def middleware_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Features", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Middleware").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("Middleware").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Intercept and process requests before they reach your page handlers using Middleware.").text("lg").text("gray-600").mb(8))

    content.add(UI.p("Middleware is useful for logging, authentication checks, and modifying request/response objects.").text("gray-600").mb(4))

    code_example = '''
async def my_middleware(scope, receive, send):
    print("Request received!")
    await app(scope, receive, send)

# Registering (Coming Soon)
'''
    content.add(make_code_block(code_example))

    return docs_layout(content, active_nav_item="Middleware")
