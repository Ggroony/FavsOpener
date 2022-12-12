import os
import subprocess
import webbrowser


Outlook = "C:\\Program Files\\Microsoft Office\\root\Office16\\outlook.exe"
Chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"


subprocess.Popen(Outlook)

url = "https://www.youtube.com/"
url2 = "https://calendar.google.com/calendar/u/0/r/week?tab=oc"
url3 ="https://www.dropout.tv/browse"
url4 = "https://docs.google.com/spreadsheets/d/1pmRKcG4k79jJGjWd23lDPNPjuhmj-50eOOUKoxsj14I/edit?usp=drive_web&ouid=103105443447840236307"
url5 ="https://drive.google.com/drive/my-drive"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(Chrome))
webbrowser.get('chrome').open_new_tab(url)
webbrowser.get('chrome').open_new_tab(url2)
webbrowser.get('chrome').open_new_tab(url3)
webbrowser.get('chrome').open_new_tab(url4)
webbrowser.get('chrome').open_new_tab(url5)


  