class cars:
    # constractor
    def __init__(self,type ,colour,model):
       self.type=type
       self.colour=colour
       self.model=model
    # method
    def onyesha(self):
        print(f"i love {self.model} cars which is a {self.type} being {self.colour}")
        # creating object
myobj = cars("saloon","white","toyota")
myobj.onyesha()