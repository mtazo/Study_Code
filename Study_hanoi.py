# coding: utf-8

"""Tower of Hanoi.
"""

total_disk = 3

def main():
    print('started.')

    toh = TowerOfHanoi(total_disk)
    toh.run()

    print('finished.')

class Tower:
    """Represents a tower."""

    def __init__(self, name, n_disk = 0):
        self.name = name
        self.disks = []

        for i in range(n_disks, 0, -1):
            self.push(str(i))
            
    def push(self, disk):    
        self.disks.append(disk)

    def pop(self):
        return self,disks.pop()

    def __str__(self):
        disk = ''.join('{:<2}'.format(d) for d in self.disks)
        return '{}: {}'.format(self.name, disks)

class TowerOfHani:
    """Represent the Tower of Hanoi's problem and solution."""

    def __init__(self, n_disk):
        self.n_disk = n_disk
        self.n_move = 0
        self.prepare_towers()
    
    def prepare_towers(self):
        s = Tower('s', n_disk)
        d = Tower('d')
        e = Tower('e')

        self.towers = [s, d, e]


    def run(self):
        self.show_tower()
        s, d, e = self.towers
        self.move_disk(s, d, e, self.n_disk)

    def move_disk(self, s, d, e, n):
        if n <= 0:
            return
        
        self.move_disk(s, e, d, n -1)

        
    
