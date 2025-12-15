# PyX Security Analysis

> **Security Status**: ✅ Production-Ready  
> **Date**: 2025-12-15

---

## 📊 Security Features Overview

PyX has a comprehensive security module at `pyx/core/security.py` (643 lines, 20KB+).

### ✅ Implemented Features

| Feature | Location | Status | Description |
|---------|----------|:------:|-------------|
| **Password Hashing** | `security.py` | ✅ | Bcrypt with SHA256 fallback |
| **Password Policy** | `security.py` | ✅ | Configurable strength requirements |
| **Password Strength** | `security.py` | ✅ | Score 0-100 with suggestions |
| **Security Headers** | `security.py` | ✅ | All OWASP recommended headers |
| **HTTPS Redirect** | `security.py` | ✅ | Force HTTPS in production |
| **Account Lockout** | `security.py` | ✅ | Brute-force protection |
| **XSS Prevention** | `security.py` | ✅ | HTML escape & sanitize |
| **Token Generation** | `security.py` | ✅ | Cryptographically secure |
| **API Key Generation** | `security.py` | ✅ | Format: `pyx_xxxxxxxx` |
| **CSRF Protection** | `middleware.py` | ✅ | Token-based |
| **Rate Limiting** | `middleware.py` | ✅ | IP-based |
| **CORS** | `middleware.py` | ✅ | Configurable origins |
| **Input Validation** | `lib/validation.py` | ✅ | Laravel-style rules |
| **Auth Middleware** | `middleware.py` | ✅ | Route protection |
| **Role-based Access** | `middleware.py` | ✅ | `@require_role`, `@require_permission` |

---

## 🔐 Usage Examples

### Password Hashing (Bcrypt)

```python
from pyx import security

# Hash password (uses bcrypt if available)
hash = security.hash_password("my_password")

# Verify password
is_valid = security.verify_password("my_password", hash)
```

### Password Policy

```python
from pyx import security

# Validate against policy
is_valid, errors = security.check_password("weak123")
# errors: ["Must contain uppercase", "Must contain special char"]

# Get strength analysis
result = security.password_strength("MyP@ssw0rd!")
# {
#     "score": 85,
#     "level": "strong",
#     "suggestions": []
# }
```

### Security Headers

```python
from pyx import security

# Add security headers middleware
app.use(security.headers(
    hsts=True,           # Strict-Transport-Security
    csp="default-src 'self'"  # Content-Security-Policy
))
```

**Default headers added:**
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: geolocation=(), camera=(), microphone=()`

### HTTPS Redirect

```python
from pyx import security

# Force HTTPS in production
app.use(security.https_redirect())
```

### Account Lockout (Brute-force Protection)

```python
from pyx import security

# Check if locked
if security.lockout.is_locked(email):
    remaining = security.lockout.remaining_time(email)
    return f"Account locked. Try again in {remaining}s"

# Record failed attempt
if not valid_password:
    locked = security.lockout.record_failure(email)
    if locked:
        return "Too many attempts. Account locked."

# Clear on success
security.lockout.clear(email)
```

### XSS Prevention

```python
from pyx import security

# Escape all HTML
safe_text = security.escape("<script>alert('xss')</script>")
# &lt;script&gt;alert('xss')&lt;/script&gt;

# Sanitize (allow some tags)
safe_html = security.sanitize(
    user_input, 
    allowed_tags=["b", "i", "a", "p"]
)
```

### Token Generation

```python
from pyx import security

# Random token
token = security.generate_token(32)  # 64 char hex

# API key
api_key = security.generate_api_key()  # pyx_xxxxxxxxxxxxxxxx
```

---

## 🛡️ Security Middleware Stack

```python
from pyx import App, security
from pyx import CORSMiddleware, RateLimitMiddleware, CSRFMiddleware, AuthMiddleware

app = App()

# 1. HTTPS Redirect (production)
app.use(security.https_redirect())

# 2. Security Headers
app.use(security.headers(hsts=True))

# 3. CORS
app.use(CORSMiddleware(origins=["https://myapp.com"]))

# 4. Rate Limiting
app.use(RateLimitMiddleware(requests_per_minute=60))

# 5. CSRF Protection  
app.use(CSRFMiddleware())

# 6. Auth
app.use(AuthMiddleware(login_url="/login"))
```

---

## 🔒 Route Protection

```python
from pyx import protected, require_role, require_permission

# Require login
@protected
def dashboard():
    return ui.div("Dashboard")

# Require specific role
@require_role("admin")
def admin_panel():
    return ui.div("Admin Only")

# Require specific permission
@require_permission("users.edit")
def edit_user():
    return ui.div("Edit User")
```

---

## 📋 Security Checklist

| Item | Status |
|------|:------:|
| Bcrypt password hashing | ✅ |
| Security headers | ✅ |
| HTTPS enforcement | ✅ |
| CSRF protection | ✅ |
| XSS prevention | ✅ |
| SQL injection (SQLModel/parameterized) | ✅ |
| Rate limiting | ✅ |
| Account lockout | ✅ |
| Input validation | ✅ |
| Role-based access | ✅ |
| Password policy | ✅ |
| Secure token generation | ✅ |

---

## 🟢 Optional Enhancements (Future)

| Feature | Priority | Status |
|---------|:--------:|:------:|
| JWT Authentication | Low | Optional |
| 2FA/MFA Support | Low | Planned |
| OAuth2 Integration | Low | Planned |
| API Key Auth | Low | ✅ Basic |
| Audit Logging | Low | ✅ Basic |

---

## 🧘 Zen Mode Security

All security features accessible via `security.*`:

```python
from pyx import security

security.hash_password(password)
security.verify_password(password, hash)
security.check_password(password)
security.password_strength(password)
security.escape(text)
security.sanitize(html)
security.generate_token()
security.generate_api_key()
security.headers()
security.https_redirect()
security.lockout.is_locked(identifier)
security.lockout.record_failure(identifier)
security.lockout.clear(identifier)
```

---

*Security audit updated: 2025-12-15*
*Status: ✅ Production-Ready*
