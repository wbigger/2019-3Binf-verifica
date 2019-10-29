class Locker:
    def __init__(self, position,width,height,depth,material,private_key):
        self.position = position
        self.width = width
        self.height = height
        self.depth = depth
        self.material = material
        self.private_key = private_key 
        self.volume = height* width *depth
        if self.volume > 2000000:
            self.is_bulky = True
        else:
            self.is_bulky = False
        def is_code_valid()


     

   

