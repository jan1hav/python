import random

class Coin:

    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for k,v in kwargs.items():
            setattr(self,k,v)
        
        self.heads = True
        self.israre = rare
        self.isclean = clean
        
        

        if self.isclean:
            self.color = self.c_color
        else:
            self.color = self.r_color

    def rust(self):
        self.color = self.r_color
        print("Coin Color: {}.".format(self.color))

    def clean(self):
        self.color = self.c_color
        print("Coin Color: {}.".format(self.color))

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def rare_c(self):
        if self.israre == False:
            self.israre = True
            if self.israre:
                self.value *= 1.25
            else:
                self.value = self.value
        else:
            pass

    # Destructing
    def __del__(self):
        print("Coin Spent!")

    def __str__(self):
        if self.value >= 1.00:
            return "{}Pound coin".format(int(self.value))
        else:
            return "{}pence coin".format(int(self.value * 100))


class One_pence(Coin):
    def __init__(self):
        data = {
            "value": 0.01,
            "c_color": 'bronze',
            "r_color": 'brownish',
            "edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
            }
        super().__init__(**data)


class Two_pence(Coin):
    def __init__(self):
        data = {
            "value": 0.02,
            "c_color": 'bronze',
            "r_color": 'brownish',
            "edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
            }
        super().__init__(**data)

class Five_pence(Coin):
    def __init__(self):
        data = {
            "value": 0.05,
            "c_color": 'silver',
            "r_color": None,
            "edges": 1,
            "diameter": 18,
            "thickness": 1.77,
            "mass": 3.25
            }
        super().__init__(**data)

    def rust(self):
        self.color = self.c_color

class Ten_pence(Coin):
    def __init__(self):
        data = {
            "value": 0.1,
            "c_color": 'silver',
            "r_color": None,
            "edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50
            }
        super().__init__(**data)

    def rust(self):
        self.color = self.c_color

class Twenty_pence(Coin):
    def __init__(self):
        data = {
            "value": 0.20,
            "c_color": 'silver',
            "r_color": None,
            "edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00
            }
        super().__init__(**data)

    def rust(self):
        self.color = self.c_color

class Fifty_pence(Coin):
    def __init__(self):
        data = {
            "value": 0.50,
            "c_color": 'silver',
            "r_color": None,
            "edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8.00
            }
        super().__init__(**data)

    def rust(self):
        self.color = self.c_color
            

class One_pound(Coin):
    def __init__(self):
        data = {
            "value": 1.00,
            "c_color": 'gold',
            "r_color": 'greenish',
            "edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
            }
        super().__init__(**data)

class Two_pound(Coin):
    def __init__(self):
        data = {
            "value": 2.00,
            "c_color": 'gold & silver',
            "r_color": 'greenish',
            "edges": 1,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00
            }
        super().__init__(**data)


coins = [One_pence(), Two_pence(), Five_pence(), Ten_pence(), Twenty_pence(),
         Fifty_pence(), One_pound(), Two_pound()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness,
           coin.edges, coin.mass]
    string = "{} - Color: {}, Value: {}, Diameter: {}, Thickness: {}, Edges: {}, Mass: {}".format(*arguments)
    print(string)    
