# Spring 2025 CNAD Assignment 2

# Math Operations CLI Application

A simple command-line interface (CLI) application that performs various mathematical operations.

## Features

- Addition of two numbers
- Factorial calculation
- Odd/Even number checking
- User-friendly menu interface
- Error handling for invalid inputs

## Project Structure

```
math_cli_app/
├── addition.py      # Addition operation implementation
├── factorial.py     # Factorial calculation implementation
├── odd_even.py      # Odd/Even number checking implementation
├── main.py          # Main CLI application
└── README.md        # This file
```

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the files
2. Navigate to the project directory:
   ```bash
   cd math_cli_app
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the on-screen menu to select an operation:
   - Option 1: Addition
   - Option 2: Factorial
   - Option 3: Odd/Even Check
   - Option 4: Exit

3. Enter the required numbers when prompted

## Examples

### Addition
```
Enter your choice (1-4): 1
Enter first number: 5
Enter second number: 3
The sum is: 8
```

### Factorial
```
Enter your choice (1-4): 2
Enter a non-negative integer: 5
The factorial of 5 is: 120
```

### Odd/Even Check
```
Enter your choice (1-4): 3
Enter an integer: 7
The number 7 is Odd
```

## Error Handling

The application includes error handling for:
- Invalid menu choices
- Non-numeric inputs
- Negative numbers for factorial
- Invalid integer inputs

## Contributing

Feel free to submit issues and enhancement requests! 
