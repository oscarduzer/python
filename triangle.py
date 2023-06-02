class Triangle:
    def __init__(self,AB,BC,AC):
        self.AB=int(AB)
        self.BC=int(BC)
        self.AC=int(AC)

    def isset(self):
        if (self.AB+self.BC) < (self.AC):
            return False
        elif (self.AB+self.AC) < (self.BC):
            return False
        elif (self.AC+self.BC) < (self.AB):
            return False
        else:
            return True
        
    def maximum(self):
        if self.isset():
            maxi=max(self.AB,self.BC,self.AC)
            return int(maxi)
    
    def perim(self):
        if self.isset():
            return self.AB+self.BC+self.AC
        else:
            return None

    def equil(self):
        if self.isset():
            if self.AB==self.BC and self.AB==self.AC:
                return True
            else:
                return False
        else:
            return False
    
    def iso(self):
        if self.isset():
            if self.AB==self.BC or self.AB==self.AC or self.BC==self.AC:
                return True
            else:
                return False
        else:
            return False

    # def rect(self):  
    #     if self.isset():
    #         maxi=max(self.AB,self.BC,self.AC)
    #         if maxi==self.AB:
    #             pow=self.BC*self.BC+self.AC*self.AC
    #             if pow == self.AB*self.AB:
    #                 return True
    #         elif maxi==self.BC:
    #             pow=self.AB*self.AB+self.AC*self.AC
    #             if pow==self.BC*self.BC:
    #                 return True
    #         elif maxi==self.AC:
    #             pow=self.BC*self.BC+self.AB*self.AB
    #             if pow == self.AC*self.AC:
    #                 return True
    #         else:
    #             return False
    #     else:
    #         return False


    
tri=Triangle(2,2,4)

print(tri.equil())


