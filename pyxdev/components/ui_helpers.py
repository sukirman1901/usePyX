from pyx.ui import UI, PyxElement, ui

# -------------------------------------------------------------------------
# UI HELPERS
# -------------------------------------------------------------------------

def md_bold(text):
    """
    Parses plain text with **bold** markers into PyxElement struct.
    Example: "Hello **World**" -> Span("Hello ", Strong("World"))
    """
    parts = text.split("**")
    container = PyxElement("span")
    for i, part in enumerate(parts):
        if i % 2 == 1:
            container.add(PyxElement("strong").add(part).font("semibold").text("gray-900"))
        else:
            container.add(PyxElement("span").add(part))
    return container

def make_code_block(code_txt, language="python"):
    """
    Creates a pre/code block with Highlight.js class.
    """
    return PyxElement("pre").cls("bg-gray-50 p-4 rounded-lg text-sm font-mono text-gray-800 border border-gray-200 mb-8 overflow-x-auto") \
        .add(PyxElement("code").cls(f"language-{language} bg-transparent").add(code_txt.strip()))

def Lucide(name, size=24, color="currentColor"):
    return PyxElement("i").attr("data-lucide", name).attr("width", size).attr("height", size).attr("style", f"color: {color}")
