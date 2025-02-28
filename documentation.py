"""
    Coinbase's proof of work (PoW) algorithm can be found around line 150 in
    https://login.coinbase.com/e_C1Tp-yCr.js
    
    In this project, I fully reversed their implementation of it :)
    
    The hash format according to the Coinbase PoW algorithm is:
    HC:::nonce:::suffix
    
    Where:
    HC is a constant
    Nonce is a hashed string we get from get_nonce()
    Suffix is a random string we have to bruteforce
    
    The suffix format: letter, number or letter, number or letter, number, number (e.g., A1B23)
    
    Disclaimer: I am not responsible for any damage that may be caused by
    using this code. Use at your own risk. 
    
    This code was written by @
"""

import hashlib
import random
import time
import string

# hash dat bitch lol
def calculate_sha256(input_str):
    hash_obj = hashlib.sha256(input_str.encode())
    return hash_obj.hexdigest()

def is_valid_hash(hash_str):
    """
    check if the hash is valid according to the matching function
    function(x){ return x.slice(0, 6).split('').every((char) => char === x[0]) }
    """
    if len(hash_str) < 6:
        return False
    first_char = hash_str[0]
    for i in range(1, 6):
        if hash_str[i] != first_char:
            return False
    return True

# bruteforce the suffix
def generate_suffix(nonce):
    print("Generating the suffix...")
    random.seed(int(time.time() * 1000))  # Seed the random number generator
    letters = string.ascii_letters
    alphanumeric = string.ascii_letters + string.digits
    numeric = string.digits

    while True:
        # generate the 5-character suffix
        sf = [
            random.choice(letters),           # 1st character: letter
            random.choice(alphanumeric),      # 2nd character: letter or number
            random.choice(alphanumeric),      # 3rd character: letter or number
            random.choice(numeric),           # 4th character: number
            random.choice(numeric)            # 5th character: number
            # these values are true every time
        ]
        
        # as seen in HC:::nonce:::suffix
        combined = nonce + ''.join(sf)
        
        # hash dat bitch
        hash_str = calculate_sha256(combined)
        
        # DID WE DO IT???????
        if is_valid_hash(hash_str):
            return ''.join(sf)

def solution(nonce, suffix):
    return f'HC:::{nonce}:::{suffix}'


def main():
    nonce = "q8qD4BSX1zdrlRuhQ/8SliQFkB8FoS5HFP0futr49VhNVC9WggIiPjsUGfbTqx6ZZPfttK2KI2hMgDX3X4UsfLexM7XRS4saA2dqilirx+libtY2kZpKGV4YY0DfXPwaQHP57Z1qSnmgs/zAL1Aam4hKORHefMPP+MepuYcZZ1orZ53zmEbid9zlvnMaTcx+6sAt7NRYuXgI4NWgf89C3tE+n9nufc7rBgqDcrpfOaYoWQDcxTSblfGkzLMMVE6Pk9b77s5JVGli4Oioz4Uvpp3y34vspbOf1+fgCf5lTKFeKKwDEEEjjcZQfhyiEM1x1AXTwaNA3aM/MjZaCq8="
    suffix = generate_suffix(nonce)
    print("Generated suffix:", suffix)  # Example output: "b1q90"
    
# main()
