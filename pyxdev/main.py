from pyx import App
from router import ROUTES

# Initialize App
app = App()

# Register Routes Automatically from Registry
for path, handler in ROUTES.items():
    app.add_page(path, handler)

# Expose API for server
app_instance = app.api

if __name__ == "__main__":
    app.run()
