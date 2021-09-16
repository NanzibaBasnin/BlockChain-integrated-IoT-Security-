import streams

# Ethereum modules
from blockchain.ethereum import ethereum
from blockchain.ethereum import rpc

# WiFi drivers
from espressif.esp32net import esp32wifi as net_driver # for ESP-8266
# from broadcom.bcm43362 import bcm43362 as net_driver # for Particle Photon
from wireless import wifi

# SSL module for https
import ssl

#to read from analogue sensosr
import adc

# Configuration file
import config

import math
import json
import requests

# import Real-Time Clock module
import rtc

def get_epoch():
    user_agent = {"user-agent": "curl/7.56.0"}
    return int(json.loads(requests.get("http://now.zerynth.com/", headers=user_agent).content)['now']['epoch'])



# The SSL context is needed to validate https certificates
SSL_CTX = ssl.create_ssl_context(
    cacert=config.CA_CERT,
    options=ssl.CERT_REQUIRED|ssl.SERVER_AUTH
)

inputAnalog = A0
tempC = 0
ledOutput = D12

mVerAmp = 66;
volt = 0;
vrms = 0;
ampsrms = 0;
result = 0.0;



# Use serial monitor
streams.serial()


def init_wifi():
    # Connect to WiFi network
    net_driver.auto_init()
    print("Connecting to wifi")
    wifi.link(config.WIFI_SSID, wifi.WIFI_WPA2, config.WIFI_PASSWORD)
    print("Connected!")


def print_balance():
    # Get our current balance from the net
    balance = eth.getBalance(config.ADDRESS)
    print("Current balance: ", balance)
    if not balance:
        print(eth.last_error)
        raise Exception
        

def get_vpp():
    print("in vpp")
    readValue = 0
    maxValue = 0
    minValue = 1024
    print("reached here")
    
    timestamp = get_epoch()
    rtc.set_utc(timestamp)
    print("here i am")
    tm = rtc.get_utc(1)
    print(tm)
    start_time = int(tm[0] * 1000)
    
    while (((int(tm[0] * 1000)) - start_time) <1000):
        readValue = adc.read(inputAnalog)
        if(readValue>maxValue):
            maxValue = readValue
        if(readValue < minValue):
            minValue = readValue
    global result
    result = (((maxValue-minValue)*5.0) /1024.0)
    print("Result: ")
    print(result)
     


def get_current():
    global volt
    volt = result
    print("Volt: ")
    print(volt)
    global vrms
    vrms = (volt/2.0) * 0.707
    print("VRMS: ")
    print(vrms)
    global ampsrms
    ampsrms = (vrms*1000)/ampsrms;
    print("ampsrms: ")
    print(ampsrms)


# Main
try:
    init_wifi()
    pinMode(ledOutput, OUTPUT)
    
    # Init the RPC node
    eth = rpc.RPC(config.RPC_URL, ssl_ctx=SSL_CTX)

    # Init smart contract object
    tempAndLED = ethereum.Contract(
        eth,
        config.CONTRACT_ADDRESS,
        config.PRIVATE_KEY,
        config.ADDRESS,
        chain=ethereum.RINKEBY
    )
    
    for name in config.CONTRACT_METHODS:
        method = config.CONTRACT_METHODS[name]
        tempAndLED.register_function(
            name,
            config.GAS_PRICE,
            method["gas_limit"],
            method["args"]
        )
   
    print_balance()


except Exception as e:
    print(e)

while True:
    print(eth.getGasPrice())
    # ledOneStatus = tempAndLED.call('getLEDOneStatus', rv=(256, int))
    # ledTwoStatus = tempAndLED.call('getLEDTwoStatus', rv=(256, int))
    # if ledOneStatus is not None:
    #     if ledOneStatus >= 1:
    #         print("LED ON")
    #         digitalWrite(D12, HIGH)  # turn the LED ON by setting the voltage HIGH
    #     else:
    #         print("LED OFF")
    #         digitalWrite(D12, LOW)
            
    # if ledTwoStatus is not None:
    #     if ledTwoStatus >= 1:
    #         print("LED ON")
    #         digitalWrite(D13, HIGH)  # turn the LED ON by setting the voltage HIGH
    #     else:
    #         print("LED OFF")
    #         digitalWrite(D13, LOW)
    
    get_vpp()
    get_current()
    print('Current...')
    nonce = eth.getTransactionCount(config.ADDRESS)
    tx_hash = tempAndLED.tx('setCurrentFromDevice', nonce, value=None, args=(30,))
    sleep(50000)