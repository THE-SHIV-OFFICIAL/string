from motor.motor_asyncio import AsyncIOMotorClient
import logging

class Database:
    def __init__(self, uri, database_name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        logging.info("MongoDB Connected Successfully!")

    async def is_user_exist(self, user_id):
        """Checks if a user is already in the database."""
        user = await self.col.find_one({'_id': user_id})
        return bool(user)

    async def add_user(self, user_id, first_name):
        """Adds a new user to the database."""
        if not await self.is_user_exist(user_id):
            user_data = {
                '_id': user_id,
                'first_name': first_name
            }
            await self.col.insert_one(user_data)
            return True # Returns True if it's a new user
        return False # Returns False if they already exist
