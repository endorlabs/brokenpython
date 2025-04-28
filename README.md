# PyYAML Security Issue  

## The Task: Update some legacy code

- **CVE-2017-18342** affects PyYAML.
- Your application is using a vulnerable version of **PyYAML**.
- Security is telling you **to upgrade PyYAML**.
- **After upgrading, your app is broken.**
- **Fix it.**  

- Your application has **a CVE**.  
- Security is telling you **to upgrade PyYAML**.  
- **After upgrading, your app is broken.**  
- **Fix it.**  

## What You Have  

- `app.py` – Your YAML loader.  
- `exploit.py` – A proof-of-concept exploit.  
- **A security advisory telling you to upgrade.**  


## What your team is telling you?

- The code requires Python 3.8.

   ```bash
   sudo apt install python3.8 python3.8-venv -y
   ```
- You probably need to actually setup Python 3.8 by connecting to a personal package archive for python 3.8 because that was released before COVID and you know software happens quick.

   ```bash
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt update
   ```

- Do it in a virtual environment or you're gonna have a bad time.

    ```bash
    python3.8 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py
    ```

- You can check if the application is functioning properly by using the `/heatlh` route.

   ```bash
   curl http://127.0.0.1:5000/health
   ```

## What You Don’t Have  

- **Any real context on why this matters.**  
- **Any clear instructions on how much effort this will be**  

## What You Need to Do  

1. **Install the old PyYAML version.**  
2. **Run the app and confirm it works.**  
3. **Run the exploit to confirm vulnerability.**  
4. **Upgrade PyYAML.**  
5. **Watch it break.**  
6. **Figure out why it broke.**  
7. **Fix it.**  

### **Once You’re Done**  

Ask yourself:  

- **Did this feel easy or annoying?**  
- **Would you prioritize this fix if security just said "Upgrade PyYAML" with no details?**  
- **What would make this easier for developers?**  

This is what developers deal with every day. Security teams need to **see the friction** before they demand fixes.

# Scan for Vulnerabilities

We'll use `endorctl` to scan the project for known vulnerabilities.

### Step-by-step:

1. **Initialize Endor Labs**  
   Run the following command to authenticate with Endor Labs and set up your environment:
   ```bash
   ./endorctl init --auth-mode <mode> --headless-mode
   ```
   Replace `<mode>` with your preferred authentication mode (e.g., `google`, `github`, etc.).

2. **Authenticate via Portal**  
   The command will output a URL. You can command-click (⌘+click) the link in your terminal to open the authentication portal.  
   Log in and copy the generated token.

3. **Complete Setup**  
   Paste the token back into your terminal.  
   You'll then be prompted to select a tenant—choose the one you just created.

4. **Run the Vulnerability Scan**  
   Once authenticated and configured, scan your codebase:
   ```bash
   ./endorctl scan
   ```
   This will analyze your project for security vulnerabilities.

# Give up or wanna cheat?

Navigate to the solution folder and find `solution.md` for step by step instructions. 
