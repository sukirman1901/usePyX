"""
ImpulseAI - Analysis Page
"""
import sys
sys.path.insert(0, '/Users/aaa/Documents/Developer/Framework/PyX')

from pyx import UI
from app.state import StockState


def analysis_page():
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
                    UI.a("Analisis").attr("href", "/analysis").cls("text-sm font-medium text-foreground ml-6"),
                    UI.a("Watchlist").attr("href", "/watchlist").cls("text-sm font-medium text-muted-foreground hover:text-foreground ml-6"),
                ).cls("flex items-center ml-10"),
            ).cls("flex items-center max-w-6xl mx-auto px-8"),
        ).cls("border-b border-border py-4"),
        
        # Content
        UI.div(
            # Search
            UI.div(
                UI.input().attr("placeholder", "Masukkan kode saham (BBCA)").cls("h-10 w-80 px-4 rounded-md border border-input bg-transparent text-sm"),
                UI.button("Analisa").cls("bg-primary text-primary-foreground px-4 py-2 rounded-md text-sm font-medium ml-3"),
            ).cls("flex items-center mb-8"),
            
            # Stock Header
            UI.div(
                UI.div(
                    UI.span("BBCA").cls("text-3xl font-bold"),
                    UI.span("Bank Central Asia Tbk").cls("text-muted-foreground ml-3"),
                ).cls("flex items-baseline"),
                UI.div(
                    UI.span("Rp 9,875").cls("text-4xl font-bold"),
                    UI.span("+2.45%").cls("text-lg font-semibold text-green-600 ml-3"),
                ).cls("flex items-baseline mt-2"),
            ).cls("rounded-lg border border-border bg-card p-6 mb-6"),
            
            # Two columns
            UI.div(
                # Chart
                UI.div(
                    UI.h3("Price Chart").cls("font-semibold mb-4"),
                    UI.div(
                        UI.p("Candlestick Chart").cls("text-muted-foreground"),
                    ).cls("h-80 rounded-lg border border-border bg-muted/20 flex items-center justify-center"),
                ).cls("flex-1 rounded-lg border border-border bg-card p-4"),
                
                # Indicators
                UI.div(
                    UI.h3("Indikator Teknikal").cls("font-semibold mb-4"),
                    indicator_row("RSI (14)", "62.5"),
                    indicator_row("MACD", "0.85"),
                    indicator_row("MA (20)", "Rp 9,750"),
                    indicator_row("MA (50)", "Rp 9,500"),
                    indicator_row("Trend", "UPTREND"),
                ).cls("w-72 ml-6 rounded-lg border border-border bg-card p-4"),
            ).cls("flex"),
            
            # Actions
            UI.div(
                UI.button("Tambah ke Watchlist").cls("bg-primary text-primary-foreground px-4 py-2 rounded-md text-sm font-medium"),
                UI.button("Set Alert").cls("border border-input px-4 py-2 rounded-md text-sm font-medium ml-3"),
            ).cls("mt-8"),
            
        ).cls("max-w-6xl mx-auto py-8 px-8"),
        
        UI.raw('<script>lucide.createIcons();</script>'),
    ).cls("min-h-screen bg-background text-foreground")


def indicator_row(label, value):
    return UI.div(
        UI.span(label).cls("text-sm text-muted-foreground"),
        UI.span(value).cls("text-sm font-medium ml-auto"),
    ).cls("flex items-center py-2 border-b border-border")
