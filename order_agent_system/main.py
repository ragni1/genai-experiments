from agents.email_reader_agent import EmailReaderAgent
from agents.order_pull_agent.order_parser_agent import OrderParserAgent
from agents.order_pull_agent.prompt import load_prompt
from agents.erp_order_agent import ERPOrderAgent
from agents.messaging_agent import MessagingAgent

def main():
    # Step 0: Email Text/File -> A class cab be added to read diff. file types
    email = """Hello There, I am sharing my order details below: 
                item_number: 5
                item_name: ITC Notebook
                Kindly place the order in the ERP system."""
    
    # Step 1: Read email
    reader = EmailReaderAgent(email)
    email_text = reader.read()

    # Step 2: Parse orders
    parser = OrderParserAgent()
    orders = parser.parse(email_text)

    # Step 3: Place orders (save to file)
    erp_agent = ERPOrderAgent("orders.json")
    success = erp_agent.place_order(orders)

    # Step 4: Send confirmation/failure
    messenger = MessagingAgent()
    messenger.send_confirmation(success)


# # Example usage
if __name__ == "__main__":
    main()
