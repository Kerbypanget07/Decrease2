# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:31:22 2023

@author: Kervy
"""
def alternate_glasses(glasses):
    filled = []
    empty = []

    for i, glass in enumerate(glasses):
        if glass == "filled":
            filled.append(i)
        else:
            empty.append(i)

    result = [None] * len(glasses)
    for i in range(0, len(glasses), 2):
        result[i] = "filled"
    for i in range(1, len(glasses), 2):
        result[i] = "empty"

    moves = 0
    for i in range(len(filled)):
        result.insert(0, result.pop(empty[i] + moves))
        moves += 1
        result.append(result.pop(filled[i] + moves))
        moves += 1

    return result, moves

def get_glasses_input():
    n = int(input("Enter the number of glasses (n): "))
    glasses = ["filled"] * n + ["empty"] * n
    return glasses

# Main function
def main():
    glasses = get_glasses_input()
    result, moves = alternate_glasses(glasses)
    print("Initial state:", glasses)
    print("Final state:", result)
    print("Number of moves:", moves)

if __name__ == "__main__":
    main()
