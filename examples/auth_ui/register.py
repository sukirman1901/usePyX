from framework.ui import ui
import pyx

def RegisterPage():
    with ui.div().cls("min-h-screen flex items-center justify-center bg-gray-100") as page:
        with ui.card().w("96"):
            ui.h1("Create Account").text("2xl").font("bold").text("center").mb(6)
            
            with ui.form().cls("space-y-4"):
                with ui.div():
                    ui.label("Name").block().font("medium").mb(1)
                    ui.input(name="name", placeholder="John Doe").w_full().border().p(2).rounded()
                    
                with ui.div():
                    ui.label("Email").block().font("medium").mb(1)
                    ui.input(name="email", placeholder="you@example.com").w_full().border().p(2).rounded()
                
                with ui.div():
                    ui.label("Password").block().font("medium").mb(1)
                    ui.input(name="password", type="password").w_full().border().p(2).rounded()

                with ui.div():
                    ui.label("Confirm Password").block().font("medium").mb(1)
                    ui.input(name="password_confirmation", type="password").w_full().border().p(2).rounded()
                
                with ui.div().pt(2):
                    ui.button("Register").bg("black").text("white").w_full().p(2).rounded().font("bold")
            
            with ui.div().pt(4).text("center").text("sm"):
                ui.span("Already have an account? ").text("gray-600")
                ui.a("Sign In", href="/login").text("blue-600 hover:underline").font("medium")
                
    return page
