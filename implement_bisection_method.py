def square_root_bisection(number, tolerance=0.1, iterations=10):
    if number <0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number==0 or number==1:
        print(f"The square root of {number} is {number}")
        return number
    elif number >0:
        low = 0
        high = max(1.0,number)

        for _ in range(iterations):
            mid = (low+high)/2

            if abs(number - (mid**2)) <= tolerance:
                print (f"The square root of {number} is approximately {number**0.5}")
                return number**0.5
                
            if mid**2 < number:
                low = mid
            elif mid**2 > number:
                high = mid
            
        print(f"Failed to converge within {iterations} iterations")
        return None
