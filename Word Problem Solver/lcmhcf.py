import math

def find_lcm(numbers):
    # Function to calculate LCM of two numbers
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm(lcm_result, numbers[i])

    return lcm_result

def find_hcf(numbers):
    # Function to calculate HCF of two numbers
    def hcf(x, y):
        return math.gcd(x, y)

    hcf_result = numbers[0]
    for i in range(1, len(numbers)):
        hcf_result = hcf(hcf_result, numbers[i])

    return hcf_result

# Example usage:
'''numbers = [12, 18, 24]
lcm_result = find_lcm(numbers)
hcf_result = find_hcf(numbers)
print(f"LCM: {lcm_result}")
print(f"HCF: {hcf_result}")
'''