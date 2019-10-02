def sqrt(x):

    #Intital guess
    z = 1.0
    #Keep getting a better estimate for the square root of x,
    #until you are within two decimal places
    while abs(z*z - x) > 0.01:
    #Get a better aproximation for the sqr root
        z -= (z*z -x) / (2*z)
    #Returns z
    return z

#Get the sqr rt of 8 and print it
z = sqrt(8.0)
#Print z
print(z)
#Print the square of the square of z
print(z*z)