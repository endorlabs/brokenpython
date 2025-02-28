# PyYAML Security Vulnerability Solution Guide

## Overview

This document provides a step-by-step guide to identifying and fixing a security vulnerability in PyYAML, specifically **CVE-2017-18342**. This vulnerability allows arbitrary code execution when `yaml.load()` is used without specifying a `Loader`, making it possible for attackers to execute malicious code through specially crafted YAML input.

To resolve this issue, you will:

1. **Install the vulnerable version of PyYAML** and observe the application's behavior.
2. **Upgrade PyYAML** to a secure version and note the resulting issue.
3. **Modify the application code** to be compatible with the updated PyYAML version while mitigating arbitrary code execution risks.

---

## Step 1: Set Up the Environment

1. **Ensure you're using Python 3.8** (since older PyYAML versions may not work with newer Python versions):

   ```bash
   python3 --version
   ```

   If your version is newer than 3.8, install and use Python 3.8:

   ```bash
   sudo apt install python3.8 python3.8-venv -y
   ```
   You probably need to actually setup Python 3.8 by connecting to a personal package archieve. 

   ```bash
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt update
   ```
2. **Clone the Repository**:

   You don't need to do this if you are in CodeSpaces.

   ```bash
   git clone https://github.com/endorlabs/brokenpython.git
   cd brokenpython
   ```

3. **Create and Activate a Virtual Environment**:

   ```bash
   python3.8 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Verify Installed Python Version in the Virtual Environment**:

   ```bash
   python --version
   ```

5. **Ensure Required Dependencies are Installed**:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` specifies `PyYAML==3.13`, a version vulnerable to CVE-2017-18342.

---

## Step 2: Run the Application with the Vulnerable PyYAML Version

1. **Start the Flask Application**:

   ```bash
   python app.py
   ```

   The application should be running at `http://127.0.0.1:5000/`.

2. **Test the Application**: Open a browser and navigate to `http://127.0.0.1:5000/`. You should see the application's interface.

3. **Run the Exploit Script**: In a new terminal (with the virtual environment activated), execute:

   ```bash
   python exploit.py
   ```

   **Expected Output**:

   ```html
   <h3>Parsed Data:</h3><pre>0</pre>
   ```

   This confirms that the application is vulnerable to arbitrary code execution through untrusted YAML input.

---

## Step 3: Upgrade PyYAML to a Secure Version

1. **Check Installed PyYAML Version Before Upgrade**:

   ```bash
   pip list | grep PyYAML
   ```

2. **Upgrade PyYAML**:

   ```bash
   pip install --upgrade PyYAML
   ```

   This will upgrade PyYAML to the latest version (e.g., 6.0.2).

3. **Verify the Upgrade**:

   ```bash
   pip show PyYAML
   ```

   Ensure the version is 5.1 or higher.

---

## Step 4: Observe the Breaking Change

1. **Restart the Application**:
   ```bash
   python app.py
   ```
   **Expected Error**:
   ```plaintext
   TypeError: load() missing 1 required positional argument: 'Loader'
   ```
   This error occurs because, starting from PyYAML 5.1, the `yaml.load()` function requires an explicit `Loader` argument for security reasons.

---

## Step 5: Fix the Application Code

1. **Modify **``: Open `app.py` and locate the line:

   ```python
   parsed_data = yaml.load(yaml_input)  # This will break after upgrading
   ```

   Replace it with:

   ```python
   parsed_data = yaml.safe_load(yaml_input)  # Safe and works with PyYAML 5.1+
   ```

   The `safe_load` function prevents execution of arbitrary code and is compatible with newer PyYAML versions.

2. **Save the Changes**.

---

## Step 6: Verify the Fix

1. **Restart the Application**:

   ```bash
   python app.py
   ```

   The application should now run without errors.

2. **Test the Application**: Navigate to `http://127.0.0.1:5000/` to ensure it's functioning correctly.

3. **Run the Exploit Script Again**: In the terminal, execute:

   ```bash
   python exploit.py
   ```

   **Expected Output**:

   ```html
   <h3>Error:</h3><pre>yaml.constructor.ConstructorError: could not determine a constructor for the tag '!!python/object/apply:os.system'</pre>
   ```

   This indicates that the exploit is no longer successful, and the vulnerability has been mitigated.

4. **Run the Health Check Endpoint**:

   ```bash
   curl http://127.0.0.1:5000/health
   ```

   If the fix is applied correctly, you should see a successful response.

---

## Summary

By following these steps, you've:

- **Identified** the security vulnerability caused by using `yaml.load()` without a `Loader`.
- **Upgraded** the vulnerable dependency to a secure version.
- **Modified** the application code to use `yaml.safe_load()`, mitigating the arbitrary code execution risk.
- **Verified** that the application is functioning correctly and is no longer vulnerable to CVE-2017-18342.

This exercise highlights the importance of understanding how security patches can introduce breaking changes and the necessity of adapting application code accordingly.
