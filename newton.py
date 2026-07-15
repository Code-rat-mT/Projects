from numpy import linspace
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from sympy.solvers.solveset import solveset, solveset_real

import matplotlib.pyplot as plt


def distanceFromRoot(x, values):  
    currentDistance = abs(x-values[0])

    if len(values) > 1: 

        for value in values:
            newDist = abs(x-value)
            if newDist < currentDistance:
                currentDistance = newDist

    return currentDistance


def generateTangents(x0, real_roots, accuracy):
    if distanceFromRoot(x0, real_roots) > accuracy: ## Continue if the value we have calculated is still too far from a real root
        tangent = simplify(dy.subs(x, x0)*(x-x0)+(y.subs(x,x0)))
        tangent_intercept = solve(tangent, x)[0]                 

        lam_tan = lambdify(x, tangent, modules=['numpy'])       
        tan_y_vals = lam_tan(x_values)                          

        text.set_text("Current x-estimate:  " + str(N(tangent_intercept))) ## Display estimate

        plt.plot(x_values, tan_y_vals, 'b-')                     ## Plot our new y values with a colour of blue and a ocnsistent line
        plt.draw()                                               ## Draw the plot
        plt.pause(0.5)                                             ## Pause for 1 second before drawing the next line

        generateTangents(N(tangent_intercept), real_roots, accuracy)     ## Call itself again recursively
    else: ## Do nothing
        ## Display some ending text
        print("Found value to be: " + str(x0))
        print("With real roots: " + str(real_roots))
        pass

if __name__ == '__main__':
    ## Equation
    x = symbols('x')
    y = parse_expr(str(input("Enter Equation: ")))
    dy = diff(y, x) ## Differentiate y in terms of x

    x0 = float(input("Enter starting value for x: "))
    roots = solveset_real(y, x) ## Find roots of y in terms of x
    roots_array = [] ## Get in terms of array
    for root in roots:
        roots_array.append(N(root))


    ## Setup Values
    x_min = int(input("Enter x-axis min: "))
    x_max = int(input("Enter x-axis max: "))

    y_min = int(input("Enter y-axis min: "))
    y_max = int(input("Enter y-axis max: "))

    res = 200

    ## Convert to use with other library
    lam_y = lambdify(x, y, modules=['numpy'])   ## Functions of our main func
    lam_dy = lambdify(x, dy, modules=['numpy']) ## Differential of our eq

    ## Calculate starting values
    x_values = linspace(x_min, x_max, res)     
    y_values = lam_y(x_values)                  ## Calculated y values

    ## Graph 
    plt.axis([x_min, x_max, y_min, y_max])      
    plt.grid()                                  
    plt.ion()                                   

    ## Plot main Function
    y0_values = linspace(0,0, res)
    plt.plot(x_values, y_values, 'g-', linewidth=2)
    plt.plot(x_values, y0_values,'k-', linewidth=2) ## Create more noticable x axis
    text = plt.text(0,5,"Current x-estimate:  " + str(x0), fontsize = 30)
    plt.draw()
    plt.pause(0.1)

    
    generateTangents(x0, roots_array, 0.0000001)

   
    plt.ioff()
    plt.show()
