def draw_square(size:int, filled=False, char="*")-> str:
    """
    This function draws a square of given size.

    Args:
        size (int): size of the square (side length).
        filled (bool, optional): If True, the square is filled. Defaults to False.
        char (str, optional): Character used to draw the square. Defaults to "*".

    Returns:
        str: A string representation of the square.
    """
    square='' 
    for i in range(size) :
        for j in range(size) :
            if filled:
                square += char
            else:
                if i == 0 or i == size - 1:
                    square += char
                elif j == 0 or j == size - 1:
                    square += char
                else:
                    square += ' ' 
        square +='\n'
    return sqaure
def draw_number_triangle(height:int)->str:
    """
    This function draws a triangle of numbers with the given height.
    i.e height = 4
    returns: 
        1 
        2 3 
        4 5 6 
        7 8 9 10
        
    Args:
        height (int): height of the triangle.

    Returns:
        string : A string representation of the number triangle.
    """
    triangle ='' 
    for i in range(height) :
        for j in range(1,i+1) :
            triangle += str(j)
        triangle +='\n' 
    return triangle 
        

def factorial(n:int):
    """
    Calculate factorial of n (n!)
    A factorial is the product of all positive integers less than or equal to n.
    i.e factorial(5) or 5! = 5 * 4 * 3 * 2 * 1 = 120

    n: non-negative integer
    return: n!
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
    
def bar_graph()->str:
    """
    This function draws a graph of averages per class:
    
    read data from grades.txt, there is data for 8 class and marks for 15 students per class
    each row represents a class and each column represents a student marks
    
    Task is to draw a bar graph of averages per class:
    each '*' represents 10 % 
    i.e
    
    Class averages:
    1: *****
    2: ********
    3: **
    4: *****
    ... etc.

    returns:
        str: string of the graph
    """
    bar ='' 
    with open('grades.txt','r') as f:
        for idx, line in enumerate(f, 1):
            grades = line.split(',')
            grades = [int(i.strip()) for i in grades] 
            avg = sum(grades) /len(grades) 
            bar +=f"{idx}: {'*' *avg}\n"
        return bar


def pascals_triangle(rows:int)->list[int]:
    """ p(n, k) = n! / (k! * (n-k)!)
    
    
    n: number of rows starting from 0
    k: column number starting from 0
    i.e 
    rows 
    0:              1
    1:            1   1
    2:          1   2   1
    3:        1   3   3   1
    4:      1   4   6   4   1
    5:    1  5  10  10   5   1
    6:  1  6  15  20  15   6   1
    7:1  7 21  35  35  21   7   1
    
    example:
        pascals_triangle(5)
        returns [1, 5, 10, 10, 5, 1]
        using 'p(n, k) = n! / (k! * (n-k)!)'
    """
    pascal =[] 
    for i in range(rows) :
        triangle=[] 
        for j in range(i+1):
            triangle.append(int(factorial(i)/(factorial(j) *factorial(i-j))))
        Pascal.append(triangle)
    return pascal[rows+1]


    
    
def main():
    chars = ['#', '*', '+', '@', '%']
    for i in range(3,8):
        print(draw_square(i,False,char=chars[i-3]))
        
    print()
    print(draw_number_triangle(6))
    print(factorial(5))
    print()
    print(pascals_triangle(5))
    print(bar_graph())
    print()
 
    
if __name__ == "__main__":
    main()

    
    
