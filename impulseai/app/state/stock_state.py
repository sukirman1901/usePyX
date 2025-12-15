"""
ImpulseAI State Management
"""
import sys
sys.path.insert(0, '/Users/aaa/Documents/Developer/Framework/PyX')

from pyx import State, var, redirect, toast
from typing import List, Optional
from datetime import datetime


class StockState(State):
    """State for stock analysis."""
    
    # Current stock
    symbol: str = ""
    stock_name: str = ""
    
    # Price data
    current_price: float = 0.0
    change_percent: float = 0.0
    volume: int = 0
    
    # Technical indicators
    rsi: float = 0.0
    macd: float = 0.0
    signal: float = 0.0
    ma_20: float = 0.0
    ma_50: float = 0.0
    
    # AI Analysis
    ai_score: int = 0  # 0-100
    ai_signal: str = ""  # BUY, SELL, HOLD
    ai_reason: str = ""
    
    @var
    def is_bullish(self) -> bool:
        return self.change_percent > 0
    
    @var
    def trend(self) -> str:
        if self.ma_20 > self.ma_50:
            return "UPTREND"
        elif self.ma_20 < self.ma_50:
            return "DOWNTREND"
        return "SIDEWAYS"
    
    @var
    def rsi_signal(self) -> str:
        if self.rsi > 70:
            return "OVERBOUGHT"
        elif self.rsi < 30:
            return "OVERSOLD"
        return "NEUTRAL"
    
    @var
    def formatted_price(self) -> str:
        return f"Rp {self.current_price:,.0f}"
    
    @var
    def formatted_change(self) -> str:
        sign = "+" if self.change_percent >= 0 else ""
        return f"{sign}{self.change_percent:.2f}%"
    
    def load_stock(self, symbol: str):
        """Load stock data (simulated)."""
        self.symbol = symbol.upper()
        
        # Simulated data - in real app, fetch from API
        stock_data = {
            "BBCA": {"name": "Bank Central Asia", "price": 9875, "change": 1.25, "volume": 15000000},
            "BBRI": {"name": "Bank Rakyat Indonesia", "price": 5525, "change": -0.45, "volume": 45000000},
            "TLKM": {"name": "Telkom Indonesia", "price": 3850, "change": 0.78, "volume": 25000000},
            "ASII": {"name": "Astra International", "price": 5150, "change": -1.15, "volume": 12000000},
            "BMRI": {"name": "Bank Mandiri", "price": 6350, "change": 2.10, "volume": 18000000},
        }
        
        if self.symbol in stock_data:
            data = stock_data[self.symbol]
            self.stock_name = data["name"]
            self.current_price = data["price"]
            self.change_percent = data["change"]
            self.volume = data["volume"]
            
            # Simulated technical indicators
            self.rsi = 55 + (hash(self.symbol) % 30)
            self.macd = 0.5 + (hash(self.symbol) % 10) / 10
            self.signal = 0.3 + (hash(self.symbol) % 10) / 10
            self.ma_20 = self.current_price * 0.98
            self.ma_50 = self.current_price * 0.95
            
            # Simulated AI analysis
            self.ai_score = 50 + (hash(self.symbol) % 45)
            self.ai_signal = "BUY" if self.ai_score > 70 else ("SELL" if self.ai_score < 40 else "HOLD")
            self.ai_reason = f"Berdasarkan analisa teknikal dan fundamental, {self.symbol} menunjukkan potensi {'kenaikan' if self.ai_score > 60 else 'penurunan'}."
            
            return toast(f"Data {self.symbol} berhasil dimuat", "success")
        else:
            return toast(f"Saham {self.symbol} tidak ditemukan", "error")


class ScreenerState(State):
    """State for stock screener."""
    
    # Filters
    min_price: float = 0.0
    max_price: float = 100000.0
    min_volume: int = 0
    sector: str = ""
    signal_type: str = ""  # BUY, SELL, HOLD, ALL
    
    # Results
    results: list = []
    loading: bool = False
    
    @var
    def result_count(self) -> int:
        return len(self.results)
    
    @var
    def has_results(self) -> bool:
        return len(self.results) > 0
    
    def search(self):
        """Run screener search."""
        self.loading = True
        
        # Simulated results
        self.results = [
            {"symbol": "BBCA", "name": "Bank Central Asia", "price": 9875, "change": 1.25, "signal": "BUY", "score": 85},
            {"symbol": "BMRI", "name": "Bank Mandiri", "price": 6350, "change": 2.10, "signal": "BUY", "score": 78},
            {"symbol": "TLKM", "name": "Telkom Indonesia", "price": 3850, "change": 0.78, "signal": "HOLD", "score": 62},
            {"symbol": "BBRI", "name": "Bank Rakyat Indonesia", "price": 5525, "change": -0.45, "signal": "HOLD", "score": 55},
            {"symbol": "ASII", "name": "Astra International", "price": 5150, "change": -1.15, "signal": "SELL", "score": 35},
        ]
        
        # Filter by signal
        if self.signal_type and self.signal_type != "ALL":
            self.results = [r for r in self.results if r["signal"] == self.signal_type]
        
        self.loading = False
        return toast(f"Ditemukan {len(self.results)} saham", "info")
    
    def clear_filters(self):
        """Reset all filters."""
        self.min_price = 0.0
        self.max_price = 100000.0
        self.min_volume = 0
        self.sector = ""
        self.signal_type = ""
        self.results = []


class WatchlistState(State):
    """State for user watchlist."""
    
    watchlist: list = []
    
    @var
    def watchlist_count(self) -> int:
        return len(self.watchlist)
    
    @var
    def has_watchlist(self) -> bool:
        return len(self.watchlist) > 0
    
    def add_stock(self, symbol: str):
        """Add stock to watchlist."""
        symbol = symbol.upper()
        if symbol not in self.watchlist:
            self.watchlist = self.watchlist + [symbol]
            return toast(f"{symbol} ditambahkan ke watchlist", "success")
        return toast(f"{symbol} sudah ada di watchlist", "warning")
    
    def remove_stock(self, symbol: str):
        """Remove stock from watchlist."""
        if symbol in self.watchlist:
            self.watchlist = [s for s in self.watchlist if s != symbol]
            return toast(f"{symbol} dihapus dari watchlist", "success")
