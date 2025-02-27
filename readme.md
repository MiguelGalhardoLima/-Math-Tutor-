# Mathematical Tutor System

The **Mathematical Tutor System** is a simple system that simulates a basic math tutor. It receives and answers mathematical questions, validating the input and processing the question with a **Virtual Professor** that calculates the answer.

## Requirements
- **Python 3.x**
- No external libraries required

## How to Use

1. Download or clone this repository to your local machine using:
    ```bash
    git clone https://github.com/YOUR_USERNAME/Mathematical-Tutor-System.git
    ```

2. Then, navigate to the folder where the script is located and run:
    ```bash
    python main.py
    ```

3. The system will prompt you to enter a valid mathematical expression (e.g., `5+3`, `7*2`, etc.). Simply input your expression, and the system will return the calculated answer.

4. If you provide a non-mathematical question (e.g., `What is the capital of Brazil?`), the system will inform you that the question is invalid.

### Example Usage

```plaintext
Question: 5+3
Response:
{
  "answer": 8
}
Question: What is the capital of Brazil?
Response:
{
  "error": "Invalid question. Please send a mathematical query."
}
```

### How It Works
The system consists of two main classes:

Receiver: This class receives the question, checks if it is a valid mathematical query, and forwards it to the Virtual Professor. If the input is not mathematical, it returns an error message.

Virtual Professor: This class processes the mathematical question, evaluates the expression, and returns the result. If there is an issue with processing (e.g., invalid syntax), an error message will be returned.

### Future Improvements
Integration with LangChain: The next step is to integrate LangChain for using LangGraph, improving the communication between agents and enhancing the system's structure.
### Contributing
Feel free to contribute to this project by opening issues and submitting pull requests. Any contribution is welcome!
