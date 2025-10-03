import hashlib

def generate_hash(text, algorithm="sha256"):
    if algorithm=="md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm=="sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    else:
        return hashlib.sha256(text.encode()).hexdigest()

if __name__ == "__main__":
    msg=input("Enter text to hash: ")
    algo=input("Choose algorithm (md5/sha1/sha256): ")
    print(f"Hash ({algo}):", generate_hash(msg, algo))
