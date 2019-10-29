class Locker:
    def __init__(self,position,width,height,depth,material,private_key):
        self.position = position
        self.width = width 
        self.height = height
        self.depth = depth
        self.material = material 
        self.private_key = private_key
        if width*height*depth > 2000000:
            self.is_bulky = True
        else:
            self.is_bulky = False
    def is_code_valid(self,code) :
        if len(code)>=4 and len(code) <=8:
        return True
    else:
        return False



