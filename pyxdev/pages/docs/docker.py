from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import md_bold, make_code_block

def docker_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Deployment", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Docker").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("Docker Deployment").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Deploying PyX with Docker is the recommended way for production.").text("lg").text("gray-600").mb(8))

    # Dockerfile
    content.add(UI.h2("Dockerfile").text("2xl").font("bold").text("gray-900").mb(4))
    content.add(UI.p("Create a `Dockerfile` in your project root:").text("gray-600").mb(4))
    
    dockerfile = '''
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port (PyX default is 8020, change as needed)
EXPOSE 8020

# Run with Granian directly for production
CMD ["granian", "--interface", "asgi", "main:app_instance", "--host", "0.0.0.0", "--port", "8020"]
'''
    content.add(make_code_block(dockerfile, language="dockerfile"))

    # Layout
    return docs_layout(content, active_nav_item="Docker")
