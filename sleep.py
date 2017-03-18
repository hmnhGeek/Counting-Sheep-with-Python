

class sleep(object):

    def __init__(self):
        self.nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.occured = [0 for i in range(10)]

    def check(self, List, numb):
        count_1 = 0
        for element in List:
            if element == 1:
                count_1 += 1
        if count_1 == len(List):
            return True, numb
        else:
            return False, None
    
    def start(self, N):
        if (N <> 0):
            original = N
            i = 1
            tup = self.check(self.occured, N)
            
            while not tup[0]:
                N = str(i*int(original))
                
                for number in N:
                    if self.occured[self.nums.index(number)] == 0:
                        self.occured[self.nums.index(number)] = 1
                tup = self.check(self.occured, N)
                i+=1
            self.occured = [0 for i in range(10)]
            return tup[1]
        else:
            return 'INSOMNIA'
