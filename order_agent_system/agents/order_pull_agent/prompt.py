
def load_prompt():
    return """You are an intelligent document system. 
            Return ONLY valid JSON. Do not include explanations, code, or text outside the JSON. 
            If unclear, return null.
            
            Example Input and Output:
            Input: Hello There, I am sharing my order details below: 
            Order 1: 
            Item Number: 5
            Item Name: ITC Notebook
            
            Order 2: 
            Item Number: 10
            Item Name: ITC Ball Pen
            
            Kindly place the order in the ERP system.
            
            Output Format (This should not be actual output):
            {
            'Order_1': {'item_name':'ITC Notebook', 'item_unit':5},
            'Order_2':{'item_name':'ITC Ball Pen', 'item_unit':10}
            }
            Constrains:
            If the order details are not clear, return Null
    """
