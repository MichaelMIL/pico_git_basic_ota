

def connectToWifiAndUpdate():
    import time, machine, network, gc, confs.secrets as secrets
    time.sleep(1)
    print('Memory free', gc.mem_free())

    from lib.ota_updater import OTAUpdater

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    otaUpdater = OTAUpdater('https://github.com/MichaelMIL/pico_git_basic_ota', main_dir='app', secrets_file="secrets.py")
    hasUpdated = otaUpdater.install_update_if_available()
    if hasUpdated:
        machine.reset()
    else:
        del(otaUpdater)
        sta_if.disconnect()
        del(sta_if)
        gc.collect()

def startApp():
    import program


connectToWifiAndUpdate()
startApp()