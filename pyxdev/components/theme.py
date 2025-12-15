class Theme:
    # Brand Colors
    primary = "blue-600"
    primary_hover = "blue-700"
    primary_light = "blue-500"
    primary_soft = "blue-50"
    
    # Secondary / Accents
    accent = "indigo-600"
    success = "green-500"
    danger = "red-600"
    warning = "yellow-500"
    
    # Backgrounds
    bg_body = "white"
    bg_subtle = "gray-50"
    bg_card = "white"
    bg_dark = "slate-950"  # For landing page
    bg_dark_subtle = "slate-900"
    
    # Text
    text_main = "gray-900"
    text_muted = "gray-500"
    text_light = "gray-400"
    text_inverse = "white"
    
    # Borders
    border_default = "gray-200"
    border_light = "gray-100"
    
    # Layout
    max_width = "7xl"
    sidebar_width = "64" # w-64
    
    # Animations
    transition_base = "transition-all duration-200 ease-in-out"
    fade_in = "animate-fade-in"

    @staticmethod
    def button_primary():
        return f"bg-{Theme.primary} hover:bg-{Theme.primary_hover} text-white px-4 py-2 rounded-lg text-sm font-medium {Theme.transition_base}"

    @staticmethod
    def button_secondary():
        return f"bg-white border border-{Theme.border_default} text-{Theme.text_main} hover:bg-{Theme.bg_subtle} px-4 py-2 rounded-lg text-sm font-medium {Theme.transition_base}"

    @staticmethod
    def button_danger():
        return f"bg-{Theme.danger} hover:bg-red-700 text-white px-4 py-2 rounded-lg text-sm font-medium {Theme.transition_base}"

    @staticmethod
    def link_sidebar_active():
        return f"bg-{Theme.primary_soft} text-{Theme.primary}"

    @staticmethod
    def link_sidebar_inactive():
        return f"text-{Theme.text_muted} hover:bg-{Theme.bg_subtle} hover:text-{Theme.text_main}"
