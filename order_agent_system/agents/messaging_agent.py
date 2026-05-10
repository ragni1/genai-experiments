class MessagingAgent:
    def send_confirmation(self, success):
        if success:
            print("✅ Order placed successfully. Confirmation sent.")
        else:
            print("❌ Failed to place order. Failure message sent.")
