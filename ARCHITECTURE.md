# PyX Framework Architecture

> **Modular Reactive MVC** - The Evolution of Traditional MVC for Real-time Python Apps

---

## 📐 Philosophy

PyX uses a **Modular Reactive MVC** pattern. Unlike traditional MVC (Laravel/Django) which is request-response based, PyX is **Stateful & Event-Driven**.

| Traditional MVC | PyX Reactive MVC |
|-----------------|------------------|
| Controller dies after response | Controller stays alive (Stateful) |
| View is passive HTML | View is reactive Python UI |
| Model = Database only | Model = Database + Live State |
| Form POST → Controller | Direct binding (on_click → handler) |

---

## 📁 Folder Structure

### The Modular Approach

Instead of separating `models/`, `views/`, `controllers/` globally, PyX groups them **per Feature/Module**.

```
your-project/
├── main.py             # Entry point
├── modules/            # Feature modules
│   ├── auth/
│   │   ├── models.py       # [M] Database schema
│   │   ├── views.py        # [V] UI components
│   │   ├── controller.py   # [C] Logic & Events
│   │   └── state.py        # [C] Reactive State
│   │
│   ├── dashboard/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── controller.py
│   │   └── state.py
│   │
│   └── home/
│       ├── views.py        # Simple modules might just have views
│       └── controller.py
│
├── components/         # Reusable UI components
│
└── assets/             # Static files (CSS, images)
```

---

## 🧩 The Three Layers

### 1. Model (`models.py`)

**"The Memory"** - Database schema definitions.

**Rules:**
- ✅ Only data structure definitions
- ❌ NO UI imports (`pyx.ui`)
- ❌ NO business logic

**Base:** `pyx.Model` (Wrapper for SQLModel)

```python
# modules/auth/models.py
from pyx import Model, Column

class User(Model, table=True):
    id: int | None = Column(primary_key=True)
    email: str = Column(unique=True, index=True)
    password: str
    full_name: str = Column(default="User")
    is_active: bool = True
```

---

### 2. View (`views.py`)

**"The Face"** - Visual UI components.

**Rules:**
- ✅ Pure UI code (`PyxUI` or `ui` builder)
- ✅ Receives handlers/state from Controller
- ❌ NO database queries
- ❌ NO business logic

**Pattern:** "Dumb Components" - they only draw what they're told.

```python
# modules/auth/views.py
from pyx import ui, PyxUI
from .controller import AuthController

def login_view():
    return PyxUI.Card([
        PyxUI.CardHeader([
            PyxUI.CardTitle("Login")
        ]),
        PyxUI.CardContent([
            PyxUI.Input(placeholder="Email", name="email"),
            PyxUI.Input(placeholder="Password", name="password", type="password"),
            
            PyxUI.Button("Sign In", onClick=AuthController.handle_login)
        ])
    ])
```

---

### 3. Controller (`controller.py`)

**"The Brain"** - Connects Model and View.

**Responsibilities:**
- ✅ Receive input from View (Event Handlers)
- ✅ Process data with Model (Database)
- ✅ Update Reactive State (`state.py`)
- ✅ Trigger UI updates (Toast, Navigation)

```python
# modules/auth/controller.py
from pyx import db, JS
from .models import User

class AuthController:
    @staticmethod
    def handle_login(email: str, password: str):
        # 1. Query Model
        user = db.find_by(User, email=email)
        
        # 2. Business Logic
        if user and user.password == password:
            print(f"Welcome {user.full_name}!")
            return JS.navigate("/dashboard")
        else:
            return JS.toast("Invalid credentials", "error")
```

---

### 4. State (`state.py`)

```python
# modules/dashboard/state.py
from pyx import State, var

class DashboardState(State):
    # Typed vars = auto-setters generated!
    active_users: int = 0
    search_query: str = ""
    
    # Computed vars - auto-recalculate
    @var
    def has_users(self) -> bool:
        return self.active_users > 0
    
    # Event handlers
    def refresh(self):
        self.active_users = fetch_users_count()
```

**NEW Features (2025-12-15):**
- Auto-generated setters (`set_active_users`, `set_search_query`)
- Computed vars with `@var` decorator
- Action returns (`redirect()`, `alert()`, `toast()`)
- Session isolation per user

---

## 🔌 Database API

PyX provides a clean wrapper over SQLModel (NEW API):

```python
from pyx import Model, Field, session, Query, select

# Define models
class User(Model, table=True):
    id: int = Field(primary_key=True)
    email: str = Field(unique=True)
    name: str

# Create
with session() as db:
    user = User(email="test@mail.com", name="John")
    db.add(user)
    db.commit()

# Query
users = Query(User).filter(User.name == "John").all()
user = Query.get(User, 1)

# Advanced
with session() as db:
    result = db.exec(select(User).where(User.email.contains("@"))).all()
```

### CLI Commands (NEW!)

```bash
pyx db init              # Initialize Alembic
pyx db makemigrations    # Generate migration
pyx db migrate           # Apply migrations
pyx db rollback          # Rollback migration
```

---

## 🔌 Database API

PyX provides a clean wrapper over SQLModel:

```python
from pyx import db, Model, Column

# Initialize
db.connect("sqlite:///app.db")
db.init()  # Create tables

# CRUD Operations
user = User(email="test@mail.com", password="123")
db.save(user)           # Insert/Update

db.find_all(User)       # Get all users
db.find_by_id(User, 1)  # Find by ID
db.find_by(User, email="test@mail.com")  # Find by field
db.find_many(User, is_active=True)       # Find multiple

db.delete(user)         # Delete
db.count(User)          # Count records
```

---

## 🚦 Routing

### File-based Routing (Simple Pages)
```
pages/index.py      → /
pages/about.py      → /about
pages/docs/api.py   → /docs/api
```

### Explicit Routing (`app.add_page`)
In `main.py`:
```python
from modules.auth.views import login_view
from modules.dashboard.views import dashboard_view

app.add_page("/login", login_view)
app.add_page("/dashboard", dashboard_view)
```

---

## 🎯 Best Practices

1.  **Keep Views Dumb** - Views should only render UI based on data they receive.
2.  **Fat Controllers are OK** - Unlike traditional MVC, PyX controllers can hold more logic since they're stateful.
3.  **Use `services.py`** - If controller gets too complex, extract logic to a `services.py` file.
4.  **Type Everything** - Always use type hints (`email: str`, `user: User`).
5.  **One Module = One Feature** - Don't mix auth logic with dashboard logic.

---

## 🔄 Data Flow

```
┌─────────┐     ┌────────────┐     ┌───────┐
│  View   │ ──► │ Controller │ ──► │ Model │
│ (PyxUI) │ ◄── │  (Logic)   │ ◄── │ (DB)  │
└─────────┘     └────────────┘     └───────┘
     │                │
     └── Event ───────┘
         (onClick)
```

1.  **View** displays UI, user interacts (clicks button)
2.  **Event** triggers Controller static method with data
3.  **Controller** queries/updates Model
4.  **Model** returns data
5.  **Controller** returns **JS Action** (Toast, Navigate, or DOM Update)

---

## 🆚 Comparison

| Aspect | Laravel | Next.js | PyX |
|--------|---------|---------|-----|
| UI Language | Blade (HTML) | JSX (JavaScript) | Python (Zen Mode) |
| Context Switch | PHP ↔ HTML | JS ↔ JSX ↔ API | **None** |
| Controller State | Dies per request | Needs API | **Stateful** |
| Event Binding | Form POST | API calls | **Direct (onClick)** |
| Learning Curve | Medium | Medium | **Low** |

---

*Built with ❤️ using PyX Framework*
