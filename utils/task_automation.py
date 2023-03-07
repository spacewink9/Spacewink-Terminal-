import time
import pyautogui
import keyboard
import os

class TaskAutomation:
    def __init__(self):
        pass
        
    def open_terminal(self):
        # open the terminal application
        os.system("gnome-terminal")

    def run_auto_ai_analysis(self):
        # switch to the terminal window
        time.sleep(2)
        pyautogui.hotkey('alt', 'tab')

        # navigate to the auto AI analysis screen
        time.sleep(1)
        pyautogui.write('auto_ai_analysis')
        pyautogui.press('enter')

        # run the auto AI analysis
        time.sleep(2)
        pyautogui.write('1')
        pyautogui.press('enter')

        # wait for the analysis to complete
        time.sleep(30)

        # exit the auto AI analysis screen
        pyautogui.write('4')
        pyautogui.press('enter')

    def run_stock_analysis(self):
        # switch to the terminal window
        time.sleep(2)
        pyautogui.hotkey('alt', 'tab')

        # navigate to the stock analysis screen
        time.sleep(1)
        pyautogui.write('stock_analysis')
        pyautogui.press('enter')

        # run the stock analysis
        time.sleep(2)
        pyautogui.write('1')
        pyautogui.press('enter')

        # wait for the analysis to complete
        time.sleep(30)

        # exit the stock analysis screen
        pyautogui.write('4')
        pyautogui.press('enter')

    def send_email_notification(self):
        # switch to the terminal window
        time.sleep(2)
        pyautogui.hotkey('alt', 'tab')

        # navigate to the email management screen
        time.sleep(1)
        pyautogui.write('email_management')
        pyautogui.press('enter')

        # send the email notification
        time.sleep(2)
        pyautogui.write('2')
        pyautogui.press('enter')

        # exit the email management screen
        pyautogui.write('4')
        pyautogui.press('enter')

    def run_task_automation(self):
        # open the terminal
        self.open_terminal()

        # wait for the terminal to open
        time.sleep(5)

        # run the auto AI analysis
        self.run_auto_ai_analysis()

        # run the stock analysis
        self.run_stock_analysis()

        # send the email notification
        self.send_email_notification()

        # exit the terminal
        keyboard.press_and_release('ctrl+shift+w')
