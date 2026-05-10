import json
from datetime import datetime

class EmailReaderAgent:
    def __init__(self, source_text):
        self.source_text = source_text

    def read(self):
        # In reality, this would connect to an email inbox
        return self.source_text
