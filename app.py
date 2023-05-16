"""
A Flask web application that allows users to select a predefined template and fill in the
fields to generate formatted output.
"""

from flask import Flask, render_template, request


class Template:
    """
    A class representing a template with a title, fields, and format string for
    generating output.
    """

    def __init__(self, title, fields, format_string):
        self.title = title
        self.fields = fields
        self.format_string = format_string

    def get_title(self):
        """
        Returns the title of the template.
        """
        return self.title


# Define our templates
templates = [
    Template(
        "Web Development Coding Assistant",
        ['JavaScript', 'CSS', 'HTML'],
        """
    The purpose of this template is to assist you in writing clean, efficient, and maintainable web development code. Each section will guide you through the process of creating JavaScript, CSS, and HTML code respectively.

    1. JavaScript: {}
        - Aim for simple, clean functions.
        - Make sure your variables and functions are named in a way that makes their purpose clear.
        - Don't forget to comment your code, explaining the what, why, and how.

    2. CSS: {}
        - Group similar styles together and comment each section.
        - Use classes and IDs effectively and avoid over-specifying.
        - Make sure your CSS is maintainable and scalable, considering the use of CSS preprocessors if necessary.

    3. HTML: {}
        - Make your HTML semantic, using the right tags for the right purpose.
        - Keep your code clean and organized. Make sure indentation and spacing is consistent.
        - Don't forget to include necessary meta tags and consider accessibility as you code.
    """
    ),
    Template(
        "Lint Report",
        ['File Code', 'Pylint Output'],
        """I want you to help me lint the following file:

{}
        
Attached is its `pylint` output:

{}

Please prepare a list of your proposed changes to resolve each entry. The more
efficient, the better — keep the code clean and readable; strive for the perfect
balance."""
    ),
    # Add more templates here
]

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    The home route that handles both GET and POST requests.
    If it's a POST request, it processes the submitted form data and returns the
    output based on the selected template.
    If it's a GET request, it renders the input form for the user.
    """
    if request.method == 'POST':
        template_index = int(request.form.get('template_index', 0))
        template = templates[template_index]
        field_values = [request.form.get(field, "")
                        for field in template.fields]
        return render_template('output.html', output=template.format_string.format(*field_values))

    return render_template('input.html', templates=templates)


if __name__ == '__main__':
    app.run(debug=True)
