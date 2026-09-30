from datetime import datetime, timezone

from app.vpn.wireguard import (
    wireguard_manager
)


class VPNManager:

    def __init__(self):

        self.peers = {}

    def create_peer(
        self,
        user_id: str,
        name: str
    ):

        peer_id = (
            wireguard_manager
            .generate_peer_id()
        )

        peer = {
            "id": peer_id,
            "user_id": user_id,
            "name": name,
            "status": "inactive",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.peers[peer_id] = peer

        return peer

    def list_peers(self):

        return list(
            self.peers.values()
        )

    def get_peer(self, peer_id):

        return self.peers.get(
            peer_id
        )

    def connect_peer(self, peer_id):

        peer = self.get_peer(
            peer_id
        )

        if not peer:
            return None

        peer["status"] = "connected"

        return peer

    def disconnect_peer(self, peer_id):

        peer = self.get_peer(
            peer_id
        )

        if not peer:
            return None

        peer["status"] = "inactive"

        return peer

    def delete_peer(self, peer_id):

        if peer_id not in self.peers:
            return False

        del self.peers[peer_id]

        return True


vpn_manager = VPNManager()
