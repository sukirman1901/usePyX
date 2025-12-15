"""
PyX Documentation Site Components
Reusable components for documentation layout.
"""
from pyx import UI, ui


def sidebar_link(text: str, href: str, active: bool = False):
    """Sidebar navigation link"""
    if active:
        el = UI.a(text, href) \
            .block().w_full().px(3).py(2).rounded("md") \
            .bg("blue-50").text("blue-700").font("medium") \
            .transition()
    else:
        el = UI.a(text, href) \
            .block().w_full().px(3).py(2).rounded("md") \
            .text("gray-700").hover("bg-gray-50").transition()
    ui.add(el)
    return el


def sidebar_category(text: str):
    """Sidebar category header"""
    el = UI.p(text).text("xs").font("semibold").text("gray-400") \
        .mt(6).mb(2).px(3).uppercase().tracking("wider")
    ui.add(el)
    return el


def toc_link(text: str, anchor: str, active: bool = False):
    """Table of contents link (right sidebar)"""
    color = "blue-600" if active else "gray-500"
    el = UI.a(text, f"#{anchor}") \
        .block().text("sm").text(color).py(1) \
        .hover("text-blue-600").transition()
    ui.add(el)
    return el


def code_block(code: str, language: str = "python"):
    """Syntax highlighted code block"""
    el = UI.div() \
        .bg("gray-900").rounded("lg").overflow("hidden")
    
    # Header
    header = UI.div().bg("gray-800").px(4).py(2).flex().justify("between").items("center")
    lang_label = UI.span(language).text("sm").text("gray-400")
    copy_btn = UI.button("Copy").text("xs").text("gray-400").hover("text-white") \
        .attr("onclick", f"navigator.clipboard.writeText(`{code}`); PyX.toast('Copied!', 'success')")
    header.add(lang_label)
    header.add(copy_btn)
    
    # Code
    code_el = UI.pre(UI.code(code)).p(4).text("sm").text("gray-100") \
        .overflow("x", "auto").font("mono")
    
    el.add(header)
    el.add(code_el)
    ui.add(el)
    return el


def inline_code(text: str):
    """Inline code styling"""
    return UI.code(text).bg("gray-100").text("gray-800") \
        .px(1.5).py(0.5).rounded("md").text("sm").font("mono")


def feature_item(title: str, description: str):
    """Feature list item with title and description"""
    with ui.col(gap=1):
        ui.add(UI.p(title).font("semibold").text("gray-900"))
        ui.add(UI.p(description).text("gray-600").text("sm"))


def callout(content: str, type: str = "info"):
    """Info/Warning/Tip callout box"""
    colors = {
        "info": ("blue-50", "blue-800", "blue-200", "ℹ️"),
        "warning": ("amber-50", "amber-800", "amber-200", "⚠️"),
        "tip": ("green-50", "green-800", "green-200", "💡"),
        "danger": ("red-50", "red-800", "red-200", "🚨"),
    }
    bg, text, border, icon = colors.get(type, colors["info"])
    
    el = UI.div() \
        .bg(bg).border_l(4).border_color(border) \
        .p(4).rounded("r-lg").flex().gap(3)
    
    icon_el = UI.span(icon).text("lg")
    content_el = UI.p(content).text(text).text("sm")
    
    el.add(icon_el)
    el.add(content_el)
    ui.add(el)
    return el


def doc_heading(text: str, level: int = 1, id: str = None):
    """Documentation heading with anchor"""
    sizes = {
        1: ("4xl", "extrabold", 6),
        2: ("2xl", "bold", 4),
        3: ("xl", "semibold", 3),
    }
    size, weight, mb = sizes.get(level, sizes[2])
    
    anchor_id = id or text.lower().replace(" ", "-")
    
    with ui.row(gap=2):
        if level == 1:
            el = UI.h1(text).text(size).font(weight).text("gray-900").mb(mb)
        elif level == 2:
            el = UI.h2(text).text(size).font(weight).text("gray-900").mt(8).mb(mb) \
                .border_b().border_color("gray-200").pb(2)
        else:
            el = UI.h3(text).text(size).font(weight).text("gray-900").mt(6).mb(mb)
        
        el.id(anchor_id)
        ui.add(el)
        
        # Anchor link
        ui.add(
            UI.a("#", f"#{anchor_id}").text("gray-300").hover("text-blue-500") \
                .opacity(0).group_hover("opacity-100")
        )


def doc_paragraph(text: str):
    """Documentation paragraph"""
    el = UI.p(text).text("gray-600").leading("relaxed").mb(4)
    ui.add(el)
    return el


def doc_list(items: list):
    """Documentation bullet list"""
    with ui.col(gap=2):
        for item in items:
            with ui.row(gap=3):
                ui.add(UI.span("•").text("blue-500").font("bold"))
                ui.add(UI.span(item).text("gray-600"))
