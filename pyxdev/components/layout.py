from pyx.ui import UI, ui, PyxElement
from .ui_helpers import md_bold, Lucide
from .theme import Theme

# -------------------------------------------------------------------------
# GLOBAL SCRIPTS
# -------------------------------------------------------------------------
def inject_scripts(root):
    # Syntax Highlighting
    root.add(PyxElement("link").attr("rel", "stylesheet").attr("href", "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-light.min.css"))
    root.add(PyxElement("script").attr("src", "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"))
    root.add(PyxElement("script").attr("src", "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"))
    root.add(PyxElement("script").add("document.addEventListener('DOMContentLoaded', () => { hljs.highlightAll(); });"))
    
    # Lucide Icons
    root.add(PyxElement("script").attr("src", "https://unpkg.com/lucide@latest"))
    init_lucide = '''document.addEventListener("DOMContentLoaded", () => lucide.createIcons());'''
    root.add(PyxElement("script").add(init_lucide))

    # Smooth Scroll & Animations
    style = """
    html { scroll-behavior: smooth; }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .animate-fade-in {
        animation: fadeIn 0.4s ease-out forwards;
        will-change: opacity, transform;
    }
    """
    root.add(PyxElement("style").add(style))

    # Mobile Menu
    script_content = """
        function toggleMobileMenu() {
            const sidebar = document.getElementById('mobile-sidebar');
            const overlay = document.getElementById('mobile-overlay');
            sidebar.classList.toggle('translate-x-0');
            sidebar.classList.toggle('-translate-x-full');
            overlay.classList.toggle('hidden');
        }
    """
    root.add(PyxElement("script").add(script_content))

# -------------------------------------------------------------------------
# COMPONENT HELPERS
# -------------------------------------------------------------------------



def sidebar_link(text, href, icon=None, active=False):
    link = PyxElement("a").add("").attr("href", href).flex().items("center").gap(3).px(3).py(2).rounded("md").cls(Theme.transition_base)
    if active:
        link.cls(Theme.link_sidebar_active())
        if icon: link.add(Lucide(icon, size=18, color=Theme.primary))
        link.add(PyxElement("span").add(text).font("medium"))
    else:
        link.cls(Theme.link_sidebar_inactive())
        if icon: link.add(Lucide(icon, size=18, color=Theme.text_light))
        link.add(UI.span(text).font("medium"))
    return link

def sidebar_section(title):
    return UI.div(title).text("sm").font("bold").text("gray-900").mt(6).mb(3).px(3)

# -------------------------------------------------------------------------
# LAYOUT PARTS
# -------------------------------------------------------------------------

def create_navbar():
    nav = UI.div().fixed().top(0).left(0).right(0).z(40) \
        .bg("white/80").backdrop_blur("md").border_b().border_color("gray-200")
    
    nav_inner = UI.div().max_w("7xl").mx("auto").px(4).md("px-6").py(3).flex().justify("between").items("center")
    
    # Mobile Menu Button
    btn = PyxElement("button").add("").cls("lg:hidden p-2 rounded-lg border border-gray-200 bg-white hover:bg-gray-50") \
        .attr("onclick", "toggleMobileMenu()")
    btn.add(Lucide("menu", size=20, color="gray-500"))
    nav_inner.add(btn)
    
    # Logo
    logo = PyxElement("div").flex().items("center").gap(2)
    logo.add(PyxElement("span").add("PyX").text("xl").font("bold").text("gray-900"))
    logo.add(PyxElement("span").add("docs").text("xl").font("light").text("blue-600"))
    nav_inner.add(logo)
    
    # Desktop Links
    nav_links = PyxElement("div").cls("hidden lg:flex gap-8")
    nav_links.add(PyxElement("a").add("Docs").attr("href", "/docs/introduction").text("sm").text("blue-600").font("medium"))
    nav_links.add(PyxElement("a").add("Components").attr("href", "/docs/ui/overview").text("sm").text("gray-600").hover("text-gray-900"))
    nav_links.add(PyxElement("a").add("Examples").attr("href", "/examples").text("sm").text("gray-600").hover("text-gray-900"))
    nav_links.add(PyxElement("a").add("GitHub").attr("href", "https://github.com/sukirman1901/usePyX/").text("sm").text("gray-600").hover("text-gray-900"))
    nav_inner.add(nav_links)
    
    # CTA
    nav_inner.add(
        UI.a("Get Started", "/docs/installation").cls(f"hidden lg:block {Theme.button_primary()}")
    )
    nav.add(nav_inner)
    return nav

def create_sidebar(active_item="Introduction"):
    sidebar = PyxElement("aside").id("mobile-sidebar") \
        .fixed().left(0).top(0).h("screen").w(72).lg("w-64").bg("white") \
        .border_r().border_color("gray-200") \
        .pt(16).lg("pt-6").pb(20).px(6).z(50) \
        .cls("transform -translate-x-full lg:translate-x-0 transition-transform lg:top-14 overflow-y-auto")
        
    # Close Button
    btn = PyxElement("button").add("").cls("lg:hidden absolute top-4 right-4 p-2 rounded-md hover:bg-gray-100") \
        .attr("onclick", "toggleMobileMenu()")
    btn.add(Lucide("x", size=24, color="gray-600"))
    sidebar.add(btn)
    
    # Getting Started
    sidebar.add(sidebar_section("Getting Started"))
    sidebar.add(sidebar_link("Introduction", "/docs/introduction", "home", active=(active_item == "Introduction")))
    sidebar.add(sidebar_link("Installation", "/docs/installation", "download", active=(active_item == "Installation")))
    sidebar.add(sidebar_link("Quick Start", "/docs/quickstart", "zap", active=(active_item == "Quick Start")))
    sidebar.add(sidebar_link("State Management", "/docs/state", "database", active=(active_item == "State Management")))
    sidebar.add(sidebar_link("Project Structure", "/docs/structure", "folder-tree", active=(active_item == "Project Structure")))
    
    # User Interface
    sidebar.add(sidebar_section("User Interface"))
    sidebar.add(sidebar_link("Overview", "/docs/ui/overview", "layout-grid", active=(active_item == "UI Overview")))
    sidebar.add(sidebar_link("Typography", "/docs/ui/typography", "type", active=(active_item == "Typography")))
    sidebar.add(sidebar_link("Forms", "/docs/ui/forms", "edit-3", active=(active_item == "Forms")))
    sidebar.add(sidebar_link("Layout", "/docs/ui/layout", "columns", active=(active_item == "Layout")))
    sidebar.add(sidebar_link("Feedback", "/docs/ui/feedback", "bell", active=(active_item == "Feedback")))
    sidebar.add(sidebar_link("Overlay", "/docs/ui/overlay", "maximize", active=(active_item == "Overlay")))
    sidebar.add(sidebar_link("Data Display", "/docs/ui/data-display", "list", active=(active_item == "Data Display")))

    # Core Concepts
    sidebar.add(sidebar_section("Core Concepts"))
    sidebar.add(sidebar_link("Zen Mode UI", "/docs/zen-mode", "layout", active=(active_item == "Zen Mode")))
    sidebar.add(sidebar_link("Routing", "/docs/routing", "signpost", active=(active_item == "Routing")))
    
    # Features
    sidebar.add(sidebar_section("Features"))
    sidebar.add(sidebar_link("Authentication", "/docs/auth", "lock", active=(active_item == "Authentication")))
    sidebar.add(sidebar_link("Middleware", "/docs/middleware", "shield", active=(active_item == "Middleware")))
    sidebar.add(sidebar_link("Validation", "/docs/validation", "check-circle", active=(active_item == "Validation")))
    sidebar.add(sidebar_link("Email", "/docs/email", "mail", active=(active_item == "Email")))
    
    # Deployment
    sidebar.add(sidebar_section("Deployment"))
    sidebar.add(sidebar_link("Docker", "/docs/docker", "box", active=(active_item == "Docker")))
    sidebar.add(sidebar_link("Vercel", "/docs/vercel", "cloud", active=(active_item == "Vercel")))
    
    return sidebar

def create_toc(items):
    toc = PyxElement("div").cls("w-64 hidden xl:block flex-shrink-0 sticky top-24 h-[calc(100vh-6rem)] overflow-y-auto pl-8")
    toc.add(UI.p("On this page").text("xs").font("semibold").text("gray-900").mb(4).uppercase().tracking("wider"))
    toc_links = UI.div().cls("border-l border-gray-100 space-y-1")
    
    # Scroll Spy Script
    spy_script = """
    document.addEventListener('DOMContentLoaded', () => {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    document.querySelectorAll('.toc-link').forEach(link => {
                        link.classList.remove('text-blue-600', 'font-medium', 'border-blue-600');
                        link.classList.add('text-gray-500', 'border-transparent');
                        if (link.getAttribute('href') === '#' + id) {
                            link.classList.add('text-blue-600', 'font-medium', 'border-blue-600');
                            link.classList.remove('text-gray-500', 'border-transparent');
                        }
                    });
                }
            });
        }, { rootMargin: '-100px 0px -60% 0px' });

        document.querySelectorAll('h1[id], h2[id], h3[id]').forEach((section) => {
            observer.observe(section);
        });
    });
    """
    toc.add(PyxElement("script").add(spy_script))
    
    for item in items:
        label = item[0] if isinstance(item, tuple) else item
        href = item[1] if isinstance(item, tuple) else f"#{label.lower().replace(' ', '-')}"
        
        # Initial active state handled by JS mostly, but we set base classes
        toc_links.add(
            UI.a(label, href).block().text("sm")
            .cls("toc-link text-gray-500 hover:text-gray-900 border-l-2 border-transparent hover:border-gray-300 pl-4 py-1 transition-colors")
        )
        
    toc.add(toc_links)
    return toc


# -------------------------------------------------------------------------
# MAIN LAYOUT COMPOSER
# -------------------------------------------------------------------------

def docs_layout(content_element, active_nav_item="Introduction", toc_items=None, title=None):
    """
    Wraps content in standard Docs Dashboard Layout.
    """
    root = ui.page()
    
    # Set Page Title via JS (safest fallback)
    page_title = f"{title} - PyX Docs" if title else "PyX Documentation"
    root.add(PyxElement("script").add(f'document.title = "{page_title}";'))
    
    root.bg("white").min_h("screen")
    
    inject_scripts(root)
    
    # Overlay for mobile sidebar
    overlay = UI.div().id("mobile-overlay").cls("hidden").fixed().inset(0).bg("black/50").z(40) \
        .attr("onclick", "toggleMobileMenu()").lg("hidden")
    root.add(overlay)
    
    # Navbar
    root.add(create_navbar())
    
    # Sidebar
    root.add(create_sidebar(active_nav_item))
    
    # Dashboard Wrapper
    dashboard_layout = UI.div().w_full().min_h("screen").lg("pl-72").bg("white")
    main_wrapper = UI.div().max_w("7xl").mx("auto").px(6).md("px-8").pt(20).pb(20) \
        .flex().justify("center").gap(12)
        
    # Content Area
    # If content_element is a PyxElement, add it.
    wrapper_content = UI.div().cls("flex-1 animate-fade-in").min_w("0").max_w("4xl")
    wrapper_content.add(content_element)
    
    main_wrapper.add(wrapper_content)
    
    # TOC
    if toc_items:
        main_wrapper.add(create_toc(toc_items))
        
    dashboard_layout.add(main_wrapper)
    root.add(dashboard_layout)
    
    return root
