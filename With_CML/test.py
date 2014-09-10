def get_pka(hydrogen):
    if hydrogen.bonds:
        other = hydrogen.bonds[0].get_other(hydrogen)
        if other.name == "Carbon":
            if len(other.bonds) == 4:
                print "SP3 Carbon"
                return 50.
            elif len(other.bonds) == 3:
                if other.root == 4:
                    print "SP2 Carbon"
                    return 44.
                raise NotImplementedError("Carbon Ion")
            elif len(other.bonds) == 2:
                if other.root == 4:
                    print "SP Carbon"
                    return 25.
                raise NotImplementedError("Carbon Ion")
        elif other.name == "Nitrogen":
            if len(other.bonds) == 4:
                print "Positive Nitrogen"
                return 9.2
            elif len(other.bonds) == 3:
                print "Amine"
                return 38.
            raise NotImplementedError("Nitrogen problem")
        elif other.name == "Hydrogen":
            print "Conjugate acid of H-"
            return 35.
        elif other.name == "Sulfur":
            if len(other.bonds) == 2:
                print "Thiol"
                return 7.
            raise NotImplementedError("Sulfur problem")
        elif other.name == "Chlorine":
            print "Hydrochloric acid"
            return -6.
        elif other.name == "Bromine":
            print "Hydrobromic acid"
            return -9.
        elif other.name == "Iodine":
            print "Hydroiodic acid"
            return -10.
        elif other.name == "Oxygen":
            # Things get hairy
            if len(other.bonds) == 3:
                print "Positive Oxygen"
                return -2.
            elif len(other.bonds) == 2:
                next_other = other.bonds[0].get_other(other)
                next_name = next_other.name
                if next_name == "Carbon":
                    if next_other.is_aromatic:
                        print "Phenol"
                        raise NotImplementedError("Aromatic system")
                    elif len(next_other.bonds) == 4:
                        print "Alcohol"
                        return 16.
                    elif next_other.root == 4:
                        for bond in next_other.bonds:
                            next_next = bond.get_other(next_other)
                            if (next_next.name == "Oxygen" and
                            bond.order == 2):
                                continue
                            if next_next.name == "Carbon":
                                if any((abond.get_other(next_next).eneg > 2.5)
                                       for abond in next_next.bonds):
                                       print "Carboxylic acid with eneg groups"
                                       return 0.2
                                else:
                                    print "Carboxylic acid"
                                    return 4.8
                            raise NotImplementedError("What is happening here")
                elif next_name == "Hydrogen":
                    print "Water"
                    return 15.7
                elif next_name == "Sulfur":
                    print "Sulfuric acid"
                    return -9.
            elif other.root == 3:
                print "Protonated diene system"
                raise NotImplementedError("Protonated diene")
        raise NotImplementedError("We got to the end~")            
    else:
        raise NotImplementedError("This hydrogen isn't bonded to anything")
        