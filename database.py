from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI

# Connect to MongoDB and set the database name to "StringGenBot"
client = AsyncIOMotorClient(MONGO_DB_URI)
db = client["StringGenBot"]
users_col = db["users"]

async def add_served_user(user_id: int):
    """Adds a user to the database if they don't already exist."""
    is_served = await users_col.find_one({"_id": user_id})
    if not is_served:
        await users_col.insert_one({"_id": user_id})
        return True
    return False

async def get_served_users() -> list:
    """Returns a list of all users in the database."""
    users_list = []
    async for user in users_col.find({"_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list
