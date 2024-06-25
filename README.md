# XSD to JSON Schema Converter

A simple Python script to convert XSD files into JSON Schema format, making data validation easy and efficient.

## Prerequisites

- Python: Ensure Python is installed on your system. If not, follow the installation steps below.
- pip: Ensure pip is installed and upgraded.
- lxml: A third-party package that needs to be installed separately.


## Installing Python

1. Download Python:
   - Go to the official Python website (https://www.python.org/downloads/).
   - Download the latest version of Python for your operating system.

2. Install Python:
   - Run the downloaded installer.
   - **Important**: Check the box that says "Add Python to PATH" before clicking "Install Now".
   - Follow the prompts to complete the installation.


## Setting Up the Environment

1. Open a command prompt or terminal:
   - On Windows: Press `Win + R`, type `cmd`, and hit Enter.
   - On MacOS: Open `Terminal` from your Applications/Utilities folder.
   - On Linux: Open your preferred terminal application.

2. Verify Python installation:
   ```python --version```

3. Verify pip installation:
   ```pip --version```
   
   If pip is not installed or you need to upgrade it, run the following command:
   ```python -m ensurepip --upgrade```
   
   Or you can manually install pip with:
   ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
   ```python get-pip.py```

4. Install lxml:
   ```pip install lxml```


## Cloning the Repository

1. Navigate to your desired directory, and clone the repository:
   ```git clone https://github.com/dianosaur12/xsd2jsonschema.git```

2. Navigate to the repository on your system:
   ```cd xsd2jsonschema```

3. To run the script, use the following command:
   ```python xsd2jsonschema.py path/to/your/xsdfile.xsd```
  
   Make sure to replace `path/to/your/xsdfile.xsd` with the actual path to your XSD file.






