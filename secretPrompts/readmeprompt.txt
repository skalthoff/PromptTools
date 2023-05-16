write a readme.md file for this project:

app.py:
```
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
        return self.title


# Define our templates
templates = [
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
        field_values = [request.form.get(field, "") for field in template.fields]
        return render_template('output.html', output=template.format_string.format(*field_values))

    return render_template('input.html', templates=templates)


if __name__ == '__main__':
    app.run(debug=True)
```

templates/input.html:
```
<!DOCTYPE html>
<html>
<head>
    <title>Template Tool</title>
</head>
<body>
    <form method="POST">
        <label for="template_index">Template:</label><br>
        <select id="template_index" name="template_index">
            {% set count = 0 %}
            {% for template in templates %}
                <option value="{{ count }}">{{ template.title }}</option>
                {% set count = count + 1 %}
            {% endfor %}
        </select><br>
        {% set count = 0 %}
        {% for template in templates %}
            <div id="fields_{{ count }}" {% if not count == 0 %}style="display: none"{% endif %}>
                {% for field in template.fields %}
                    <label for="{{ field }}">{{ field }}:</label><br>
                    <textarea id="{{ field }}" name="{{ field }}" rows="10" cols="50"></textarea><br>
                {% endfor %}
            </div>
            {% set count = count + 1 %}
        {% endfor %}
        <input type="submit" value="Submit">
    </form>
    <script>
        document.getElementById('template_index').addEventListener('change', function() {
            var divs = document.querySelectorAll('[id^="fields_"]');
            for (var i = 0; i < divs.length; i++) {
                divs[i].style.display = 'none';
            }
            document.getElementById('fields_' + this.value).style.display = 'block';
        });
    </script>
</body>
</html>
```
output.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Template Tool</title>
</head>
<body>
    <pre>{{ output }}</pre>
</body>
</html>
```