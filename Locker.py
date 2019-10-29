class Locker:
    def __init__(self, position, width, height, depth, material, private_key):
        self.position = position
        self.width = width
        self.height = height
        self.depth = depth
        self.material = material
        self.private_key = private_key
        self.is_bulky = (self.depth * self.height * self.width) > 2000000

    def is_code_valid (self, code):

        if len(code) >= 4 and len(code) <= 8:
            return True
        else:
            return False

    def is_secret_passed (self, code):

        code_sum = 0
        code_coded = []

        for i in range(len(code)):

            if code[i] == "A":

                code_coded.append(1)

            if code[i] == "B":

                code_coded.append(2)

            code_sum += code_coded[i]

        if code_sum % self.private_key == 0:

            return True
        else:
            return False





