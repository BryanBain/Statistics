"""
Purpose: Calculate cumulative and inverse cumulative normal probability
distributions.
Date: Jun 24, 2020; Last Modified: July 9, 2020
Author: Bryan Bain
File Name: Normal_Distribution.py
"""

from scipy.stats import norm

def areaBetween(z_2, z_1):
    """
    Calculates the area between 2 z scores.
    z_2: the larger of the given z scores
    z_1: the smaller of the given z scores
    """
    return norm.cdf(z_score2) - norm.cdf(z_score1)

def areaOrValue():
    """
    Prints a selection menu for the user to choose the problem type.
    """
    print("\nPlease make your selection below.")
    print("1. You are trying to find area/probability/percent/etc.")
    print("2. You are given an area and need to find a value.")

def areaPrintout():
    """
    Prints a selection menu for the user for finding area.
    """
    print("\nPlease select the area you are trying to find.")
    print("1. Area to the left")
    print("2. Area to the right")
    print("3. Area between two values")
    print("4. Area outside two values")
    print("Press 'q' to quit")
    
def getZ():
    """
    Gets a z score input from the user.
    """
    return float(input("Please enter the z score: "))

def getLowerZ():
    """
    Gets the lower of two z scores from the user.
    """
    return float(input("Please enter the lower z score: "))

def getSampleSize():
    """Gets the sample size."""
    sample_size = int(input("What is the sample size? "))
    return sample_size

def getUpperZ():
    """
    Gets the higher of two z scores from the user.
    """
    return float(input("Please enter the upper z score: "))

def invAreaPrintout():
    """
    Prints a selection menu for the user for finding a value given an area.
    """
    print("\nPlease select the area you are given.")
    print("1. Area to the left")
    print("2. Area to the right")
    print("3. Area between two values")
    print("4. Area outside two values")
    print("Press 'q' to quit")

def obsToZ(x, mu, sigma):
    """
    Converts an observed value to its z score.
    x: the observed value
    mu: the mean
    sigma: the standard deviation
    """
    return (x - mu) / sigma

def sampleOrPopulation():
    """Determines if sample or population data is being used."""
    print("\nAre you given a sample or a population?")
    print("1. Sample")
    print("2. Population")
        

def toStdError(sigma, sample_size):
    """
    Converts standard deviation to standard error for a sample.
    sigma: the standard deviation
    sample_size: the sample size
    """
    return sigma/math.sqrt(sample_size)

def quitProgram():
    """
    Quits the program.
    """
    print("Goodbye!")
    return not quit

    
def whatGiven():
    """
    Prints a menu asking user if they are working with z scores or 
    observed values.
    """
    print("\nAre you working with z scores or observed values?: ")
    print("1. Z score")
    print("2. Observed value")
    print("Press 'q' to quit")

quit = False  

while quit is not True:
    
    whatGiven()
    z_or_obs = input().lower()
    if z_or_obs == 'q':
        quitProgram()
        break
    elif z_or_obs == "1":  # Problem involves working with z scores
        areaOrValue()
        aOrV = input()
        print()
        if aOrV == "1":  # Trying to find the area
            areaPrintout()
            z_option = input()
            print()
            if z_option == "1":  # Finding area to the left of z
                z_score = getZ()
                area = norm.cdf(z_score)
                print()
                print(f"The area to the left of z = {z_score} is {area:0.4f}")
            elif z_option == "2":  # Finding area to the right of z
                z_score = getZ()
                area = norm.sf(z_score)
                print()
                print(f"The area to the right of z = {z_score} is {area:0.4f}")  
            elif z_option == "3":  # Finding area between z scores
                z_score1 = getLowerZ()
                z_score2 = getUpperZ()
                area = areaBetween(z_score2, z_score1)
                print()
                print(f"The area between z = {z_score1} and z = {z_score2} "
                      f"is {area:0.4f}")
            elif z_option == "4":  # Finding area outside two z scores
                z_score1 = getLowerZ()
                z_score2 = getUpperZ()
                area = 1 - areaBetween(z_score2, z_score1)
                print()
                print(f"The area outside of z = {z_score1} and z = {z_score2} "
                      f"is {area:0.4f}")
                
        elif aOrV == "2":  # Trying to find a z score for a given area
            invAreaPrintout()
            z_option = input().lower()
            print()
            if z_option == "1":
                lt_area = float(input("Please enter the area (as a decimal) " 
                                      "to the left: "))
                z_score = norm.ppf(lt_area)
                print()
                print(f"z = {z_score:0.3f} has an area of {lt_area} to the left")
            elif z_option == "2":
                rt_area = float(input("Please enter the area (as a decimal) "  
                                      "to the right: "))
                z_score = norm.isf(rt_area)
                print()
                print(f"z = {z_score:0.3f} has an area of {rt_area} to the right") 
            elif z_option == "3":
                mid_area = float(input("Please enter the area (as a decimal) "
                                       "in the middle: "))
                z_scores = norm.interval(mid_area)
                print()
                print(f"The z scores are z = {z_scores[0]:0.3f} and "
                      f"z = {z_scores[1]:0.3f}")
            elif z_option == "4":
                out_area = float(eval(input("Please enter the total area "
                                       "(as a decimal) outside the middle: ")))
                z_scores = norm.interval(1 - out_area)
                print()
                print(f"The z scores are z = {z_scores[0]:0.3f} and "
                      f"z = {z_scores[1]:0.3f}")
            
    elif z_or_obs == "2":  # Problem involves working with observed values
        areaOrValue()
        aOrV = input()
        print()
        sampleOrPopulation()
        sOrP = input()
        if aOrV == "1":  # Trying to find area
            areaPrintout()
            x_option = input().lower()
            print()
            if x_option == "1":
                ob_val = float(input("Please enter the observed value: "))
                mu = float(input("Please enter the mean: "))
                sigma = float(input("Please enter the standard deviation: "))
                if sOrP == "1":
                    sampleSize = getSampleSize()
                    sigma = toStdError(sigma, sampleSize)
                z_score = obsToZ(ob_val, mu, sigma)
                area = norm.cdf(z_score)
                print()
                print(f"The area to the left of x = {ob_val} is {area:0.4f}")
            elif x_option == "2":
                ob_val = float(input("Please enter the observed value: "))
                mu = float(input("Please enter the mean: "))
                sigma = float(input("Please enter the standard deviation: "))
                if sOrP == "1":
                    sampleSize = getSampleSize()
                    sigma = toStdError(sigma, sampleSize)
                z_score = obsToZ(ob_val, mu, sigma)
                area = norm.sf(z_score)
                print()
                print(f"The area to the right of x = {ob_val} is {area:0.4f}")  
            elif x_option == "3":
                ob_val1 = float(input("Please enter the smaller observed value: "))
                ob_val2 = float(input("Please enter the larger observed value: "))
                mu = float(input("Please enter the mean: "))
                sigma = float(input("Please enter the standard deviation: "))
                if sOrP == "1":
                    sampleSize = getSampleSize()
                    sigma = toStdError(sigma, sampleSize)
                z1 = obsToZ(ob_val1, mu, sigma)
                z2 = obsToZ(ob_val2, mu, sigma)
                area = norm.cdf(z2) - norm.cdf(z1)
                print()
                print(f"The area between x = {ob_val1} and x = {ob_val2} "
                      f"is {area:0.4f}")
            elif x_option == "4":
                ob_val1 = float(input("Please enter the smaller observed value: "))
                ob_val2 = float(input("Please enter the larger observed value: "))
                mu = float(input("Please enter the mean: "))
                sigma = float(input("Please enter the standard deviation: "))
                if sOrP == "1":
                    sampleSize = getSampleSize()
                    sigma = toStdError(sigma, sampleSize)
                z1 = obsToZ(ob_val1, mu, sigma)
                z2 = obsToZ(ob_val2, mu, sigma)
                area = 1 - (norm.cdf(z2) - norm.cdf(z1))
                print()
                print(f"The area outside of x = {ob_val1} and x = {ob_val2} "
                      f"is {area:0.4f}")      
                
        elif aOrV == "2":  # Trying to find observed value given an area
            mu = float(input("Please enter the population mean: "))
            sigma = float(input("Please enter the standard deviation: "))
            invAreaPrintout()
            x_option = input().lower()
            if x_option == "1":
                lt_area = float(input("Please enter the area (as a decimal) "
                                      "to the left: "))
                obs_value = norm.ppf(lt_area, mu, sigma)
                print()
                print(f"x = {obs_value:0.3f} has an area of "
                      f"{lt_area} to the left")
            elif x_option == "2":
                rt_area = float(input("Please enter the area (as a decimal) "
                                      "to the right: "))
                obs_value = norm.isf(rt_area, mu, sigma)
                print()
                print(f"z = {obs_value:0.3f} has an area of "
                      f"{rt_area} to the right") 
            elif x_option == "3":
                mid_area = float(input("Please enter the area (as a decimal) "
                                        "in the middle: "))
                obs_values = norm.interval(mid_area, mu, sigma)
                print()
                print(f"The observed values are x = {obs_values[0]:0.3f}"
                      f" and x = {obs_values[1]:0.3f}")
            elif x_option == "4":
                out_area = float(eval(input("Please enter the total area "
                                        "(as a decimal) outside the middle: ")))
                obs_values = norm.interval(1 - out_area, mu, sigma)
                print()
                print(f"The observed values are x = {obs_values[0]:0.3f} "
                      f"and x = {obs_values[1]:0.3f}")


