# Template Tool

This is a simple Flask application that allows users to select from a set of predefined templates, fill in their content, and generate formatted text output. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project requires Python 3.10 and Conda. 

### Installation

1. Clone this repository:
    ```
    git clone https://github.com/<your_username>/template_tool.git
    ```
    Replace `<your_username>` with your GitHub username.

2. Navigate to the project directory:
    ```
    cd template_tool
    ```

3. Create a new Conda environment:
    ```
    conda create --name template_tool python=3.10
    ```

4. Activate the Conda environment:
    ```
    conda activate template_tool
    ```

5. Install Flask:
    ```
    pip install flask
    ```

## Usage

To start the application, simply run:
```
python app.py
```

Then, open your web browser and go to `http://localhost:5000`. You will see a form with a dropdown menu to select a template and text boxes to fill in the template's fields. 

After submitting the form, you will see the generated output based on your input. You can copy this output and use it as needed.

## Adding More Templates

To add more templates, modify the `templates` list in `app.py`. For each template, you need to specify a title, a list of field names, and a format string. The format string should contain one `{}` placeholder for each field.

Here is an example of how to define a template:

```python
Template(
    "Template Title",
    ['Field 1', 'Field 2', 'Field 3'],
    "This is the format string with placeholders for {}, {}, and {}."
)
```