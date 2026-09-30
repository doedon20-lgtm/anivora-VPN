import os


class Config:

    APP_NAME = "AniVora VPN"

    VERSION = "0.1.0"

    HOST = os.getenv(
        "ANIVORA_VPN_HOST",
        "0.0.0.0"
    )

    PORT = int(
        os.getenv(
            "ANIVORA_VPN_PORT",
            "8200"
        )
    )

    DATA_DIR = os.getenv(
        "ANIVORA_VPN_DATA",
        "data"
    )

    VPN_NETWORK = os.getenv(
        "ANIVORA_VPN_NETWORK",
        "10.80.0.0/24"
  )
