import turtle
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: count
    """
    count=0
    while(n != 1):
        if(n % 2) == 0:        # n is even
            n = n // 2
            count=count+1
        else:                 # n is odd
            n = n * 3 + 1
            count=count+1
                      # the last print is 1
    return count
def draw_graph(bound=None):
  ''' This function draws a graph of the 3n+1 sequence
  args: bound (int)
  returns: None
  '''
  wn = turtle.Screen()
  drawer = turtle.Turtle()
  writer = turtle.Turtle()
  wn.setworldcoordinates(0,0,10,10)
  max_so_far = 0
  label = None
  drawer.goto(1,0)
  for i in range(1,bound+1):
    result = seq3np1(i)
    if result > max_so_far:
      max_so_far = result
      label = 'Maximum so far: '+ str(i) + ", " + str(result)
      writer.clear()
    writer.up()
    writer.goto(0,max_so_far)
    writer.write(label,align = "left")
    wn.setworldcoordinates(0,0,i+10,max_so_far+10)
    drawer.goto(i, result)
  wn.exitonclick()
  
  
  
def main():
  upper_bound = int(input("What is the upper bound?"))
  if upper_bound < 1:
    return
  start = upper_bound+1
  for i in range(1,start):
    iterations = seq3np1(i)
    print("Current loop value: ",i, " Iterations: ", iterations)
  draw_graph(upper_bound)

main()

