import os
from app import process_config

benign_yaml = 'message: "Hello, world!"'
with open("config.yaml", "w") as f:
    f.write(benign_yaml)

print("[*] Testing app with benign config...")
result = process_config("config.yaml")
assert result.get("message") == "Hello, world!", "Config message mismatch!"
print("[*] Application functionality is OK. Loaded message:", result.get("message"))

os.remove("config.yaml")
