class Claim:

    def __init__(self, claim_id, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def update_amount(self, amount):
        if amount > 0:
            self.__amount = amount