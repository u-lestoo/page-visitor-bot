import webbrowser
import time

url = "https://example.com"
liczba_wejsc = 10

for i in range(liczba_wejsc):
    webbrowser.open(url)
   print(f"Opened {i+1} time(s)")
    time.sleep(0)  # Enter the number of seconds
