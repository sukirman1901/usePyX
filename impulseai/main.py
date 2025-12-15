"""
ImpulseAI - Platform Analisa Saham Indonesia
Built with PyX Framework - shadcn-inspired UI
"""
import sys
sys.path.insert(0, '/Users/aaa/Documents/Developer/Framework/PyX')

from pyx import App
from pyx.lib.seo import Head

# Import pages
from app.pages.home import home_page
from app.pages.screener import screener_page
from app.pages.analysis import analysis_page
from app.pages.watchlist import watchlist_page

# Create app
app = App()
app._name = "ImpulseAI"  # Set app name

# Register routes
app.add_page("/", home_page)
app.add_page("/screener", screener_page)
app.add_page("/analysis", analysis_page)
app.add_page("/watchlist", watchlist_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200)
