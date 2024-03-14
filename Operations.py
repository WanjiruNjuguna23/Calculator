import re

class Operations:
    @staticmethod
    def is_valid_input(user_input):
        """
        Check if the input contains only valid characters.

        Args:
        - user_input (str): User input to validate

        Returns:
        - bool: True if the input is valid, False otherwise
        """
        return bool(re.match(r'^[\d()+\-*/.\s]*$', user_input))

    @staticmethod
    def evaluate_expression(expression):
        """
        Evaluate a mathematical expression in infix notation.

        Args:
        - expression (str): Mathematical expression to evaluate

        Returns:
        - float: Result of the evaluation
        """
        operators = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []
        tokens = re.findall(r'[0-9.]+|[()+\-*/]', expression)

        for token in tokens:
            if re.match(r'[0-9.]+', token):
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and operators.get(token, 0) <= operators.get(stack[-1], 0):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return Operations.calculate_rpn(output)

    @staticmethod
    def calculate_rpn(tokens):
        """
        Calculate the result of an expression in Reverse Polish Notation (RPN).

        Args:
        - tokens (list): List of tokens in RPN notation

        Returns:
        - float: Result of the calculation
        """
        stack = []
        for token in tokens:
            if re.match(r'[0-9.]+', token):
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
        return stack[0] if stack else None
