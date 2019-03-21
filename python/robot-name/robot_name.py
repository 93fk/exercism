import random
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
robot_IDs = []


class Robot(object):

    def generate_name():
        let = ''.join([letters[random.randint(0, 25)] for i in range(2)])
        num = ''.join(map(str, [random.randint(0, 9) for n in range(3)]))
        name = let + num
        if name in robot_IDs:
            generate_name()
        else:
            robot_IDs.append(name)
            return name

    def __init__(self):
        self.name = Robot.generate_name()

    def reset_name(self):
        robot_IDs.remove(self.name)
        self.name = Robot.generate_name()
