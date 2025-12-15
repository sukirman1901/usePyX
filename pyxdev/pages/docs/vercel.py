from pyx.ui import UI
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def vercel_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Deployment", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Vercel").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("Deploy directly to Vercel").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    
    content.add(UI.p("Deploying PyX to Vercel is simple using the standard Python runtime.").text("lg").text("gray-600").mb(8))

    content.add(UI.h2("vercel.json").text("2xl").font("bold").text("gray-900").mb(4))
    
    json_config = '''
{
    "builds": [
        {"src": "main.py", "use": "@vercel/python"}
    ],
    "routes": [
        {"src": "/(.*)", "dest": "main.py"}
    ]
}
'''
    content.add(make_code_block(json_config, language="json"))

    return docs_layout(content, active_nav_item="Vercel")
