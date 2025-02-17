"""
Context managers (used with the "with" statement) 
and try-finally are both constructs in Python that 
help you ensure certain cleanup code runs even in the presence of exceptions.
"""

with open("context_manager.py") as f:
    print(f.read())


class MyContextManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Open the file and return the file object
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Handle any exceptions if they occur
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        # Close the file whether or not an exception occurred
        if self.file:
            self.file.close()

# Usage example
with FileOpener('sample.txt', 'w') as f:
    f.write("Hello, World!")

