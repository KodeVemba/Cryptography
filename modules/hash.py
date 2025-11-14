import hashlib

# text = "Hello Kiami"
# hash_object = hashlib.sha256(text.encode())
# hash_digest = hash_object.hexdigest()
# print(f"The sha of the {text} is {hash_digest}")


def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(1024)

            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest


def verify_integrity(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    print(f"checking integrity between {file1} and {file2}")


if __name__ == "__main__":
    print
