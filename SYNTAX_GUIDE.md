# PyX Syntax Guide

> **PyX** - The Python Framework for Modern Web Apps  
> Write Python, Get Beautiful Web UIs

---

## 🚀 Quick Start

```python
from pyx import ui, State, var

class AppState(State):
    count: int = 0
    
    @var
    def doubled(self) -> int:
        return self.count * 2

def page():
    return ui.div(
        ui.h1(f"Count: {AppState.count}"),
        ui.button("Add").on_click(AppState.increment)
    ).p(8)
```

---

## 📖 Core Concepts

### 1. State Management (NEW!)

```python
from pyx import State, var, redirect, alert, toast

class UserState(State):
    # Typed variables = auto-generated setters
    username: str = ""
    email: str = ""
    count: int = 0
    
    # Computed vars - auto-recalculate
    @var
    def is_valid(self) -> bool:
        return len(self.email) > 5
    
    # Handlers can return Actions
    def submit(self):
        if not self.is_valid:
            return alert("Invalid email!")
        return redirect("/dashboard")
```

**Auto-setters**: `set_username()`, `set_email()`, `set_count()` are generated automatically!

### 2. Page Structure

Every page must return an element:

---

## 🎨 UI Strategies

PyX offers three ways to build UIs. Mix and match as needed!

### A. PyxUI (Premium Components 🌟)
High-level, pre-styled components (similar to Shadcn UI). Best for generic layouts.

```python
from pyx import PyxUI, UI, ui

# Card Component
ui.add(
    PyxUI.Card([
        PyxUI.CardHeader([
            PyxUI.CardTitle("Login"),
            PyxUI.CardDescription("Enter your credentials")
        ]),
        PyxUI.CardContent([
            PyxUI.Label("Email"),
            PyxUI.Input(placeholder="user@example.com", className="mb-4"),
            
            PyxUI.Label("Password"),
            PyxUI.Input(type="password", placeholder="••••••", className="mb-6"),
            
            PyxUI.Button("Sign In", className="w-full")
        ])
    ], className="w-96")
)
```

### B. Zen Mode (Rapid Prototyping ⚡)
Fluent API attached to the `ui` helper. Best for quick text and basic layout.

```python
ui.title("Hello World")           # <h1> styled
ui.subtitle("Description here")   # <p> large text
ui.text("Normal paragraph")       # <p> normal
ui.button("Click Me")             # <button> styled
ui.button("Secondary", variant="secondary")
ui.divider()                      # Horizontal line
```

### C. Manual Mode (Full Control 🛠️)
Direct HTML element construction using `UI`. Best for custom designs.

```python
ui.add(UI.h1("Custom Heading").text("red-500"))
ui.add(UI.div("Box").bg("gray-100").p(4))
ui.add(UI.img("/image.png", "alt text"))
```

---

## 📦 Layout Containers

Use Python's `with` statement for nested layouts:

### Row (Horizontal Flex)
```python
with ui.row(gap=4):
    ui.button("Left")
    ui.button("Right")
```

### Column (Vertical Flex)
```python
with ui.col(gap=4):
    ui.text("First")
    ui.text("Second")
    ui.text("Third")
```

### Grid
```python
with ui.grid(cols=3, gap=6):
    ui.button("1")
    ui.button("2")
    ui.button("3")
```

### Container (Generic)
```python
with ui.container() as box:
    box.bg("white").p(8).rounded("xl").shadow("lg")
    ui.text("Custom styled container")
```

---

## 🎯 Styling (Method Chaining)

All elements support Tailwind-like styling via method chaining:

### Colors & Background
```python
.bg("blue-500")        # Background color
.text("white")         # Text color
.border_color("gray-300")
```

### Spacing
```python
.p(4)      # Padding all sides
.px(4)     # Padding horizontal
.py(4)     # Padding vertical
.m(4)      # Margin all sides
.mx(4)     # Margin horizontal
.my(4)     # Margin vertical
```

### Sizing
```python
.w(80)         # Width (Tailwind units)
.w_full()      # Width 100%
.w_screen()    # Width 100vw
.h(40)         # Height
.h_full()      # Height 100%
.h_screen()    # Height 100vh
```

### Flexbox
```python
.flex()              # Display flex
.flex_row()          # Direction row
.flex_col()          # Direction column
.justify("center")   # Justify content
.items("center")     # Align items
.gap(4)              # Gap between items
.grow()              # Flex grow
```

### Interactive States
```python
.hover("bg-blue-600")         # Hover state
.focus("ring-2", "ring-blue-500")
.active("scale-95")
.transition()                  # Smooth transitions
```

---

## 📝 Form Inputs (PyxUI)

Prefer `PyxUI` components for forms:

```python
from pyx import PyxUI

# Input
PyxUI.Input(placeholder="Type here...", name="username")

# Textarea
PyxUI.Textarea(placeholder="Message...", rows=4)

# Switch
PyxUI.Switch(checked=True, name="notifications")

# Select
PyxUI.Select(
    options=[
        {"label": "Option 1", "value": "1"},
        {"label": "Option 2", "value": "2"}
    ], 
    placeholder="Choose..."
)

# Checkbox
PyxUI.Checkbox(checked=False, name="agree")
```

---

## 🎨 Icons (Lucide)

Use generic `Lucide` class:

```python
from pyx import Lucide

# Basic usage
ui.add(Lucide("home"))
ui.add(Lucide("mail", size=20))
ui.add(Lucide("settings", size=24, color="blue-500"))

# Full list: https://lucide.dev/icons
```

---

## 📊 Charts

PyX has built-in `Chart` component (using Chart.js):

```python
from pyx import Chart

ui.add(Chart.line(
    labels=["Jan", "Feb", "Mar"],
    datasets=[
        {"label": "Sales", "data": [100, 150, 200], "color": "blue"},
        {"label": "Costs", "data": [80, 90, 120], "color": "red"}
    ],
    title="Q1 Performance"
))
```

Supported types: `line`, `bar`, `pie`, `doughnut`, `area`, `radar`, `candlestick`.

---

## 📁 Project Structure

Typical MVC structure generated by `pyx init`:

```
my_project/
├── main.py              # Entry point
├── assets/              # Static files
└── modules/             # MVC Modules
    └── home/
        ├── __init__.py
        ├── controller.py # Logic
        ├── state.py      # Data Models
        └── views.py      # UI Components
```

### 1. View (`views.py`)
```python
from pyx import UI, PyxUI
from .controller import HomeController

def home_view():
    return PyxUI.Card([
        PyxUI.Button("Click Me", onClick=HomeController.on_click)
    ])
```

### 2. Controller (`controller.py`)
```python
from pyx import JS

class HomeController:
    @staticmethod
    def on_click():
        print("Clicked!")
        return JS.toast("Hello from Python!", "success")
```

### 3. Entry Point (`main.py`)
```python
import pyx
from modules.home import home_view

app = pyx.App()
app.add_page("/", home_view)

if __name__ == "__main__":
    app.run() # Defaults to main:app
```

### Run Project
```bash
pyx run
# OR
pyx run main:app --reload
```

---

## 📂 Alternate: File-based Routing

For simple sites, you can use `pages/` directory:

```python
# pages/about.py
from pyx import ui

def page():
    return ui.text("About Page")
```

In `app.py`:
```python
from pyx import App, auto_discover_pages

app = App()
for path, page_func in auto_discover_pages("pages"):
    app.add_page(path, page_func)
```

---

## 📚 Resources

- **Lucide Icons**: https://lucide.dev/icons
- **Tailwind Colors**: https://tailwindcss.com/docs/customizing-colors

---

*Built with ❤️ using PyX Framework*
