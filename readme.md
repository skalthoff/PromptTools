# PromptTools

PromptTools is a Flask web application that allows users to select a predefined template, fill in the fields to generate formatted output. This can be used in various scenarios where a structured output is required based on user input.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/skalthoff/PromptTools.git
   ```

2. Navigate to the cloned repository:
   ```
   cd PromptTools
   ```

3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Start the application by running:

```
python app.py
```

Open your web browser and navigate to `http://localhost:5000` to see the application in action.

## Usage

1. Select a template from the dropdown menu.
2. Fill in the fields corresponding to the selected template.
3. Click "Submit" to generate the output.
4. You can now copy the output text and use it as you need.

## Contributing

Contributions are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```

You may need to create a `requirements.txt` file containing the packages your project needs (like `flask`) and a `LICENSE.md` file if you want to specify a license. The above guide assumes that you have these files in your repository.