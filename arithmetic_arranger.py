def arithmetic_arranger(problems,bool=False):
  sumx = ""
  first = ""
  second = ""
  lines = ""
  for problem in problems:
    if (re.search("[^\s0-9.+-]",problem)):
      if (re.search("[/]",problem) or re.search("[*]",problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."
      #We use RegEx to limit the string we get to digits and operands and then we limit it so the only operands we take are + and -
    if (len(problems)>5):
      return"Error: Too many problems."
      #Limit the number of operations to be rearranged to 5
    posplus = problem.find('+')
    possub = problem.find('-')      
    if (posplus != -1):
      num1 = problem[:posplus-1]
      num2 = problem[posplus+2:]
      operator = problem[posplus]
    if (possub != -1):
      num1 = problem[:possub-1]
      num2 = problem[possub+2:]
      operator = problem[possub]
      #To divide the string in first, second number and the operator
    if (len(num1)>=5 or len(num2)>=5):
      return "Error: Numbers cannot be more than four digits."
      #Limit the number to 4 digits
    if (operator == "+"):
      sum = str(int(num1) + int(num2))
    elif (operator=="-"):
      sum = str(int(num1) - int(num2))
      #In case we have a true in the call to the function we need to solve the operation
    length = max(len(num1),len(num2)) + 2
    #Check the longer string between the 2 numbers
    top = str(num1).rjust(length) #This right allings the number and also makes it so the length of the string matches that of the max
    bottom = operator + str(num2).rjust(length-1) #Same as above but we have to put the operator and take into account the space the operator takes
    line = ""
    res = str(sum).rjust(length)
    #The result of operation
    for s in range(length):
      line += "-"
    #The dashes for the bottom part

    if problem != problems[-1]: #This means that the problem the loop is currently on is not the last problem [-1] means last element
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      second += bottom
      lines += line
      sumx += res
    #This is so that the last element we print we dont print it leaving 4 spaces after it
  if bool==True:
    arranged_problems = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    arranged_problems = first + "\n" + second + "\n" + lines
  return arranged_problems
