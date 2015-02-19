class AtomMeta(type):

    # Returns what Class.__new__ returns,
    # and if it returned an instance of Class it will also call Class.__init__
    def __call__(cls, *args, **kwargs):
        return super(AtomMeta, cls).__call__(*args, **kwargs)

    # Returns the class object
    @classmethod
    def __new__(mcs, name, bases, attrs, **kwargs):
        return super(AtomMeta, mcs).__new__(name, bases, attrs)

    # Returns the namespace object (dictionary like)
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return {}


class Atom(object):

    __metaclass__ = AtomMeta


print type(AtomMeta), AtomMeta
print type(AtomMeta()), AtomMeta()
print type(Atom), Atom
print type(Atom()), Atom()