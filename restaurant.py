class Restaurant():

    def __init__(self, name, cuisine):
        """Initialize attributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Formatted and concatenated output"""
        long_desc = self.name.title() + " serves " + self.cuisine + "."
        return long_desc

    def format_served(self):
        output = str(self.number_served) + ' customers served.'
        return output

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, increment):
        self.number_served += increment

wendys = Restaurant('wendys', 'fast food')
print(wendys.describe_restaurant())
print(wendys.format_served())

jacks = Restaurant('jack in the box', 'fast food')
jacks.set_number_served(250)
print(jacks.describe_restaurant())
print(jacks.format_served())

roundtable = Restaurant('roundtable', 'pizza')
roundtable.increment_number_served(50)
print(roundtable.describe_restaurant())
print(roundtable.format_served())

