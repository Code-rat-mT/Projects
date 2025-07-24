from numpy import linspace
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from sympy.solvers.solveset import solveset, solveset_real

import matplotlib.pyplot as plt
#from numpy.doc.constants import lines

def distanceFromRoot(x, values):  ## Return the lowest distance between the supplied roots
    currentDistance = abs(x-values[0])

    if len(values) > 1:  ## Only run if there is more than one root

        for value in values:
            newDist = abs(x-value)
            if newDist < currentDistance:
                currentDistance = newDist

    return currentDistance
#Here's something cooler. A graphical simulation of Newton's method. Pretty Amatuer though

def generateTangents(x0, real_roots, accuracy):
    if distanceFromRoot(x0, real_roots) > accuracy: ## Continue if the value we have calculated is still too far from a real root
        tangent = simplify(dy.subs(x, x0)*(x-x0)+(y.subs(x,x0))) ## Find equation of tangent at our x0
        tangent_intercept = solve(tangent, x)[0]                 ## Find tangent's x intercept

        lam_tan = lambdify(x, tangent, modules=['numpy'])        ## Function to generate y values of the tangent line
        tan_y_vals = lam_tan(x_values)                           ## Y values of the tangent line to plot

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
    x_values = linspace(x_min, x_max, res)      ## Array of x values between xmin and max seperated by res
    y_values = lam_y(x_values)                  ## Calculated y values

    ## Graph Setup
    plt.axis([x_min, x_max, y_min, y_max])      ## Setup graph axis
    plt.grid()                                  ## Enable the graph grid
    plt.ion()                                   ## Make graph interactive to add future lines

    ## Plot main Function
    y0_values = linspace(0,0, res)
    plt.plot(x_values, y_values, 'g-', linewidth=2)
    plt.plot(x_values, y0_values,'k-', linewidth=2) ## Create more noticable x axis
    text = plt.text(0,5,"Current x-estimate:  " + str(x0), fontsize = 30)
    plt.draw()
    plt.pause(0.1)

    ## Start generating tangent lines! weo
    generateTangents(x0, roots_array, 0.0000001)

    ## Keep the graph from disappearing
    plt.ioff()
    plt.show()