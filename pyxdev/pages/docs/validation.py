from pyx.ui import UI
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def validation_page():
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Features", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Validation").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Header
    content.add(UI.h1("Data Validation").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Ensure data integrity with PyX's built-in validation helpers.").text("lg").text("gray-600").mb(8))

    content.add(UI.p("PyX integrates closely with Pydantic for robust data validation.").text("gray-600").mb(4))

    code_example = '''
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

# Usage in handlers
def create_user(data: User):
    ...
'''
    content.add(make_code_block(code_example))

    return docs_layout(content, active_nav_item="Validation")
