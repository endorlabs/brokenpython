# PyYAML Security Issue  

## The Task

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

## What You Don’t Have  

- **Any real context on why this matters.**  
- **Any clear instructions on what will break.**  

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