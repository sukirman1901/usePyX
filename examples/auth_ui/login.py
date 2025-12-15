from framework.ui import ui
import pyx

def LoginPage():
    with ui.div().cls("min-h-screen flex items-center justify-center bg-gray-100") as page:
        with ui.card().w("96"):
            ui.h1("Login").text("2xl").font("bold").text("center").mb(6)
            
            with ui.form().cls("space-y-4"):
                with ui.div():
                    ui.label("Email").block().font("medium").mb(1)
                    ui.input(name="email", placeholder="admin@pyx.com", value="admin@pyx.com").w_full().border().p(2).rounded()
                
                with ui.div():
                    ui.label("Password").block().font("medium").mb(1)
                    ui.input(name="password", type="password", placeholder="••••••", value="password").w_full().border().p(2).rounded()
                
                with ui.div().pt(2):
                    ui.button("Sign In").bg("black").text("white").w_full().p(2).rounded().font("bold")
            
            with ui.div().pt(4).text("center").text("sm"):
                ui.span("Don't have an account? ").text("gray-600")
                ui.a("Sign Up", href="/register").text("blue-600 hover:underline").font("medium")
                
    return page
