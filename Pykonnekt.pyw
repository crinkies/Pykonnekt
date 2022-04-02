import urllib.request
import subprocess
import threading
import keyboard
import random
import time
import os

from plyer import notification as n
'''
License:MIT
Author:github.com/crinkies
'''
quitProcess = False
url_list = ["1.1.1.1","8.8.8.8","8.8.4.4","1.0.0.1","208.67.220.220","208.67.222.222"]
reconnects = 0
path = os.path.expanduser('~\Documents\Pykonnekt\\')
    
def main():
    try:
        host_file = open(f"{path}Network.txt", "r")
        network = host_file.readline().lower().strip()
        host_file.close()
        m_body = "Pykonnekt is monitoring your network state."
        notif(m_body)
        new_thread(key_listen)
        new_thread(check_connection(network))
    except:
        try:
            os.mkdir(path)
        except:
            pass
        try:
            urllib.request.urlretrieve('https://raw.githubusercontent.com/crinkies/Pykonnekt/master/icon.ico', f'{path}icon.ico')
        except:
            pass
        host_file = open(f"{path}Network.txt", "a+")
        network_profiles = subprocess.check_output("Netsh wlan show profiles", shell=True).decode('ascii')
        host_file.write(f"Your network name goes here. One line.\nHere's your network information:\n{network_profiles}")
        host_file.close()
        time.sleep(1)
        m_body = f"Network.txt created at {path}.\nPlease enter your network name into the file and reload the app."
        notif(m_body)
        os.startfile(f"{path}Network.txt")


def new_thread(thread):
    x = threading.Thread(target=thread)
    x.start()

def add_disconnect():
    m_body = "Your internet has been disconnected.\nReconnecting..."
    notif(m_body)
    global reconnects
    reconnects+=1

def check_connection(network):
    while not quitProcess:
        url = random.choice(url_list)
        try:
            subprocess.check_output(f"ping {url} -n 2", shell=True)
        except:
            try:
                add_disconnect()
                subprocess.check_output(f"netsh wlan connect name={network}", shell=True)
                time.sleep(.3)
            except:
                m_body = "Reconnection was unsuccessful.\nReattempting in 10s...\nPress Ctrl+Shift+Z to exit."
                notif(m_body)
                global reconnects
                reconnects-=1
                time.sleep(10)

def key_listen():
    while not quitProcess:
        time.sleep(.3)
        if keyboard.is_pressed('ctrl+shift+z'):
            quit_threading()
        elif keyboard.is_pressed('ctrl+shift+x'):
            m_body = f"There have been a total of {reconnects} reconnects during your session."
            notif(m_body)
            while keyboard.is_pressed('ctrl+shift+x'):
                pass
        else:
            pass

def notif(m_body):
    n.notify(title='Pykonnekt',message=m_body,app_icon=f'{path}icon.ico')

def quit_threading():
    global quitProcess
    quitProcess = True
    m_body = f"Thanks for using Pykonnekt.\nThere were {reconnects} reconnects during your session."
    notif(m_body)
    raise SystemExit

main()
