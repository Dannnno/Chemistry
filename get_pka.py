def get_pka(hydrogen):
    
    if len(hydrogen.bonds) == 0: pass
    else: 
        other = hydrogen.bonds[0].get_other(hydrogen)
        if other.name == "Hydrogen": 
            print "H2"
            return 42.
        elif other.name == "Carbon": pass
        elif other.name == "Sulfur": pass
        elif other.name == "Nitrogen": pass
        elif other.name == "Oxygen": 
            if other.charge == 1:
                if len(other.bonds) == 2:
                    if other.is_bonded_to("Carbon"):
                        print "Alcohol"
                        return
                    elif other.is_bonded_to("Hydrogen", exclude=[hydrogen]):
                        print "Water"
                        return 15.7
                    else: raise NotImplementedError
                elif len(other.bonds) == 3: 
                    if len(filter(lambda x: 
                                    x.get_other(other).name == "Hydrogen",
                                  other.bonds)) == 3:
                        print "Hydronium"
                        return 
                    else:
                        pass
            elif other.charge == 1: pass
            else: raise NotImplementedError
        elif other.name in ["Chlorine", "Iodine", "Fluorine", "Bromine"]:
            pass
        else: raise NotImplementedError