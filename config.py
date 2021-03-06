"""
    Configuration files. Please double check all the informations for the
    project to run correctly.
    The included CA certificate is for `Amazon Root CA 1`, and it's being used
    for *.infura.io RPC node. Omit it if your node is not using https, or
    change it with the one of your CA.
"""

# Network configuration

WIFI_SSID = 'F For Family'
WIFI_PASSWORD = 'drabdullatif197116'

# WIFI_SSID = 'mizanonik'
# WIFI_PASSWORD = '12345678i'


# Ethereum configuration

RPC_URL = 'https://rinkeby.infura.io/v3/85f9c5b1f7144773b43e93705d6bdd7f'

ADDRESS = '0x314843b951748AF9cEFC5B28Afc0FC4ef3FCDA1e'
PRIVATE_KEY = '0x963FF0710F9264DA329C452549AACC849515AAB10B024F0F64687AF2D9D7DAC0' # Note the '0x' prefix - it must be used

BET_AMOUNT = 50 # The Wei amount to be used as a bet

WEI_AMOUNT = 10


#CONTRACT_ADDRESS = '0x35bfe0dB519b8Ac55621c29c34B0Fc3F6675312a'
CONTRACT_ADDRESS = '0x0D6b8DddcfB82C63a276E320beAd41AdF5134bA3'

#Methods interface
#Name, arguments types, and gas limit must be specified.
CONTRACT_METHODS = {
    "getLEDOneStatus": {
        "args": (),
        "gas_limit": "0x6691b7"
    },
    "getLEDTwoStatus": {
        "args": (),
        "gas_limit": "0x6691b7"
    },
    "setCurrentFromDevice": {
        "args": ("int256",),
        "gas_limit": "0x6691b7"
    }
}

GAS_PRICE = "0x174876e800"

CA_CERT = """-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv
b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj
ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM
9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw
IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6
VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L
93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm
jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC
AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA
A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI
U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs
N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv
o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU
5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy
rqXRfboQnoZsG4q5WTP468SQvvG5
-----END CERTIFICATE-----
\x00"""