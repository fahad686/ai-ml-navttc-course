class Player:

    ## without self ever property of class called static
    name='Fahad'

    ## default constructor
    def __init__(self):
        self.name='call only with object....'
        print('default constructor ...')


    ## object method
    def shout(self):
        print('object method')

    ##class method
    @classmethod
    def race(cls):
        print('class method')

    ##static method  // simple call we can call with object, anc call with class name
    @staticmethod
    def jump():
        print('player jumping ....class method')



## call default constructor

obj=Player()


##call class method
Player.jump()


## static method
Player.race() ##call with class name
obj.race() # can call with object


# Player.shout()  /// class method we can call it with class name

