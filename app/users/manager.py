import secrets
from datetime import datetime, timezone


class UserManager:

    def __init__(self):

        self.users = {}

    def create_user(
        self,
        name: str
    ):

        user_id = (
            "user_"
            + secrets.token_hex(8)
        )

        user = {
            "id": user_id,
            "name": name,
            "status": "active",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.users[user_id] = user

        return user

    def list_users(self):

        return list(
            self.users.values()
        )

    def get_user(self, user_id):

        return self.users.get(
            user_id
        )

    def delete_user(self, user_id):

        if user_id not in self.users:
            return False

        del self.users[user_id]

        return True


user_manager = UserManager()
