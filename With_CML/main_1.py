class Element(object):
    count = [0]*118

    def __init__(self, symbol='C', number=12, name="Carbon", bonds=[]):

        self.symbol = symbol
        self.number = number
        self.name = name
        self.bonds = list(bonds)
        Element.count[number] += 1


    def add_bond(self, other, bond_info):
        try:
            if isinstance(other, Element):
                temp_bond = Bond(self, other, *bond_info)
                self.bonds.append(temp_bond)
                other.bonds.append(temp_bond)

            else:
                raise BondingException(''.join(["Object \"", repr(other), "\":",
                                                str(type(other)), " could not",
                                                " be bonded to element ",
                                                self.name]))
        except BondingException as BE:
            print BE
            return


    def remove_bond(self, bond):
        try:
            if bond in self.bonds:
                self.bonds.pop(bond)
            else:
                raise BondingException(''.join(["Bond \"", repr(bond),
                                                 "\" does not exist for element ",
                                                 self.name]))
        except BondingException as BE:
            print BE
            return


    def __del__(self):
        Element.count[self.number] += -1


class Bond(object):

    def __init__(self, first_element, second_element, order=1,
                 chirality=None):
        self.first = first_element
        self.second = second_element
        self.order = order
        self.chirality = chirality
        self.type = self.eval_bond()

    def eval_bond(self):
        """This method will determine covalent/ionic bond"""
        pass




class BondingException(Exception):

    def __init__(self, err_message="Bonding Error"):
        self.err_message = err_message

    def __str__(self):
        return self.err_message

    def __repr__(self):
        return self.err_message

print Element.count[12]
a = Element()
print Element.count[12]
b = Element()
print Element.count[12]
del a
print Element.count[12]
del b
print Element.count[12]
