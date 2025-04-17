import doctest

"""
Competition answer sheet
NOTE: DO NOT ask for user input. Mark penalties will be incurred if ignored.
Group Number: 15
Group Name: Big Balls

Group Member 1 Name: Pang Chang Sheng
Group Member 1 Student ID: 35478136

Group Member 2 Name: Matthew Chong Zi Jun
Group Member 2 Student ID: 35534109

"""

##########################################################################
# Question 1
"""
print((15+62)*4)
308


"""
##########################################################################
# Question 2
"""
False


"""
##########################################################################
# Question 3
"""
False

"""
##########################################################################
# Question 4
"""
33.33

"""
##########################################################################
# Question 5
"""
File "<ipython-input-5-48f1533e16ec>", line 1
    print("Coding", "Is" + "Fun", “if you are passionate”)
                                  ^
SyntaxError: invalid character '“' (U+201C)

"""

##########################################################################
# Question 6
"""
y = 7
print("The value of y is: " + str(y))

"""
##########################################################################
# Question 7
"""
Unknown drink!

"""
##########################################################################
# Question 8
"""
Mature adult

"""
##########################################################################
# Question 9
"""
no output

counter = 0

while not (counter > 3 and counter < 5):

    counter += 1

    print(counter)

1
2
3
4

"""
##########################################################################
# Question 10
"""
print(numbers[len(numbers)-2])

"""
##########################################################################
# Question 11
def joinStringsWithHyphen(x, y):
  x_strip = str.strip(x)
  y_strip = str.strip(y)
  return f"{x_strip}-{y_strip}"

##########################################################################
# Question 12
def convertLength(cm):
  meter = cm/100
  km = meter/1000
  return [meter,km]


##########################################################################
# Question 13
def doubleChars(x):
  hist = []
  for alphabet in x:
    hist.append(alphabet)
    hist.append(alphabet)

  return "".join(hist)


##########################################################################
# Question 14
def getUpperCase(s):
  hist = []
  for alphabet in s:
    if alphabet in "QWERTYUIOPASDFGHJKLZXCVBNM":
      hist.append(alphabet)
  return "".join(hist)


##########################################################################
# Question 15
def countVowels(s):
  count = 0
  for alphabet in s:
    if alphabet in "AEIOUaeiou":
      count += 1
  return count


##########################################################################
# Question 16
def isAnagram(s1, s2):
  s1 = []
  s2 = []
  for a in s2:
    s2.append(a)
  for a in s1:
    s1.append(a)
  s1.sort()
  s2.sort()
  return s1 == s2


##########################################################################
# Question 17
def sumOfSquares(x):
  num = 0
  for i in x:
    num += i**2
  return num


##########################################################################
# Question 18
def longestCommonPrefix(strings):
  prefixes = []
  count = []
  for string in strings:
    prefix = f"{string[0]}{string[1]}"
    prefixes.append(prefix)
  return prefixes[1]

##########################################################################
# Question 19
def findMissingNumber(arr):
  arr.sort()
  for i in range(len(arr)):
    if (i+1) != arr[i]:
      return i+1
##########################################################################
# Question 20
def flattenNestedList(nestedList):
  new_list = []
  for nest in nestedList:
    if len(nest) > 0:
      for integer in nest:
        if type(integer) == list:
          for i in integer:
            new_list.append(i)
        else:
            new_list.append(integer)
  return new_list


##########################################################################
##########################################################################

if __name__ == "__main__":
    # Test your code here (not marked)
    pass

