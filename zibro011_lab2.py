class Zillion:
    
    def __init__(self,digits):
        self.l=[] #create empty list
        count = 0
        for a in digits:
            if (a==' ' or a== ','):
                self.l = self.l
            else:
                try:
                    self.l.append(int(a))
                    count+=1                   #add numbers to list
                except:
                    raise RuntimeError
        if (count==0):
            raise RuntimeError              #check if empty

    def increment(self):
        i = len(self.l) - 1
        while i >=0:
            if(self.l[i] == 9):
                self.l[i] = 0
                i= i-1
            else:
                self.l[i] +=1
                break
        if (i == -1):
                self.l = [1] + self.l

    def isZero(self):
       for x in self.l:
        if (x!= 0):
            return False
        else:
            return True

    def toString(self):
        s =''
        for a in self.l:
            s = s +str(a)
        return s
        


try:
  z = Zillion('')
except RuntimeError:
  print('Empty string')

# It must print 'Empty string' without apostrophes. 2 points.

try:
  z = Zillion(' , ')
except RuntimeError:
  print('No digits in the string')

# It must print 'No digits in the string' without apostrophes. 2 points.

try:
  z = Zillion('1+0')
except RuntimeError:
  print('Non-digit in the string')

# It must print 'Non-digit in the string' without apostrophes. 2 points.

try:
  z = Zillion('0')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.
#z = Zillion('0')
print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('000000000')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('000 000 000')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('997')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing.  2 points.

print(z.isZero())    #  It must print False. 2 points.

#stops working here
print(z.toString())  #  It must print 997. 2 points. 

z.increment()

print(z.toString())  #  It must print 998. 2 points.

z.increment()

print(z.toString())  #  It must print 999. 2 points.

z.increment()

print(z.toString())  #  It must print 1000. 2 points.

try:
  z = Zillion('0 9,9 9')
except:
  print('This must not be printed')

#  It must print nothing.  3 points.

z.increment()
print(z.toString())  #  It must print 1000. 2 points.
