from sales import calc_shipping, calc_tax

class UseUm:
    def __init__(self, vibe):
        self.vibe = vibe
    def __doc__(self):
        return "This is a doc string object."

using = UseUm('Low')
print(using.__doc__())
