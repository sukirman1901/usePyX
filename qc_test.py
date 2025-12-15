"""
PyX Framework - Comprehensive QC (Quality Control)
===================================================
Tests all major components and features.
"""
import sys
sys.path.insert(0, '/Users/aaa/Documents/Developer/Framework/PyX')

import traceback

print("=" * 70)
print("PyX Framework - Comprehensive QC")
print("=" * 70)

errors = []
warnings = []
passed = []

def test(name, func):
    """Run a test and track result."""
    try:
        func()
        passed.append(name)
        print(f"✅ {name}")
        return True
    except Exception as e:
        errors.append((name, str(e)))
        print(f"❌ {name}: {e}")
        return False

def warn(name, message):
    """Record a warning."""
    warnings.append((name, message))
    print(f"⚠️  {name}: {message}")

# =============================================================================
# 1. CORE IMPORTS
# =============================================================================
print("\n📦 1. Core Imports")
print("-" * 50)

def test_core_imports():
    from pyx import App, Router, Route
    assert App is not None
    
test("App, Router, Route", test_core_imports)

def test_state_imports():
    from pyx import State, StateManager, redirect, alert, toast, refresh, Action, var, computed
    assert State is not None
    assert var is not None
    
test("State, var, computed, actions", test_state_imports)

def test_database_imports():
    from pyx import Model, Field, session, Query, configure_db, create_tables, select
    assert Model is not None
    assert Field is not None
    
test("Model, Field, session, Query", test_database_imports)

def test_session_imports():
    from pyx import Session, SessionStorage, SessionConfig, generate_session_id
    assert Session is not None
    
test("Session, SessionStorage", test_session_imports)

def test_tasks_imports():
    from pyx import background, BackgroundTask, delayed, periodic, run_async
    assert background is not None
    
test("background, delayed, periodic", test_tasks_imports)

def test_events_imports():
    from pyx import EventManager, event
    assert EventManager is not None
    
test("EventManager, event", test_events_imports)

def test_reactive_imports():
    from pyx import rx, cond, foreach, match, text
    assert rx is not None
    
test("rx, cond, foreach, match", test_reactive_imports)

def test_middleware_imports():
    from pyx import (
        LoggingMiddleware, CORSMiddleware, RateLimitMiddleware,
        AuthMiddleware, CSRFMiddleware, protected, require_role
    )
    assert CORSMiddleware is not None
    
test("Middleware classes", test_middleware_imports)

def test_ui_imports():
    from pyx import ui, UI, Element
    assert ui is not None
    
test("ui, UI, Element", test_ui_imports)

def test_components_imports():
    from pyx import PyxUI, Lucide, Chart, DataGrid
    assert PyxUI is not None
    
test("PyxUI, Lucide, Chart, DataGrid", test_components_imports)

# =============================================================================
# 2. STATE FUNCTIONALITY
# =============================================================================
print("\n📦 2. State Functionality")
print("-" * 50)

def test_state_class():
    from pyx import State, var
    
    class TestState(State):
        count: int = 0
        name: str = ""
        
        @var
        def doubled(self) -> int:
            return self.count * 2
    
    state = TestState()
    assert hasattr(state, 'set_count')
    assert hasattr(state, 'set_name')
    state.set_count(5)
    assert state.count == 5
    assert state.doubled == 10
    
test("State class with auto-setters", test_state_class)

def test_computed_vars():
    from pyx import State, var
    
    class CalcState(State):
        a: int = 10
        b: int = 20
        
        @var
        def sum(self) -> int:
            return self.a + self.b
        
        @var
        def product(self) -> int:
            return self.a * self.b
    
    state = CalcState()
    assert state.sum == 30
    assert state.product == 200
    state.a = 5
    assert state.sum == 25
    
test("Computed vars (@var)", test_computed_vars)

def test_actions():
    from pyx.core.state import RedirectAction, AlertAction, ToastAction
    from pyx import redirect, alert, toast
    
    r = redirect("/dashboard")
    assert isinstance(r, RedirectAction)
    assert r.to_dict()["type"] == "navigate"
    
    a = alert("Hello")
    assert isinstance(a, AlertAction)
    assert a.to_dict()["type"] == "alert"
    
    t = toast("Success", "info")
    assert isinstance(t, ToastAction)
    assert t.to_dict()["type"] == "toast"
    
test("Actions (redirect, alert, toast)", test_actions)

def test_state_manager():
    from pyx import State, StateManager
    
    class UserState(State):
        username: str = ""
    
    StateManager.register(UserState)
    s1 = StateManager.get("session1", UserState)
    s1.set_username("user1")
    
    s2 = StateManager.get("session2", UserState)
    s2.set_username("user2")
    
    assert s1.username != s2.username
    
test("StateManager (session isolation)", test_state_manager)

# =============================================================================
# 3. DATABASE FUNCTIONALITY
# =============================================================================
print("\n📦 3. Database Functionality")
print("-" * 50)

def test_model_definition():
    from pyx import Model, Field
    from typing import Optional
    
    class User(Model, table=True):
        __tablename__ = "qc_users"
        id: Optional[int] = Field(default=None, primary_key=True)
        email: str = Field(unique=True)
        name: str
    
    assert User is not None
    
test("Model definition", test_model_definition)

def test_database_config():
    from pyx.core.database import DatabaseConfig, configure_db
    
    configure_db("sqlite:///qc_test.db")
    assert DatabaseConfig._db_url == "sqlite:///qc_test.db"
    
test("Database configuration", test_database_config)

def test_session_context():
    from pyx import session, create_tables
    from pyx.core.database import DatabaseConfig
    
    # Make sure we have a config
    if not DatabaseConfig._db_url:
        from pyx import configure_db
        configure_db("sqlite:///qc_test.db")
    
    create_tables()
    
    with session() as db:
        assert db is not None
        
test("Session context manager", test_session_context)

# =============================================================================
# 4. SESSION FUNCTIONALITY
# =============================================================================
print("\n📦 4. HTTP Session Functionality")
print("-" * 50)

def test_session_create():
    from pyx.core.session import Session
    
    s = Session()
    s.set('user_id', 123)
    s.set('role', 'admin')
    s.save()
    
    assert s.get('user_id') == 123
    assert s['role'] == 'admin'
    
test("Session create & store", test_session_create)

def test_session_restore():
    from pyx.core.session import Session, SessionStorage
    
    s1 = Session()
    s1['test'] = 'value'
    s1.save()
    
    s2 = Session.from_cookie(s1.session_id)
    assert s2['test'] == 'value'
    
test("Session restore from cookie", test_session_restore)

# =============================================================================
# 5. BACKGROUND TASKS
# =============================================================================
print("\n📦 5. Background Tasks")
print("-" * 50)

def test_background_decorator():
    from pyx import background
    import time
    
    @background
    def slow_task():
        time.sleep(0.1)
        return "done"
    
    future = slow_task()
    result = future.result(timeout=2)
    assert result == "done"
    
test("@background decorator", test_background_decorator)

def test_delayed_decorator():
    from pyx import delayed
    import time
    
    @delayed(0.1)
    def delayed_task():
        return "delayed_done"
    
    future = delayed_task()
    result = future.result(timeout=2)
    assert result == "delayed_done"
    
test("@delayed decorator", test_delayed_decorator)

# =============================================================================
# 6. AUTH MODULE
# =============================================================================
print("\n📦 6. Auth Module (contrib)")
print("-" * 50)

def test_auth_user():
    from pyx.contrib.auth import User
    
    user = User(email="test@pyx.dev", username="testuser")
    user.set_password("secret123")
    
    assert user.check_password("secret123") == True
    assert user.check_password("wrong") == False
    
test("User model & password", test_auth_user)

def test_auth_state():
    from pyx.contrib.auth import AuthState
    
    auth = AuthState()
    assert hasattr(auth, 'set_email')
    assert hasattr(auth, 'set_password')
    assert hasattr(auth, 'login')
    assert hasattr(auth, 'logout')
    
test("AuthState class", test_auth_state)

# =============================================================================
# 7. SECURITY MODULE
# =============================================================================
print("\n📦 7. Security Module")
print("-" * 50)

def test_security_imports():
    from pyx.core.security import (
        security, PasswordHasher, PasswordPolicy,
        SecurityHeaders, HTTPSRedirect, AccountLockout,
        escape_html, sanitize_html, generate_token
    )
    assert security is not None
    
test("Security imports", test_security_imports)

def test_password_hashing():
    from pyx.core.security import PasswordHasher
    
    hash = PasswordHasher.hash("testpassword")
    assert PasswordHasher.verify("testpassword", hash) == True
    assert PasswordHasher.verify("wrong", hash) == False
    
test("Password hashing", test_password_hashing)

def test_xss_prevention():
    from pyx.core.security import escape_html
    
    result = escape_html("<script>alert('xss')</script>")
    assert "<script>" not in result
    assert "&lt;script&gt;" in result
    
test("XSS escape", test_xss_prevention)

def test_token_generation():
    from pyx.core.security import generate_token, generate_api_key
    
    token = generate_token(32)
    assert len(token) > 20  # URL-safe encoding varies
    
    api_key = generate_api_key()
    assert api_key.startswith("pyx_")
    
test("Token generation", test_token_generation)

def test_account_lockout():
    from pyx.core.security import AccountLockout
    
    lockout = AccountLockout(max_attempts=3, lockout_minutes=1)
    
    lockout.record_failure("test@email.com")
    lockout.record_failure("test@email.com")
    
    assert lockout.is_locked("test@email.com") == False
    
    lockout.record_failure("test@email.com")
    assert lockout.is_locked("test@email.com") == True
    
    lockout.clear("test@email.com")
    assert lockout.is_locked("test@email.com") == False
    
test("Account lockout", test_account_lockout)

# =============================================================================
# 8. UI MODULE
# =============================================================================
print("\n📦 8. UI Module")
print("-" * 50)

def test_ui_elements():
    from pyx import ui
    
    div = ui.div("Hello")
    assert div is not None
    
    btn = ui.button("Click")
    assert btn is not None
    
test("Basic UI elements", test_ui_elements)

def test_ui_chaining():
    from pyx import ui
    
    el = ui.div("Test").bg("blue-500").p(4).rounded("lg").shadow("md")
    assert el is not None
    
test("UI method chaining", test_ui_chaining)

def test_ui_nesting():
    from pyx import ui
    
    el = ui.div(
        ui.h1("Title"),
        ui.p("Description"),
        ui.button("Click")
    )
    assert el is not None
    
test("UI nesting", test_ui_nesting)

# =============================================================================
# 9. CLI MODULE
# =============================================================================
print("\n📦 9. CLI Module")
print("-" * 50)

def test_cli_app():
    from pyx.cli import app, db_app
    assert app is not None
    assert db_app is not None
    
test("CLI app & db_app", test_cli_app)

# =============================================================================
# 10. LIB MODULES
# =============================================================================
print("\n📦 10. Lib Modules (Batteries)")
print("-" * 50)

def test_seo_module():
    from pyx.lib.seo import Metadata, Head, JSONLD, seo
    assert Metadata is not None
    assert JSONLD is not None
    
test("SEO module", test_seo_module)

def test_email_module():
    from pyx.lib.email import Email, email
    assert Email is not None
    assert email is not None
    
test("Email module", test_email_module)

def test_jobs_module():
    from pyx.lib.jobs import jobs, BackgroundWorker
    assert jobs is not None
    
test("Jobs module", test_jobs_module)

def test_i18n_module():
    from pyx.lib.i18n import I18n, i18n, t
    assert I18n is not None
    assert i18n is not None
    
test("i18n module", test_i18n_module)

def test_pwa_module():
    from pyx.lib.pwa import PWAConfig
    assert PWAConfig is not None
    
test("PWA module", test_pwa_module)

def test_validation_module():
    from pyx.lib.validation import Validator
    assert Validator is not None
    
test("Validation module", test_validation_module)

# =============================================================================
# CLEANUP
# =============================================================================
print("\n📦 Cleanup")
print("-" * 50)

import os
for f in ["qc_test.db", "test_pyx.db"]:
    if os.path.exists(f):
        os.remove(f)
        print(f"  🗑️  Removed {f}")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print("QC SUMMARY")
print("=" * 70)

total = len(passed) + len(errors)
percentage = (len(passed) / total * 100) if total > 0 else 0

print(f"\n✅ PASSED: {len(passed)}/{total} ({percentage:.1f}%)")

if warnings:
    print(f"\n⚠️  WARNINGS: {len(warnings)}")
    for name, msg in warnings:
        print(f"   • {name}: {msg}")

if errors:
    print(f"\n❌ ERRORS: {len(errors)}")
    for name, err in errors:
        print(f"   • {name}: {err}")
else:
    print(f"\n🎉 ALL TESTS PASSED!")

print("=" * 70)

if len(errors) == 0:
    print("\n✅ PyX Framework QC: PASSED")
else:
    print(f"\n⚠️  PyX Framework QC: {len(errors)} issues found")
