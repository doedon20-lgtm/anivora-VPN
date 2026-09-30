import secrets


class WireGuardManager:

    def __init__(self):

        self.server_public_key = (
            self._generate_placeholder_key()
        )

        self.interface = "anivora0"

    def _generate_placeholder_key(self):

        return secrets.token_urlsafe(32)

    def status(self):

        return {
            "provider": "WireGuard",
            "interface": self.interface,
            "configured": False,
            "message": (
                "WireGuard server integration "
                "has not been connected yet."
            )
        }

    def generate_peer_id(self):

        return (
            "peer_"
            + secrets.token_hex(8)
        )


wireguard_manager = WireGuardManager()
