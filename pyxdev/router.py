# router.py
from pages.home import homepage
from pages.docs.introduction import introduction_page
from pages.docs.installation import installation_page
from pages.docs.quickstart import quickstart_page
from pages.docs.structure import structure_page
from pages.docs.state import state_page
from pages.docs.zen_mode import zen_mode_page
from pages.docs.routing import routing_page
from pages.docs.auth import auth_page
from pages.docs.ui.overview import ui_overview_page
from pages.docs.ui.typography import typography_page
from pages.docs.ui.forms import forms_page
from pages.docs.ui.layout_page import layout_page
from pages.docs.ui.feedback import feedback_page
from pages.docs.ui.overlay import overlay_page
from pages.docs.ui.data_display import data_display_page

# Mock pages for placeholders
def not_found_page():
    from pyx.ui import UI
    return UI.div("404 Not Found").cls("flex items-center justify-center h-screen text-2xl font-bold")

def placeholder_page(title):
    from components.layout import docs_layout
    from pyx.ui import UI
    return lambda: docs_layout(UI.div(f"Content for {title} coming soon."), title=title)

# Route Registry
ROUTES = {
    "/": homepage,
    "/docs/introduction": introduction_page,
    "/docs/installation": installation_page,
    "/docs/quickstart": quickstart_page,
    "/docs/structure": structure_page,
    "/docs/state": state_page,
    
    # Core Concepts
    "/docs/zen-mode": zen_mode_page,
    "/docs/routing": routing_page,
    
    # UI Components
    "/docs/ui/overview": ui_overview_page,
    "/docs/ui/typography": typography_page,
    "/docs/ui/forms": forms_page,
    "/docs/ui/layout": layout_page,
    "/docs/ui/feedback": feedback_page,
    "/docs/ui/overlay": overlay_page,
    "/docs/ui/data-display": data_display_page,
    
    # Features (Some might be missing, adding placeholders)
    "/docs/auth": auth_page,
    "/docs/middleware": placeholder_page("Middleware"),
    "/docs/validation": placeholder_page("Validation"),
    "/docs/email": placeholder_page("Email"),
    
    # Deployment
    "/docs/docker": placeholder_page("Docker"),
    "/docs/vercel": placeholder_page("Vercel"),
}

def get_page(path):
    # exact match
    if path in ROUTES:
        return ROUTES[path]
    
    # simple 404
    return not_found_page
