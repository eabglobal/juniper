import bcrypt


def lambda_handler(event, context):
    password = b"super secret password"
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    # Check that an unhashed password matches one that has previously been
    # hashed
    if bcrypt.checkpw(password, hashed):
        return {"value": "It Matches!"}

    return {"value": "It Does not Match :("}
