from pyx.ui import UI, ui, PyxElement
from components.layout import docs_layout, Lucide
from components.ui_helpers import md_bold, make_code_block
import pyx

# -----------------------------------------------------------------------------
# LOCAL STATE
# -----------------------------------------------------------------------------
class InstallState(pyx.State):
    os_tab: str = "mac"  # Options: 'mac', 'win'

    def set_mac(self):
        self.os_tab = "mac"

    def set_win(self):
        self.os_tab = "win"

# -----------------------------------------------------------------------------
# PAGE COMPONENT
# -----------------------------------------------------------------------------
def installation_page():
    # Initialize Context (IMPORTANT for State binding)
    # Note: doc_layout calls ui.page(), but we need to ensure state is registered if we use it directly.
    # However, since we return layout content, the root creation happens inside layout.
    # State usage inside 'content' build is fine.
    
    content = UI.div()
    
    # Breadcrumb
    breadcrumb = UI.div().flex().gap(2).mb(4)
    breadcrumb.add(UI.a("Getting Started", "#").text("sm").text("gray-400"))
    breadcrumb.add(UI.span("›").text("gray-400"))
    breadcrumb.add(UI.span("Installation").text("sm").font("medium").text("gray-900"))
    content.add(breadcrumb)
    
    # Title
    content.add(UI.h1("Installation").text("3xl").md("text-4xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p().add(md_bold("PyX requires **Python 3.9+**.")).text("lg").text("gray-600").mb(6))

    # 1. Virtual Environment
    content.add(UI.h2("1. Virtual Environment").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("venv"))
    content.add(UI.p("We highly recommend creating a virtual environment for your project.").text("gray-600").mb(4))
    
    # OS Tabs (Visual Only for now as complex conditional rendering might need verifying)
    # Let's stick to a clean static display for stability, showing macOS first clearly.
    
    content.add(UI.div().cls("bg-blue-50 border-l-4 border-blue-500 p-4 mb-6").add(
        UI.p().add(md_bold("Note: **MacOS/Linux** commands are shown below. For Windows, use PowerShell.")).text("sm").text("blue-700")
    ))

    content.add(UI.p("Create the project directory and switch to it:").text("gray-600").mb(2))
    content.add(make_code_block("mkdir my_app_name\ncd my_app_name", language="bash"))
    
    content.add(UI.p("Create and activate virtual environment:").text("gray-600").mb(2))
    content.add(make_code_block("python3 -m venv .venv\nsource .venv/bin/activate", language="bash"))

    # 2. Install Package
    content.add(UI.h2("2. Install PyX Framework").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("install"))
    content.add(UI.p("PyX is available as a pip package.").text("gray-600").mb(2))
    content.add(make_code_block("pip install pyx-framework", language="bash"))
    
    # 3. Initialize
    content.add(UI.h2("3. Initialize the Project").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("init"))
    content.add(UI.p("Initialize the web directory with the basic template:").text("gray-600").mb(2))
    content.add(make_code_block("pyx init", language="bash"))
    
    content.add(UI.p("This command will create the necessary directory structure for your new PyX app.").text("gray-600").mb(4))
    
    # 4. Run App
    content.add(UI.h2("4. Run the App").text("2xl").font("bold").text("gray-900").mt(8).mb(4).id("run"))
    content.add(UI.p("Run your app in development mode:").text("gray-600").mb(2))
    content.add(make_code_block("pyx run", language="bash"))
    
    content.add(UI.p().add(md_bold("Your app will run at [http://localhost:8020](http://localhost:8020).")).text("gray-600").mb(4))
    
    # Debug Tip
    tip_box = UI.div().cls("bg-gray-50 border border-gray-200 rounded-lg p-4 mt-6")
    tip_box.add(UI.h4("Debugging Tip").font("bold").text("gray-900").mb(2))
    tip_box.add(UI.p("You can increase log verbosity to help with debugging using the --loglevel flag:").text("sm").text("gray-600").mb(2))
    tip_box.add(PyxElement("code").cls("bg-white text-pink-600 px-2 py-1 rounded border border-gray-200 text-xs font-mono").add("pyx run --loglevel debug"))
    content.add(tip_box)

    # Build Final Page using Layout
    toc_items = [
        "Installation", 
        ("Virtual Env", "#venv"),
        ("Install Package", "#install"),
        ("Initialize", "#init"),
        ("Run App", "#run")
    ]
    
    return docs_layout(content, active_nav_item="Installation", toc_items=toc_items)
