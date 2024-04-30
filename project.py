class Volume:
    
    def _init_(self, initial, final, amount):
        self.initial= initial
        self.final = final
        self.amount = amount
        
    def unit(self):
        
        def cubicmeters(self):
            if self.final == "b":
                num = self.amount * 6.2898
                print(self.amount,"m³ is", num," barrels.")
            
            elif self.final == 'ft3':
                num = self.amount / 0.0283168466
                print(self.amount,"m³ is",num,"ft cubed.")
                
            elif self.final == "dm3":
                num = self.amount * 1000
                print(self.amount,"m³ is", num," cubic decimeters.")
                
        def Barrels(self):
                
              if self.final == "m3":
                num = self.amount * 0.159
                print(self.amount,"b is", num," cubicmeters.")
            
              elif self.final == 'ft3':
                num = self.amount * 5.615
                print(self.amount,"b is",num,"ft cubed.")
                
              elif self.final == "dm3":
                num = self.amount * 158.987
                print(self.amount,"b is", num," cubic decimeters.")
                
        def cubicfeet(self):
                
              if self.final == "m3":
                num = self.amount * 0.0283
                print(self.amount,"ft3 is", num," cubicmeters.")
            
              elif self.final == 'b':
                num = self.amount * 0.178
                print(self.amount,"ft3 is",num,"Barrels.")
                
              elif self.final == "dm3":
                num = self.amount * 28.317
                print(self.amount,"ft3 is", num," cubic decimeters.")
                
        def cubicdecimeters(self):
                
              if self.final == "m3":
                num = self.amount * 0.001
                print(self.amount,"dm3 is", num," cubicmeters.")
            
              elif self.final == 'ft3':
                num = self.amount * 0.0353
                print(self.amount,"dm3 is",num,"ft cubed.")
                
              elif self.final == "b":
                num = self.amount * 0.00629
                print(self.amount,"dm3 is", num," Barrels.")
                
        if self.initial == "m3":
            cubicmeters(self)
        elif self.initial == "b":
            Barrels(self)
        elif self.initial =="ft3":
            cubicfeet(self)
        elif self.initial=="dm3":
            cubicdecimeters(self)