from app.esp_8266_wifi import Wifi

def connectToWifiAndUpdate():
    import time, machine, network, gc, app.secrets as secrets
    time.sleep(1)
    print('Memory fr ee', gc.mem_free())

    from app.ota_updater import OTAUpdater

    wifi = Wifi()
    wifi.power_on_and_connect()
    print('wifi status:', wifi.get_status())
    print('is connected:', wifi.is_connected())
    if wifi.is_connected():
        otaUpdater = OTAUpdater('https://github.com/MichaelMIL/pico_git_basic_ota', main_dir='app', secrets_file="secrets.py")
        hasUpdated = otaUpdater.install_update_if_available()
        if hasUpdated:
            machine.reset()
        else:
            del(wifi)
            del(otaUpdater)
            gc.collect()
            

def startApp():
    import app.start


connectToWifiAndUpdate()
startApp()