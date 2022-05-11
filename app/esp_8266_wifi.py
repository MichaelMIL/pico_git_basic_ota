import network , app.secrets as secrets

class Wifi:
    def __init__(self) -> None:
        self.wifi_module = network.WLAN(network.STA_IF)

    def power_on(self) -> None:
        self.wifi_module.active(True)
    def power_off(self) -> None:
        self.wifi_module.active(False)
    def connect(self, ssid: str = secrets.WIFI_SSID, password: str = secrets.WIFI_PASSWORD) -> None:
        self.wifi_module.connect(ssid, password)
        while not self.wifi_module.isconnected():
            pass
    def disconnect(self) -> None:
        self.wifi_module.disconnect()
    def is_connected(self) -> bool:
        return self.wifi_module.isconnected()
    def get_ip(self) -> str:
        return self.wifi_module.ifconfig()[0]
    def get_ssid(self) -> str:
        return self.wifi_module.config('essid')
    def get_password(self) -> str: 
        return self.wifi_module.config('password')
    def get_mac(self) -> str:
        return self.wifi_module.config('mac')
    def get_rssi(self) -> int:
        return self.wifi_module.status('rssi')
    def get_status(self) -> str:
        return self.wifi_module.status()

    def power_on_and_connect(self, ssid: str = secrets.WIFI_SSID, password: str = secrets.WIFI_PASSWORD) -> None:
        self.power_on()
        self.connect(ssid, password)
        print('network config:', self.get_ip())
    def __del__(self) -> None:
        print('Wifi destructor')
        self.power_off()