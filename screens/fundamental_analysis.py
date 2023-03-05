from utils.display import clear_screen
from fundamental_analysis.advanced_fundamental_analysis import *
from fundamental_analysis.company import *
from fundamental_analysis.employment import *
from fundamental_analysis.earning import *
from fundamental_analysis.losing import *
from fundamental_analysis.insider_info import *
from fundamental_analysis.news_analysis import *
from fundamental_analysis.public_views import *
import matplotlib.pyplot as plt

def fundamental_analysis():
    clear_screen()
    print("Welcome to Fundamental Analysis!\n")
    print("Select an option:")
    print("1. Advanced Fundamental Analysis")
    print("2. Company")
    print("3. Employment")
    print("4. Earnings")
    print("5. Losing")
    print("6. Insider Info")
    print("7. News Analysis")
    print("8. Public Views")
    print("9. Return to main menu\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        advanced_fundamental_analysis()
    elif choice == "2":
        company()
    elif choice == "3":
        employment()
    elif choice == "4":
        earning()
    elif choice == "5":
        losing()
    elif choice == "6":
        insider_info()
    elif choice == "7":
        news_analysis()
    elif choice == "8":
        public_views()
    elif choice == "9":
        return
    else:
        print("Invalid choice. Please try again.")
        fundamental_analysis()

def data_visualize():
    clear_screen()
    print("Welcome to Fundamental Analysis Data Visualization!\n")
    print("Select an option:")
    print("1. Earnings per share")
    print("2. Price to earnings ratio")
    print("3. Dividend yield")
    print("4. Price to book ratio")
    print("5. Debt to equity ratio")
    print("6. Return on equity")
    print("7. Price to sales ratio")
    print("8. Current ratio")
    print("9. Quick ratio")
    print("10. Gross margin")
    print("11. Operating margin")
    print("12. Net margin")
    print("13. Cash flow")
    print("14. Capital expenditures")
    print("15. Inventory analysis")
    print("16. Accounts receivable analysis")
    print("17. Accounts payable analysis")
    print("18. Shareholder equity analysis")
    print("19. Market capitalization")
    print("20. PEG ratio")
    print("21. Return to main menu\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        earnings_per_share()
    elif choice == "2":
        price_to_earnings_ratio()
    elif choice == "3":
        dividend_yield()
    elif choice == "4":
        price_to_book_ratio()
    elif choice == "5":
        debt_to_equity_ratio()
    elif choice == "6":
        return_on_equity()
    elif choice == "7":
        price_to_sales_ratio()
    elif choice == "8":
        current_ratio()
    elif choice == "9":
        quick_ratio()
    elif choice == "10":
        gross_margin()
    elif choice == "11":
        operating_margin()
    elif choice == "12":
        net_margin()
    elif choice == "13":
        cash_flow()
    elif choice == "14":
        capital_expenditures()
    elif choice == "15":
        inventory_analysis()
    elif choice == "16":
        accounts_receivable_analysis()
    elif choice == "17":
    # Price-to-earnings ratio (P/E ratio) chart
    symbol = input("Enter the stock symbol: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # Retrieve P/E ratio data
    df = financial_analysis.get_pe_ratio_data(symbol, start_date, end_date)
    
    # Generate chart
    chart = data_visualize.generate_pe_ratio_chart(df)
    
    # Display chart
    data_visualize.display_chart(chart)
    
else:
    print("Invalid choice. Please try again.")
