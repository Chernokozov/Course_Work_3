class Operation:
    def __init__(
            self,
            date,
            state,
            amount,
            currency_name,
            description,
            from_,
            to,
    ):
        """
        Инициализация класса Operation

        """
        self.date = date
        self.state = state
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_
        self.to = to

