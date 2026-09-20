
def pay_premium(amount):

    try:

        amount = float(amount)

        if amount <= 0:
            raise ValueError("Payment amount must be positive.")

        print("Processing payment...")
        print("Payment successful.")

    except ValueError as ex:

        print("Payment failed:", ex)

    finally:

        print("Payment operation completed.")
        
pay_premium(25000)        