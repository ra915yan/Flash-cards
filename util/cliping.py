import keyboard
import pyperclip
import time



SAVE_FILE = "captured_text.txt"
SHORTCUT = "windows+shift+c"


def save_clipboard_text():
    
    time.sleep(1)
    pyperclip.copy("")
    keyboard.press_and_release("ctrl+c")
    
    time.sleep(0.2)
    
    try:
        text = pyperclip.paste().strip()
        if text:
            with open(SAVE_FILE,"a",encoding='utf-8') as f:
                f.write(f"{text}\n")
            print("word is copied")
            
    except Exception as e:
        print(e)
        
        
def main():
    
    
    keyboard.add_hotkey(SHORTCUT,save_clipboard_text)
    
    keyboard.wait("esc")
    
if __name__ == "__main__":
    main()