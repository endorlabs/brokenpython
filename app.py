import yaml

def process_config(file_path="config.yaml"):
    """Load YAML configuration (vulnerable to RCE via yaml.load on untrusted input)."""
    with open(file_path, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)  
    print("Message from config:", config.get("message", "<no message>"))
    return config

if __name__ == "__main__":
    process_config("config.yaml")
