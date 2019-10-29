class Locker:
    def __init__(self, position, width, height, depth, material, private_key):
        self.position = position
        self.width = width
        self.height = height
        self.depth  = depth
        self.material = material
        self.private_key = private_key
        self.is_bulky = ((width * height * depth) / 1000000) > 2.0

    def is_code_valid(self, code_name):
        if(len(code_name) >= 4 and len(code_name) <= 8):
            return True
        else:
            return False

    def is_secret_passed(self, secret):
        result = 0

        for c in secret:
            if(c == 'A'):
                result += 1
        for c in secret:
            if(c == 'B'):
                result += 2
                          
        if((result % self.private_key) == 0):
            return True
        else:
            return False

