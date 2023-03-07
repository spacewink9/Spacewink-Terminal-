# import modules for the screens package
from .trades import trades_menu
from .valuation_analysis import valuation_menu
from .fundamental_analysis import fundamental_menu

# create a dictionary to map screen names to their corresponding functions
screen_functions = {
    "trades": trades_menu,
    "valuation analysis": valuation_menu,
    "fundamental analysis": fundamental_menu
}
