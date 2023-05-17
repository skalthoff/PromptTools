# PromptTools

PromptTools is a Flask web application that allows users to select a predefined template and fill in the fields to generate formatted output. This tool is helpful in generating text according to predefined templates.

## Installation and Setup

Follow the below instructions to install and setup this project on your local machine:

1. Clone the repository from GitHub.

```bash
git clone https://github.com/skalthoff/PromptTools.git
```

2. Navigate to the project directory.

```bash
cd PromptTools
```

3. Create a virtual environment.

```bash
python3.10 -m venv venv
```

4. Activate the virtual environment.

On Windows:

```bash
venv\Scripts\activate
```

On Unix or MacOS:

```bash
source venv/bin/activate
```

5. Install the required packages.

```bash
pip install -r requirements.txt
```

## Running the Application

You can run the application with the following command:

```bash
python app.py
```

Once the server is running, open a web browser and navigate to `http://localhost:5000` to use the application.

## Adding New Templates

New templates can be added by modifying the `app.py` file. Templates are defined as instances of the `Template` class, which takes a title, a list of fields, and a format string as arguments. The format string should include placeholders (in `{}` brackets) for each field.

Once a new template is added to the `templates` list in `app.py`, it will automatically be available in the application.

## License

This project is licensed under the terms of the MIT license.
```

Please replace `"MIT license"` with the actual license of your project, if it's not MIT. This README includes instructions for cloning the repository, setting up a virtual environment with Python 3.10, installing the required packages, running the application, and adding new templates.