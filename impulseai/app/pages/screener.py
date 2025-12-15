"""
ImpulseAI - Screener Page
"""
import sys
sys.path.insert(0, '/Users/aaa/Documents/Developer/Framework/PyX')

from pyx import UI
from app.state import ScreenerState


def screener_page():
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
                    UI.a("Screener").attr("href", "/screener").cls("text-sm font-medium text-foreground ml-6"),
                    UI.a("Analisis").attr("href", "/analysis").cls("text-sm font-medium text-muted-foreground hover:text-foreground ml-6"),
                    UI.a("Watchlist").attr("href", "/watchlist").cls("text-sm font-medium text-muted-foreground hover:text-foreground ml-6"),
                ).cls("flex items-center ml-10"),
            ).cls("flex items-center max-w-6xl mx-auto px-8"),
        ).cls("border-b border-border py-4"),
        
        # Content
        UI.div(
            UI.h1("Stock Screener").cls("text-3xl font-bold mb-2"),
            UI.p("Filter dan temukan saham terbaik").cls("text-muted-foreground mb-8"),
            
            # Filter Card
            UI.div(
                UI.h3("Filter").cls("font-semibold mb-4"),
                UI.div(
                    UI.div(
                        UI.label("Harga Min").cls("text-sm text-muted-foreground block mb-1"),
                        UI.input().attr("placeholder", "0").cls("w-full h-9 px-3 rounded-md border border-input bg-transparent text-sm"),
                    ),
                    UI.div(
                        UI.label("Harga Max").cls("text-sm text-muted-foreground block mb-1"),
                        UI.input().attr("placeholder", "100,000").cls("w-full h-9 px-3 rounded-md border border-input bg-transparent text-sm"),
                    ),
                    UI.div(
                        UI.label("Sektor").cls("text-sm text-muted-foreground block mb-1"),
                        UI.select(
                            UI.option("Semua Sektor").attr("value", "all"),
                            UI.option("Banking").attr("value", "banking"),
                            UI.option("Mining").attr("value", "mining"),
                        ).cls("w-full h-9 px-3 rounded-md border border-input bg-transparent text-sm"),
                    ),
                    UI.div(
                        UI.label("Sinyal AI").cls("text-sm text-muted-foreground block mb-1"),
                        UI.select(
                            UI.option("Semua").attr("value", "all"),
                            UI.option("BUY").attr("value", "buy"),
                            UI.option("SELL").attr("value", "sell"),
                        ).cls("w-full h-9 px-3 rounded-md border border-input bg-transparent text-sm"),
                    ),
                ).cls("grid grid-cols-4 gap-4"),
                UI.button("Cari Saham").cls("bg-primary text-primary-foreground px-4 py-2 rounded-md text-sm font-medium mt-6").on_click(ScreenerState.search),
            ).cls("rounded-lg border border-border bg-card p-6 mb-8"),
            
            # Results
            UI.h3("Hasil Screener").cls("font-semibold mb-4"),
            UI.div(
                table_row("BBCA", "Bank Central Asia", 9875, 2.45, "BUY", 85),
                table_row("BMRI", "Bank Mandiri", 6350, 1.85, "BUY", 78),
                table_row("TLKM", "Telkom Indonesia", 3850, 0.78, "HOLD", 62),
                table_row("BBRI", "Bank Rakyat Indonesia", 5525, -0.45, "HOLD", 55),
                table_row("ASII", "Astra International", 5150, -1.15, "SELL", 35),
            ).cls("rounded-lg border border-border overflow-hidden"),
            
        ).cls("max-w-6xl mx-auto py-8 px-8"),
        
        UI.raw('<script>lucide.createIcons();</script>'),
    ).cls("min-h-screen bg-background text-foreground")


def table_row(symbol, name, price, change, signal, score):
    is_positive = change >= 0
    change_class = "text-green-600" if is_positive else "text-red-600"
    signal_class = {"BUY": "bg-green-100 text-green-700", "SELL": "bg-red-100 text-red-700", "HOLD": "bg-yellow-100 text-yellow-700"}.get(signal, "bg-gray-100")
    
    return UI.div(
        UI.span(symbol).cls("w-24 font-semibold text-sm"),
        UI.span(name).cls("flex-1 text-sm text-muted-foreground"),
        UI.span("Rp " + str(price)).cls("w-28 text-sm text-right"),
        UI.span(("+" if is_positive else "") + str(change) + "%").cls("w-20 text-sm text-right " + change_class),
        UI.span(signal).cls("w-16 text-xs text-center font-medium px-2 py-0.5 rounded-full " + signal_class),
        UI.span(str(score)).cls("w-12 text-sm text-primary text-center font-semibold"),
    ).cls("flex items-center px-4 py-3 border-b border-border hover:bg-muted/30")
