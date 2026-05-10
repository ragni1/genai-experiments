import json
from datetime import datetime

class ERPOrderAgent:
    def __init__(self, file_path="orders.json"):
        self.file_path = file_path

    def place_order(self, order_details):
        try:
            data = [o.to_dict() for o in order_details]
            with open(self.file_path, "a") as f:
                f.write(json.dumps({
                    "timestamp": datetime.now().isoformat(),
                    "orders": data
                }) + "\n")
            return True
        except Exception as e:
            print(f"Error saving order: {e}")
            return False
