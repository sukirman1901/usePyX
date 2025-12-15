# Deploying PyX Applications

PyX is designed to be easily deployable to any environment that supports Python, including Docker, VPS, and PaaS providers.

## 🐳 Docker (Recommended)

The easiest way to deploy PyX is using Docker. We provide a built-in generator to get you started.

### 1. Generate Dockerfile

Run the following command in your project root:

```bash
pyx g docker
```

This will create a `Dockerfile` and `.dockerignore`.

### 2. Build Image

```bash
docker build -t myapp .
```

### 3. Run Container

```bash
docker run -p 8000:8000 myapp
```

Your app is now running at `http://localhost:8000`.

---

## ☁️ Deploy to Railway/Render

Most modern PaaS providers (Railway, Render, Fly.io) support Docker automatically.

1. Push your code to GitHub.
2. Connect your repository to the service.
3. The service will detect the `Dockerfile` and build it automatically.

**Start Command:**
If asked for a start command (and not using Docker), use:
```bash
pyx run --host 0.0.0.0 --port $PORT --no-reload
```

---

## 🖥️ VPS / Manual Deployment

If you prefer deploying manually to a Ubuntu/Debian server:

### 1. Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip python3-venv git
```

### 2. Clone & Setup

```bash
git clone https://github.com/your/repo.git
cd repo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Systemd Service

Create a service file `/etc/systemd/system/myapp.service`:

```ini
[Unit]
Description=PyX App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/repo
Environment="PATH=/home/ubuntu/repo/venv/bin"
ExecStart=/home/ubuntu/repo/venv/bin/pyx run --host 0.0.0.0 --port 8000 --no-reload
Restart=always

[Install]
WantedBy=multi-user.target
```

### 4. Start Service

```bash
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## ⚙️ Production Checklist

Before going live:

- [ ] **Security Keys**: Ensure `SECRET_KEY` is set via environment variable.
- [ ] **Debug Mode**: Ensure debug is OFF (PyX defaults to no-reload in production).
- [ ] **Database**: Use a production database (PostgreSQL/MySQL) instead of SQLite.
- [ ] **HTTPS**: Use Nginx or a load balancer to handle SSL/HTTPS.
