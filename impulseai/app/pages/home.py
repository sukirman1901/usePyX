"""
ImpulseAI - Home Page
Clean minimalist design
"""
import sys
sys.path.insert(0, '/Users/aaa/Documents/Developer/Framework/PyX')

from pyx import UI


def home_page():
    """Main home page."""
    return UI.div(
        # Navbar
        UI.div(
            UI.div(
                # Logo
                UI.a([
                    UI.raw('<i data-lucide="line-chart" class="w-6 h-6 text-primary"></i>'),
                    UI.span("ImpulseAI").cls("font-bold text-xl ml-2"),
                ]).attr("href", "/").cls("flex items-center"),
                # Nav
                UI.nav(
                    UI.a("Home").attr("href", "/").cls("text-sm font-medium text-foreground"),
                    UI.a("Screener").attr("href", "/screener").cls("text-sm font-medium text-muted-foreground hover:text-foreground ml-6"),
                    UI.a("Analisis").attr("href", "/analysis").cls("text-sm font-medium text-muted-foreground hover:text-foreground ml-6"),
                    UI.a("Watchlist").attr("href", "/watchlist").cls("text-sm font-medium text-muted-foreground hover:text-foreground ml-6"),
                ).cls("flex items-center ml-10"),
            ).cls("flex items-center max-w-7xl mx-auto px-8"),
        ).cls("border-b border-border py-4"),
        
        # Hero Section
        UI.div(
            UI.h1([
                UI.span("Analisa Saham Indonesia "),
                UI.span("dengan AI").cls("text-primary"),
            ]).cls("text-5xl font-bold tracking-tight text-foreground"),
            UI.p("Dapatkan insight pasar, sinyal trading, dan analisa teknikal real-time untuk saham-saham BEI.").cls("text-lg text-muted-foreground mt-6 max-w-2xl"),
            UI.div(
                UI.a("Mulai Screener").attr("href", "/screener").cls("inline-flex items-center rounded-md bg-primary text-primary-foreground px-6 py-3 text-sm font-medium"),
                UI.a("Lihat Watchlist").attr("href", "/watchlist").cls("inline-flex items-center rounded-md border border-input px-6 py-3 text-sm font-medium ml-4"),
            ).cls("mt-10"),
        ).cls("py-24 px-8 border-b"),
        
        # Stats Section
        UI.div(
            UI.div(
                stat_card("900+", "Saham Terdaftar"),
                stat_card("50+", "Indikator Teknikal"),
                stat_card("24/7", "AI Analysis"),
                stat_card("Real-time", "Data Streaming"),
            ).cls("grid grid-cols-4 gap-8"),
        ).cls("max-w-5xl mx-auto py-16 px-8"),
        
        # Top Movers
        UI.div(
            UI.h2("Top Movers Hari Ini").cls("text-2xl font-semibold mb-6"),
            UI.div(
                stock_card("BBCA", "Bank Central Asia", 9875, 2.45, "BUY"),
                stock_card("BMRI", "Bank Mandiri", 6350, 1.85, "BUY"),
                stock_card("TLKM", "Telkom Indonesia", 3850, 0.78, "HOLD"),
                stock_card("UNVR", "Unilever Indonesia", 4250, -0.95, "SELL"),
            ).cls("grid grid-cols-4 gap-4"),
        ).cls("max-w-6xl mx-auto py-12 px-8"),
        
        # Footer
        UI.div(
            UI.p("© 2024 ImpulseAI. Built with PyX Framework.").cls("text-sm text-muted-foreground"),
        ).cls("border-t py-8 text-center"),
        
        # Lucide init
        UI.raw('<script>lucide.createIcons();</script>'),
    ).cls("min-h-screen bg-background text-foreground")


def stat_card(value, label):
    return UI.div(
        UI.span(value).cls("text-3xl font-bold text-primary"),
        UI.span(label).cls("text-sm text-muted-foreground mt-1 block"),
    ).cls("text-center")


def stock_card(symbol, name, price, change, signal):
    is_positive = change >= 0
    change_class = "text-green-600 bg-green-50" if is_positive else "text-red-600 bg-red-50"
    signal_class = {"BUY": "bg-green-100 text-green-700", "SELL": "bg-red-100 text-red-700", "HOLD": "bg-yellow-100 text-yellow-700"}.get(signal, "bg-gray-100")
    
    return UI.div(
        UI.div(
            UI.div(
                UI.span(symbol).cls("font-semibold text-base"),
                UI.span(name).cls("text-xs text-muted-foreground block"),
            ),
            UI.span(signal).cls("text-xs font-medium px-2 py-0.5 rounded-full " + signal_class),
        ).cls("flex items-start justify-between"),
        UI.div(
            UI.span("Rp " + str(price)).cls("text-xl font-bold"),
            UI.span(("+" if is_positive else "") + str(change) + "%").cls("text-xs font-medium ml-2 px-1.5 py-0.5 rounded " + change_class),
        ).cls("flex items-baseline mt-3"),
    ).cls("rounded-lg border border-border bg-card p-4")
