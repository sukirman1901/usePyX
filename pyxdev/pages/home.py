from pyx.ui import UI, ui, PyxElement

def homepage():
    """Detailed Modern Landing Page for PyX"""
    root = ui.page()
    root.bg("slate-950").min_h("screen").text("white").cls("selection:bg-blue-500/30 selection:text-blue-200 font-sans antialiased overflow-x-hidden")
    root.add(PyxElement("script").add('document.title = "PyX - Build Modern Web Apps in Pure Python";'))
    
    # Global Resources
    root.add(PyxElement("link").attr("rel", "stylesheet").attr("href", "https://unpkg.com/lucide@latest"))
    # Custom CSS for specific glows and animations
    style = """
    .glow-text { text-shadow: 0 0 20px rgba(59, 130, 246, 0.5); }
    .hero-glow {
        background: radial-gradient(circle at 50% 50%, rgba(37, 99, 235, 0.15) 0%, transparent 50%);
        pointer-events: none;
    }
    .grid-bg {
        background-image: linear-gradient(to right, rgba(255,255,255,0.05) 1px, transparent 1px),
                          linear-gradient(to bottom, rgba(255,255,255,0.05) 1px, transparent 1px);
        background-size: 40px 40px;
        mask-image: radial-gradient(ellipse at center, black 40%, transparent 80%);
    }
    """
    root.add(PyxElement("style").add(style))
    
    # -------------------------------------------------------------------------
    # NAVBAR
    # -------------------------------------------------------------------------
    nav = PyxElement("nav").fixed().top(0).w("full").z(50).cls("backdrop-blur-md bg-slate-950/70 border-b border-white/5")

    nav_inner = UI.div().max_w("7xl").mx("auto").px(6).h(16).flex().items("center").justify("between")
    
    # Logo
    logo = PyxElement("a").attr("href", "/").flex().items("center").gap(2).cls("group")
    logo.add(UI.div().w(8).h(8).bg("blue-600").rounded("lg").shadow("lg shadow-blue-500/20").flex().items("center").justify("center")
             .add(UI.span("P").font("bold").text("white").text("lg")))
    logo.add(UI.span("PyX").font("bold").text("xl").text("slate-100").cls("tracking-tight group-hover:text-blue-400 transition-colors"))
    nav_inner.add(logo)
    
    # Links
    links = UI.div().cls("hidden md:flex items-center gap-8")
    for label, href in [("Documentation", "/docs/introduction"), ("Components", "/docs/ui/overview"), ("Blog", "#"), ("GitHub", "https://github.com/sukirman1901/usePyX/")]:
        links.add(UI.a(label, href).text("sm").font("medium").text("slate-300").hover("text-white").hover("text-shadow-sm transition-colors"))
    
    # CTA Small
    links.add(UI.a("Get Started", "/docs/quickstart").cls("px-4 py-2 bg-white/10 hover:bg-white/20 border border-white/10 rounded-full text-sm font-medium transition-all"))
    nav_inner.add(links)
    
    # Mobile Menu Icon (Placeholder)
    nav_inner.add(PyxElement("button").cls("md:hidden text-slate-300").add(PyxElement("i").attr("data-lucide", "menu")))
    
    nav.add(nav_inner)
    root.add(nav)
    
    # -------------------------------------------------------------------------
    # HERO SECTION
    # -------------------------------------------------------------------------
    hero = PyxElement("section").cls("relative pt-32 pb-20 lg:pt-48 lg:pb-32 px-6 overflow-hidden")
    
    # Background Effects
    hero.add(UI.div().absolute().inset(0).cls("grid-bg z-0"))
    hero.add(UI.div().absolute().inset(0).cls("hero-glow z-0"))
    
    container = UI.div().relative().z(10).max_w("7xl").mx("auto").grid().cols(1).lg("grid-cols-2").gap(12).items("center")
    
    # Left Content
    content_col = UI.div().cls("text-center lg:text-left")
    
    # Badge
    badge = UI.div().inline_flex().items("center").gap(2).px(3).py(1).rounded("full").bg("blue-500/10").border("blue-500/20").mb(8).cls("animate-fade-in")
    badge.add(PyxElement("span").cls("relative flex h-2 w-2").add(PyxElement("span").cls("animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75")).add(PyxElement("span").cls("relative inline-flex rounded-full h-2 w-2 bg-blue-500")))
    badge.add(UI.span("v1.0 Now Stable").text("xs").font("semibold").text("blue-300").tracking("wide").uppercase())
    content_col.add(badge)
    
    # Headlines
    h1 = PyxElement("h1").cls("text-5xl lg:text-7xl font-bold tracking-tight text-white mb-6 leading-tight")
    h1.add("The Frontend for")
    h1.add(UI.br())
    h1.add(UI.span("Backend Developers").cls("text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-cyan-400 to-emerald-400 glow-text"))
    content_col.add(h1)
    
    content_col.add(UI.p("Build beautiful, reactive web applications in pure Python. No JavaScript, no HTML mess, just Zen Mode.").cls("text-lg lg:text-xl text-slate-400 mb-8 max-w-2xl mx-auto lg:mx-0 leading-relaxed"))
    
    # CTA Group
    btns = UI.div().flex().flex_col().sm("flex-row").gap(4).justify("center").lg("justify-start")
    btns.add(UI.a("Start Building", "/docs/quickstart").cls("px-8 py-4 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-semibold shadow-lg shadow-blue-500/25 transition-all transform hover:-translate-y-1"))
    btns.add(UI.a("Read the Zen", "/docs/zen-mode").cls("px-8 py-4 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl font-semibold transition-all"))
    content_col.add(btns)
    
    # Tech Stack / Trust
    stack = UI.div().mt(12).flex().items("center").justify("center").lg("justify-start").gap(6).cls("opacity-60 grayscale hover:grayscale-0 transition-all duration-500")
    stack.add(UI.span("Powered by").text("xs").text("slate-500").uppercase().tracking("widest").mr(2))
    # Simple Text Logos for illustration
    stack.add(UI.div("Python").font("bold").text("slate-400"))
    stack.add(UI.div("Rust").font("bold").text("slate-400"))
    stack.add(UI.div("Tailwind").font("bold").text("slate-400"))
    content_col.add(stack)
    
    container.add(content_col)
    
    # Right Content (Code Visual)
    visual_col = UI.div().cls("relative hidden lg:block perspective-1000")
    
    # Code Window
    window = UI.div().cls("relative bg-slate-900 border border-slate-800 rounded-xl shadow-2xl shadow-blue-900/20 overflow-hidden transform rotate-y-6 rotate-x-6 hover:rotate-0 transition-transform duration-700 ease-out")
    
    # Window Header
    hdr = UI.div().flex().items("center").gap(2).px(4).py(3).bg("slate-950/50").border_b("slate-800")
    hdr.add(UI.div().w(3).h(3).rounded("full").bg("red-500/80"))
    hdr.add(UI.div().w(3).h(3).rounded("full").bg("yellow-500/80"))
    hdr.add(UI.div().w(3).h(3).rounded("full").bg("green-500/80"))
    hdr.add(UI.div("app.py").ml(4).text("xs").font("mono").text("slate-500"))
    window.add(hdr)
    
    # Code Body (Mock Syntax Highlight)
    code_body = UI.div().p(6).font("mono").text("sm").cls("leading-relaxed")
    
    def line(num, html_content):
        row = UI.div().flex().gap(4)
        row.add(UI.span(str(num)).text("slate-700").w(6).text("right").cls("select-none"))
        row.add(UI.div().add(html_content))
        return row
        
    code_body.add(line(1, PyxElement("span").add("from pyx.ui import ui").cls("text-purple-400")))
    code_body.add(line(2, PyxElement("span").add("")))
    code_body.add(line(3, PyxElement("span").add("def app():").cls("text-blue-400")))
    code_body.add(line(4, PyxElement("span").add("&nbsp;&nbsp;with ui.card().p(8):").cls("text-yellow-300")))
    code_body.add(line(5, PyxElement("span").add('&nbsp;&nbsp;&nbsp;&nbsp;ui.title("Hello World")').cls("text-green-400")))
    code_body.add(line(6, PyxElement("span").add('&nbsp;&nbsp;&nbsp;&nbsp;ui.button("Click Me").bg("blue-600")').cls("text-green-400")))
    
    window.add(code_body)
    visual_col.add(window)
    
    # Floating Element (Decor)
    float_card = UI.div().absolute().bottom(-20).left(-20).bg("slate-800/90").backdrop_blur().p(4).rounded("lg").shadow("xl").border("slate-700").cls("animate-bounce-slow")
    float_card.add(UI.div().flex().items("center").gap(3).add(UI.div().w(2).h(2).bg("green-400").rounded("full")).add(UI.span("Server Running").text("xs text-green-400 font-mono")))
    visual_col.add(float_card)
    
    container.add(visual_col)
    
    hero.add(container)
    root.add(hero)
    
    # -------------------------------------------------------------------------
    # FEATURES (Bento Grid)
    # -------------------------------------------------------------------------
    features = PyxElement("section").py(24).bg("slate-950").relative()
    feat_container = UI.div().max_w("7xl").mx("auto").px(6)
    
    features.add(UI.div().text("center").mb(16)
                 .add(UI.h2("Why Developers Choose PyX").text("3xl lg:text-5xl").font("bold").text("white").mb(4))
                 .add(UI.p("Everything you need to ship faster, without leaving Python.").text("lg").text("slate-400")))
                 
    grid = UI.div().grid().cols(1).md("grid-cols-3").gap(8)
    
    def feature_card(title, desc, icon, col_span=1):
        card = UI.div().cls(f"col-span-1 md:col-span-{col_span} group relative bg-slate-900 border border-slate-800 p-8 rounded-3xl hover:border-blue-500/30 transition-all duration-300 hover:shadow-2xl hover:shadow-blue-900/10 overflow-hidden")
        
        # Icon
        card.add(UI.div().w(12).h(12).bg("slate-800").rounded("2xl").flex().items("center").justify("center").mb(6).cls("group-hover:bg-blue-600 group-hover:scale-110 transition-all duration-300")
                 .add(PyxElement("i").attr("data-lucide", icon).cls("text-slate-300 group-hover:text-white")))
        
        card.add(UI.h3(title).text("xl").font("bold").text("white").mb(3))
        card.add(UI.p(desc).text("slate-400").cls("leading-relaxed"))
        
        # Decor
        card.add(UI.div().absolute().top(0).right(0).w(32).h(32).bg("blue-500").cls("blur-[100px] opacity-10 group-hover:opacity-20 transition-opacity"))
        
        return card

    grid.add(feature_card("Zero JavaScript", "Write your entire frontend and backend logic in pure Python. No context switching.", "code-2", 2))
    grid.add(feature_card("Type Safe", "Leverage Python type hints for rock-solid code reliability and editor support.", "shield-check"))
    grid.add(feature_card("Real-time State", "Built-in reactive state management that syncs automatically via WebSockets.", "zap"))
    grid.add(feature_card("Modular Design", "Component-based architecture that scales with your application needs.", "layers", 2))
    
    feat_container.add(grid)
    features.add(feat_container)
    root.add(features)

    # Simple Footer
    footer = PyxElement("footer").py(12).border_t("slate-900").bg("slate-950").text("center")
    footer.add(UI.p("© 2024 PyX Framework. Open Source MIT.").text("slate-600 text-sm"))
    root.add(footer)

    # Init Icons
    lucide_init = '''document.addEventListener("DOMContentLoaded", () => lucide.createIcons());'''
    root.add(PyxElement("script").add(lucide_init))
    
    return root
