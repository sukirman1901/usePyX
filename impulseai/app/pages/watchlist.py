"""
ImpulseAI - Watchlist Page
"""
import sys
sys.path.insert(0, '/Users/aaa/Documents/Developer/Framework/PyX')

from pyx import UI
from app.state import WatchlistState


def watchlist_page():
    return UI.div(
        # Navbar
        UI.div(
            UI.div(
                UI.a([
                    UI.raw('<i data-lucide="line-chart" class="w-6 h-6 text-primary"></i>'),
                    UI.span("ImpulseAI").cls("font-bold text-xl ml-2"),
                ]).attr("href", "/").cls("flex items-center"),
                UI.nav(
                    UI.a("Home").attr("href", "/").cls("text-sm font-medium text-muted-foreground hover:text-foreground"),
                    UI.a("Screener").attr("href", "/screener").cls("text-sm font-medium text-muted-foreground hover:text-foreground ml-6"),
                    UI.a("Analisis").attr("href", "/analysis").cls("text-sm font-medium text-muted-foreground hover:text-foreground ml-6"),
                    UI.a("Watchlist").attr("href", "/watchlist").cls("text-sm font-medium text-foreground ml-6"),
                ).cls("flex items-center ml-10"),
            ).cls("flex items-center max-w-4xl mx-auto px-8"),
        ).cls("border-b border-border py-4"),
        
        # Content
        UI.div(
            UI.h1("Watchlist Saya").cls("text-3xl font-bold mb-2"),
            UI.p("Pantau saham favorit Anda").cls("text-muted-foreground mb-8"),
            
            # Add form
            UI.div(
                UI.input().attr("placeholder", "Tambah saham (BBCA)").cls("h-9 w-64 px-3 rounded-md border border-input bg-transparent text-sm"),
                UI.button("Tambah").cls("bg-primary text-primary-foreground px-4 py-2 rounded-md text-sm font-medium ml-3"),
            ).cls("flex items-center mb-8"),
            
            # Cards
            UI.div(
                watchlist_card("BBCA", "Bank Central Asia", 9875, 2.45, "BUY"),
                watchlist_card("BMRI", "Bank Mandiri", 6350, 1.85, "BUY"),
                watchlist_card("TLKM", "Telkom Indonesia", 3850, 0.78, "HOLD"),
                watchlist_card("BBRI", "Bank Rakyat Indonesia", 5525, -0.45, "HOLD"),
            ).cls("grid grid-cols-2 gap-4"),
            
        ).cls("max-w-4xl mx-auto py-8 px-8"),
        
        UI.raw('<script>lucide.createIcons();</script>'),
    ).cls("min-h-screen bg-background text-foreground")


def watchlist_card(symbol, name, price, change, signal):
    is_positive = change >= 0
    change_class = "text-green-600" if is_positive else "text-red-600"
    signal_class = {"BUY": "bg-green-100 text-green-700", "SELL": "bg-red-100 text-red-700", "HOLD": "bg-yellow-100 text-yellow-700"}.get(signal, "bg-gray-100")
    
    return UI.div(
        UI.div(
            UI.span(symbol).cls("font-semibold text-lg"),
            UI.span(name).cls("text-sm text-muted-foreground ml-2"),
        ).cls("flex items-baseline"),
        UI.div(
            UI.span("Rp " + str(price)).cls("text-2xl font-bold"),
            UI.span(("+" if is_positive else "") + str(change) + "%").cls("text-sm font-medium ml-2 " + change_class),
        ).cls("flex items-baseline mt-3"),
        UI.div(
            UI.span("Signal:").cls("text-xs text-muted-foreground"),
            UI.span(signal).cls("text-xs font-medium ml-2 px-2 py-0.5 rounded-full " + signal_class),
        ).cls("flex items-center mt-4"),
        UI.a("View Chart").attr("href", "/analysis?symbol=" + symbol).cls("text-sm text-primary mt-4 block"),
    ).cls("rounded-lg border border-border bg-card p-4")
