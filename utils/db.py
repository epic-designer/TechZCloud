from pymongo import MongoClient
print("Connecting to database...")
client = MongoClient(
    "mongodb+srv://kiraPersonalDB:KiraDB2023@cluster0.qm8bgzb.mongodb.net/"
)

db = client["techzcloud"]
filesdb = db["files"]
print("Connected to database...")

def save_file_in_db(filename, hash, msg_id=None):
    filesdb.update_one(
        {
            "hash": hash,
        },
        {"$set": {"filename": filename, "msg_id": msg_id}},
        upsert=True,
    )


def is_hash_in_db(hash):
    data = filesdb.find_one({"hash": hash})
    if data:
        return data
    else:
        return None
