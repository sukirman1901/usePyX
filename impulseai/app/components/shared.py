"""
ImpulseAI - Shared Components
"""
import sys
sys.path.insert(0, '/Users/aaa/Documents/Developer/Framework/PyX')

from pyx import ui


def navbar():
    """Navigation bar component."""
    return ui.div(
        ui.div(
            # Logo
            ui.div(
                ui.span("Impulse").font("bold").text("2xl").text_color("white"),
                ui.span("AI").font("bold").text("2xl").text_color("cyan-400"),
            ).flex().items("center").gap(1),
            
            # Nav Links
            ui.div(
                ui.a("Home", href="/").text_color("gray-300").hover("text-white").transition(),
                ui.a("Screener", href="/screener").text_color("gray-300").hover("text-white").transition(),
                ui.a("Analisis", href="/analysis").text_color("gray-300").hover("text-white").transition(),
                ui.a("Watchlist", href="/watchlist").text_color("gray-300").hover("text-white").transition(),
            ).flex().gap(6),
            
            # Search
            ui.div(
                ui.input(placeholder="Cari saham... (BBCA, BBRI)").bg("gray-800").border_color("gray-700").text_color("white").px(4).py(2).rounded("lg").w(64),
            ),
        ).flex().items("center").justify("between").max_w("7xl").mx("auto").px(6),
    ).bg("gray-900").py(4).border_b("1px solid").border_color("gray-800")


def sidebar():
    """Sidebar for market summary."""
    return ui.div(
        ui.h3("Market Summary").font("semibold").text_color("white").mb(4),
        
        # IHSG
        ui.div(
            ui.div(
                ui.span("IHSG").text_color("gray-400"),
                ui.span("7,234.56").text_color("white").font("semibold"),
            ).flex().justify("between"),
            ui.span("+0.45%").text_color("green-400").text("sm"),
        ).bg("gray-800").p(3).rounded("lg").mb(3),
        
        # LQ45
        ui.div(
            ui.div(
                ui.span("LQ45").text_color("gray-400"),
                ui.span("1,023.45").text_color("white").font("semibold"),
            ).flex().justify("between"),
            ui.span("+0.32%").text_color("green-400").text("sm"),
        ).bg("gray-800").p(3).rounded("lg").mb(3),
        
        # IDX30
        ui.div(
            ui.div(
                ui.span("IDX30").text_color("gray-400"),
                ui.span("512.34").text_color("white").font("semibold"),
            ).flex().justify("between"),
            ui.span("-0.12%").text_color("red-400").text("sm"),
        ).bg("gray-800").p(3).rounded("lg"),
        
    ).w(64).p(4).bg("gray-900").border_r("1px solid").border_color("gray-800").h_screen()


def stock_card(symbol: str, name: str, price: float, change: float, signal: str = "HOLD"):
    """Stock card component."""
    is_positive = change >= 0
    change_color = "green-400" if is_positive else "red-400"
    signal_color = "green-500" if signal == "BUY" else ("red-500" if signal == "SELL" else "yellow-500")
    
    return ui.div(
        # Header
        ui.div(
            ui.div(
                ui.span(symbol).font("bold").text("lg").text_color("white"),
                ui.span(name).text("sm").text_color("gray-400"),
            ),
            ui.span(signal).text("xs").font("semibold").text_color("white").bg(signal_color).px(2).py(1).rounded("full"),
        ).flex().justify("between").items("start"),
        
        # Price
        ui.div(
            ui.span(f"Rp {price:,.0f}").text("2xl").font("bold").text_color("white"),
            ui.span(f"{'+' if is_positive else ''}{change:.2f}%").text_color(change_color).font("semibold"),
        ).flex().items("baseline").gap(2).mt(3),
        
    ).bg("gray-800").p(4).rounded("xl").border("1px solid").border_color("gray-700").hover("border-cyan-500").transition().cursor("pointer")


def signal_badge(signal: str, score: int = 0):
    """AI signal badge."""
    colors = {
        "BUY": ("green-500", "green-900"),
        "SELL": ("red-500", "red-900"),
        "HOLD": ("yellow-500", "yellow-900"),
    }
    text_color, bg_color = colors.get(signal, ("gray-500", "gray-900"))
    
    return ui.div(
        ui.span(signal).font("bold"),
        ui.span(f"Score: {score}").text("xs").opacity(80) if score else None,
    ).flex().flex_col().items("center").text_color(text_color).bg(bg_color).px(4).py(2).rounded("lg")


def page_layout(*children):
    """Main page layout wrapper."""
    return ui.div(
        navbar(),
        ui.div(*children).flex_1().overflow("auto"),
    ).flex().flex_col().h_screen().bg("gray-950").text_color("white")


def section(title: str, *children):
    """Section with title."""
    return ui.div(
        ui.h2(title).text("xl").font("bold").text_color("white").mb(4),
        *children,
    ).mb(8)
