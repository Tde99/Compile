```
   ____ ___  __  __ ____ ___ _     _____ 
  / ___/ _ \|  \/  |  _ \_ _| |   | ____|
 | |  | | | | |\/| | |_) | | | |   |  _|  
 | |__| |_| | |  | |  __/| | | |___| |___ 
  \____\___/|_|  |_|_|  |___|_____|_____|
```
PYTHON-COMPILE-TOOL
A straightforward Python utility designed to compile source code into 
Python Bytecode (.pyc). This tool provides a simple interface to help 
developers and security researchers obscure their source code, preventing 
direct reading of logic and sensitive strings by casual users.

**Features**
* **Bytecode Generation:** Compiles standard `.py` files into optimized `.pyc` files.
* **Basic Obfuscation:** Helps hide the source code structure from non-technical viewers.
* **Batch-Ready Loop:** Keep compiling multiple files without restarting the program.
* **Visual Interface:** Integrated 'figlet' header for a clean terminal experience.

**Prerequisites**
The following environment is required for the script to function:
* Python 3.x
* Py_compile library (Standard Python Library).
* Figlet: (The script attempts to install this automatically via apt).

**Installation**

Clone the repository:
   * git clone https://github.com/Tde99/Python-Compiler.git

Navigate to the directory:
   * cd Python-Compiler

Make the script executable:
   * chmod +x compile_tool.py

**Usage**
To ensure the script can install dependencies and write to system directories if needed, run with sudo:

sudo python3 compile_tool.py

**How it works:**
1. **Input:** Type the name of your Python file (e.g., `my_script.py`).
2. **Processing:** The script uses the `py_compile` engine to parse the code.
3. **Output:** A new compiled file is generated, usually within a `__pycache__` directory.


**Important Notes:**
* **Not Full Encryption:** Note that bytecode can be decompiled using tools like `uncompyle6`. For higher security, consider using "PyArmor" or "Cython".
* **Python Version:** Compiled `.pyc` files are usually specific to the Python version used during compilation (e.g., Python 3.10 bytecode might not run on 3.8).
* **Automated Setup:** The script handles the `figlet` installation on the first run.
