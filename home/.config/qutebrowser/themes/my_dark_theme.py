# Load autoconfig if needed
config.load_autoconfig()

# Define your palette
bg        = "#111314"
bg_light  = "#161819"
hover     = "#1F2121"
border    = "#2B2D2D"
accent    = "#A9B665"   # main green accent
text      = "#F7F3EA"
inactive  = "#f7f3ea36"
red       = "#EA6962"
blue      = "#7DAEA3"
orange    = "#E78A4E"
purple    = "#D3869B"

# Statusbar
c.colors.statusbar.normal.bg = bg
c.colors.statusbar.normal.fg = text
c.colors.statusbar.insert.bg = accent
c.colors.statusbar.insert.fg = bg
c.colors.statusbar.command.bg = bg_light
c.colors.statusbar.command.fg = text

# Tabs
c.colors.tabs.bar.bg = bg
c.colors.tabs.odd.bg = bg_light
c.colors.tabs.odd.fg = inactive
c.colors.tabs.even.bg = bg_light
c.colors.tabs.even.fg = inactive
c.colors.tabs.selected.odd.bg = accent
c.colors.tabs.selected.odd.fg = bg
c.colors.tabs.selected.even.bg = accent
c.colors.tabs.selected.even.fg = bg

# Completion box (autocomplete dropdown)
c.colors.completion.fg = text
c.colors.completion.even.bg = bg_light
c.colors.completion.odd.bg = bg
c.colors.completion.match.fg = accent
c.colors.completion.category.bg = border
c.colors.completion.category.fg = text
c.colors.completion.item.selected.bg = hover
c.colors.completion.item.selected.fg = text
c.colors.completion.item.selected.border.top = accent
c.colors.completion.item.selected.border.bottom = accent

# Downloads
c.colors.downloads.bar.bg = bg
c.colors.downloads.start.bg = blue
c.colors.downloads.start.fg = bg
c.colors.downloads.stop.bg = accent
c.colors.downloads.stop.fg = bg
c.colors.downloads.error.bg = red
c.colors.downloads.error.fg = text

# Hints
c.colors.hints.bg = orange
c.colors.hints.fg = bg
c.colors.hints.match.fg = red

# Messages
c.colors.messages.info.bg = bg_light
c.colors.messages.info.fg = text
c.colors.messages.error.bg = red
c.colors.messages.error.fg = text
c.colors.messages.warning.bg = orange
c.colors.messages.warning.fg = text

# Prompts
c.colors.prompts.bg = bg
c.colors.prompts.fg = text
c.colors.prompts.selected.bg = hover

# Webpage dark mode
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = "dark"

