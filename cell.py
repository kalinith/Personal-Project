# each cell is a Class consisting of a grid plot and a subgrid plot
#    and a data value
#    a potential dictionary with 1-9 as the ref and Y as the value.
#    as numbers are eliminated they will be set to n on the potentials
# a plot has an x and y co-ordinate.

def test_number(x):
    if x > 9 or x <= 0:
        raise ValueError(f"{x} is not beween 1 and 9")
    return True

class Cell():
    def __init__(self, x, y, val=None):# x and y are grid-coords
        self.__gridplot = Plot(x,y,"Grid")
        self.__subgridplot = Plot(x % 3,y % 3, "Subgrid")
        self.__subgrid = Plot(x // 3, y // 3, "Subgrid")
        self.val = val
        self.__potential_val = dict()
        self.init_option()

    def get_grid_pos(self):
        return self.__gridplot.x, self.__gridplot.y

    def get_subgrid_pos(self):
        return self.__subgridplot.x, self.__subgridplot.y

    def get_subgrid(self):
        return self.__subgrid.x, self.__subgrid.y

    def init_option(self, isval="y"):
        for i in range(1,10):
            self.__potential_val[i] = isval

    def remove_option(self, option):
        if test_number(option):
            self.__potential_val[option] = "n"

    def add_option(self, option):
        if test_number(option):
            self.__potential_val[option] = "y"

    def is_option(self, option):
        try:
            test_number(option)
            return self.__potential_val[option]
        except ValueError:
            return "n"

    def has_options(self):
        return sum([len(self.__potential_val[x]) for x in self.__potential_val if self.__potential_val[x] == "y"])

    def get_options(self):
        options = list()
        for key, value in self.__potential_val.items():
            if value == "y":
                options.append(key)
        return options

    def set_val(self, value):
        if test_number(value):
            self.val = value
            self.init_option("n")

    def clear_val(self):
        self.val = None
        self.init_option()

    def pick_one(self, value=[0,]):
        for i in self.__potential_val:
            if self.__potential_val[i] == "y" and i not in value:
                self.set_val(i)
                return i
        return None


    def __str__(self):
        options = list()
        for key, value in self.__potential_val.items():
            if value == "y":
                options.append(key)

        returnstring = f"the value of the cell at {self.__gridplot.x} and {self.__gridplot.y}"
        if self.val == None:
            returnstring = f"{returnstring} can be one of the following:{options}"
        else:
            returnstring = f"{returnstring} is {self.val}"
        return returnstring

    def __repr__(self):
        options = list()
        for key, value in self.__potential_val.items():
            if value == "y":
                options.append(key)

        returnstring = f"the value of the cell at {self.__gridplot.x} and {self.__gridplot.y}"
        returnstring = f"{returnstring} can be one of the following:{options}"
        returnstring = f"{returnstring} and is currently {self.val}"
        returnstring = (str(n) for n in options)
        return ",".join(returnstring)

class Plot():
    def __init__(self, x, y, source):
        if (source == "Grid"):
            if x > 8 or x < 0:
                raise Exception(f"{x} is not beween 0 and 8")
            if y > 8 or y < 0:
                raise Exception(f"{y} is not between 0 and 8")
        if (source == "Subgrid"):
            if x > 2 or x < 0:
                raise Exception(f"{x} is not beween 0 and 8")
            if y > 2 or y < 0:
                raise Exception(f"{y} is not between 0 and 8")
        self.x = x
        self.y = y
