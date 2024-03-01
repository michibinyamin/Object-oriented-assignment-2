from Post import Post


class SalePost(Post):
    def __init__(self, user, t, price, location):
        super().__init__(user)  # Should be implemented here?
        self.item_type = t    # type of item (string)
        self.price = price  # The price (int)
        self.location = location    # Item location (string)
        self.__availability = True    # Item availability (bool)

    def discount(self, dis, password):
        if self.uploader.is_online:  # Make sure user is online
            if self.uploader.get_password() == password:
                discounted_price = self.price * (1 - dis / 100)
                self.price = discounted_price
                print(f"Discount on {self.uploader.name} product! the new price is: {discounted_price}")
        else:
            print("You are offline")

    def sold(self, password):
        if self.uploader.is_online:  # Make sure user is online
            if self.uploader.get_password() == password:
                self.__availability = False
                print(f"{self.uploader.name}'s product is sold!")
        else:
            print("You are offline")

    def __str__(self):
        if self.__availability:
            return (f"{self.uploader.name} posted a product for sale:\nFor sale! {self.item_type}, price: {self.price},"
                    f" pickup from: {self.location}")
        else:
            return (f"{self.uploader.name} posted a product for sale:\nSold! {self.item_type}, price: {self.price},"
                    f" pickup from: {self.location}")

