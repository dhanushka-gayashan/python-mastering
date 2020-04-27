# If there will be future "inheritance" and no need to access the class itself, then use "Class Methods"
# If there will be no any future "inheritance", then use "Static Methods"

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    # Create the new object base on the "cls" type. 
    # This important to desice which "__repr__" need to run
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2) 

    @staticmethod
    def show_county(country):
        return f'It is the currecy of {country}'


class Doller(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbole = '$'

    def __repr__(self):
        return f'<Doller {self.symbole}{self.amount:.2f}>'


new_number = FixedFloat.from_sum(19.3456, 0.34546)
print(new_number)
print(FixedFloat.show_county("Common"))


doller2 = Doller.from_sum(18.7899, 16.4546)
print(doller2)
print(Doller.show_county("USA"))
