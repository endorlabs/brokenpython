# PyYAML Security Vulnerability – Full Solution

## Overview

You've been given a security advisory about **CVE-2020-14343** affecting PyYAML. Your task is to upgrade the package, but when you do, the application **breaks**. Now, you need to figure out why and fix it.

This document walks you through what went wrong, why it happened, and how to resolve it with **minimal effort**.

---

## Step 1: Confirm the Vulnerability

Run the application as-is and confirm that everything is working:

```sh
python app.py
```

✔️ Expected output:
```
Message from config: Hello, world!
```

Now, attempt to exploit the vulnerability:

```sh
python exploit.py
```

❌ Expected output (if vulnerable):
```
[*] Running exploit: loading malicious YAML...
[!] Exploit successful: 'pwned.txt' was created by malicious YAML!
```

This confirms that the application is **vulnerable to RCE**.

---

## Step 2: Upgrade PyYAML

You’ve been told to upgrade PyYAML. Do that now:

```sh
pip install --upgrade pyyaml
```

Verify the installed version:

```sh
pip freeze | grep pyyaml
```

✔️ Expected output:
```
pyyaml==5.4
```

Now, run the application again:

```sh
python app.py
```

❌ Expected error:
```
TypeError: load() missing 1 required positional argument: 'Loader'
```

This means the upgrade introduced a **breaking change**.

---

## Step 3: Fix the Application

Now, update the code in `app.py`. Locate the following line:

```python
config = yaml.load(f, Loader=yaml.FullLoader)  # Old and vulnerable
```

Change it to:

```python
config = yaml.safe_load(f)  # Secure and compatible with PyYAML 5.4+
```

This is the **trivial fix** required to make the application work again while ensuring it is no longer vulnerable to arbitrary code execution.

---

## Step 4: Verify the Fix

Run the application again:

```sh
python app.py
```

✔️ Expected output:
```
Message from config: Hello, world!
```

Now, try running the exploit again:

```sh
python exploit.py
```

✔️ Expected output:
```
[*] Running exploit: loading malicious YAML...
yaml.constructor.ConstructorError: could not determine a constructor for the tag
[!] Exploit failed or mitigated: 'pwned.txt' not found.
```

This confirms that the **security issue is fixed** and the exploit no longer works.

---

## What You Learned

- Security updates can introduce **breaking changes**, even if the fix is trivial.
- Developers may resist upgrading because **it interrupts their workflow**.
- Fixing security issues isn’t just about patching; **it’s about understanding what breaks and why**.

Now, you’ve seen both sides—why security teams push for updates and why developers hesitate. 

In this case, the fix was one line. In a real-world project, it could be much worse. Think about how you’d approach security updates in a production environment. 

---

## References

- [CVE-2020-14343 - PyYAML Unsafe Deserialization](https://nvd.nist.gov/vuln/detail/CVE-2020-14343)
- [PyYAML 5.4 Breaking Change - Official Docs](https://github.com/yaml/pyyaml/blob/master/CHANGES)
