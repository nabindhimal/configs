from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
import os
import subprocess
from libqtile import hook
from libqtile.widget import Mpd2
from libqtile.config import Key
from libqtile.command import lazy

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"

catppuccin = {
    "flamingo": "#F2CDCD",
    "lavander": "#b4befe",
    "mauve": "#cba6f7",
    "pink": "#f5c2e7",
    "maroon": "#e8a2af",
    "red": "#f28fad",
    "peach": "#f8bd96",
    "yellow": "#fae3b0",
    "green": "#abe9b3",
    "teal": "#b4e8e0",
    "blue": "#96cdfb",
    "sky": "#89dceb",
    "white": "#d9e0ee",
    "gray": "#6e6c7e",
    "black": "#1a1826",
    # "crust": "#1E1E2E",
    "crust": "#111111",
    "pure":"#CDD6F4",
    "purple":"#6d6dae",
        }



color_schema = catppuccin


keys = [

    #Launch Calculator
    Key([], "XF86Calculator", lazy.spawn("galculator")),

    # Mute Microphone
    Key([], "XF86AudioMicMute", lazy.spawn("/home/mennnk/bin/changevolume micmute")),
    
    # Take Screenshot
    Key([], "Print", lazy.spawn("gnome-screenshot -i")),

    # Decrease volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("/home/mennnk/bin/changevolume down")),

    # Increase volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("/home/mennnk/bin/changevolume up")),

    # Mute Volume
    Key([], "XF86AudioMute", lazy.spawn("/home/mennnk/bin/changevolume mute")),

    # Lock Screen
    Key([], "F10", lazy.spawn("cinnamon-screensaver-command -l")),



# Add dedicated sxhkdrc to autostart.sh script

# CLOSE WINDOW, RELOAD AND QUIT QTILE
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

# CHANGE FOCUS USING VIM OR DIRECTIONAL KEYS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# MOVE WINDOWS UP OR DOWN,LEFT OR RIGHT USING VIM KEYS
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_column_right()),

# MOVE WINDOWS UP OR DOWN,LEFT OR RIGHT USING DIRECTIONAL KEYS
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_column_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_column_right()),

# RESIZE UP, DOWN, LEFT, RIGHT USING VIM KEYS
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# RESIZE UP, DOWN, LEFT, RIGHT USING DIRECTIONAL KEYS
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
     Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
     Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
     Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# QTILE LAYOUT KEYS
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
	Key([mod, "shift"], "z", lazy.layout.normalize(), desc="Reset all window sizes"),

    #Scratchpad Keys

    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('music')),

    Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle('news')),

    Key([mod], "f", lazy.group['scratchpad'].dropdown_toggle('fox')),


    Key([mod], "g", lazy.group['scratchpad'].dropdown_toggle('mail')),

    Key(['control'], 'space', lazy.group['scratchpad'].dropdown_toggle('alacritty')),
    ]

# end of keys

# Groups
groups = [
        Group(i) for i in [ "\uf120", "\uf19d", "", "\uf07c" , "\uf03d", "\uf15c", "\uf269", "\uf0e0", ""  ]   
		]


# Add ScratchPad group
scratchpad_group = ScratchPad("scratchpad", [
    
    DropDown("music", "alacritty -e ncmpcpp", x=0.15, y=0.1, height=0.9, width=0.7, on_focus_lost_hide=False),

    DropDown("news", "alacritty -e newsboat", x=0.25, y=0.1, height=0.9, width=0.5,on_focus_lost_hide=False),
    
    DropDown("fox", "librewolf", x=0.1, y=0.1, height=0.9, width=0.8, on_focus_lost_hide=False),

    # DropDown("mail", "alacritty -e neomutt", x=0.25, y=0.1, height=0.9, width=0.5,on_focus_lost_hide=False),

    DropDown("alacritty", "alacritty", x=0.1, y=0.06666666, height=0.9, width=0.8, on_focus_lost_hide=False),

    ])


# Append the ScratchPad group to the existing groups list
groups.append(scratchpad_group)



group_keys = [str(i) for i in range(1, 10)]

# workspace changer

for i, key in enumerate(group_keys):
    keys.extend(
        [
            # mod1 + number or icon of group = switch to group
            Key(
                [mod],
                key,
                lazy.group[groups[i].name].toscreen(),
                desc="Switch to group {}".format(groups[i].name),
            ),
            # mod1 + shift + number or icon of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                key,
                lazy.window.togroup(groups[i].name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(groups[i].name),
            ),
        ]
    )



layouts = [
    layout.Columns(margin=3, num_columns=3, insert_position=1, border_focus="#bd93f9", border_normal="#282836", border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(border_focus="#bd93f9", border_normal="#282836"),
    # layout.Matrix(border_focus="#bd93f9", border_normal="#282836"),
    layout.MonadTall(margin=3, border_width=6, border_focus="#f28fad", border_normal="#282836"),
    # layout.MonadWide(border_focus="#bd93f9", border_normal="#282836"),
    # layout.RatioTile(margin=4, border_width=4, border_focus="#f8bd96", border_normal="#282836"),
    # layout.Tile(border_focus="#bd93f9", border_normal="#282836"),
    # layout.TreeTab(border_focus="#bd93f9", border_normal="#282836"),
    # layout.VerticalTile(border_focus="#bd93f9", border_normal="#282836"),
    # layout.Zoomy(border_focus="#bd93f9", border_normal="#282836"),
]

widget_defaults = dict(
	font='JetBrains Mono Nerd Font',
    forground=catppuccin["pure"],
    fontsize=18,
    padding=2,
)
extension_defaults = widget_defaults.copy()

def get_widgets(primary=False):
    widgets = [
        widget.Spacer(
            length=7,
            background=catppuccin["pure"],
            ),
        widget.Image(
            filename= "~/bin/logo.svg" , scale = "False",
            background =catppuccin["pure"],
            ),    
         widget.Spacer(
            length=7,
            background=catppuccin["pure"],
            ),
        widget.GroupBox(
            highlight_method="line",
            background=catppuccin["crust"],
            highlight_color=[catppuccin["pure"], catppuccin["purple"]],
            inactive=catppuccin["purple"],
            ),
        widget.Spacer(
            length=10,
            background=catppuccin["crust"],
            ),
        widget.Prompt(
            foreground='#ea6962',
            background=catppuccin["crust"],
            ),
        widget.WindowName(
            fontsize=16,
            foreground=catppuccin["pure"],
            background=catppuccin["crust"],
            ),
        widget.Mpd2(
            server="127.0.0.1",
            port=6565,
            update_interval=1,
            foreground=catppuccin["pure"],
            background=catppuccin["crust"],
            ),
         widget.Spacer(
            length=12,
            background=catppuccin["crust"],
            ),
        widget.Spacer(
            length=12,
            background=catppuccin["crust"],
            ),

        widget.Clock(
            format="󰥔 %I:%M %p",
            foreground=catppuccin["pure"],
            background=catppuccin["crust"],
            ),
        widget.Spacer(
           length = 10, 
           background=catppuccin["crust"],
            ),
        widget.Image(
            filename= "~/bin/debian.png" , scale = "False",
            background = catppuccin["crust"],
            ),
        widget.Spacer(
            length=7,
            background= catppuccin["crust"],
            ),
        ]
    return widgets

screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary=True),
            24,
            background="#00000000",
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="qimgv"),  # q image viewer
        Match(wm_class="Galculator"),  # calculator
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=catppuccin["sky"],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
