"""
Loop Slicer

Using a loop to iterate through a list, 
print off a slice of a list each iteration

[1, 2, 3, 4, 5] ->
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]

"""

def loop_slicer(lst):

    for i in range(len(lst)):
        print(lst[i:])

loop_slicer([1,2,3,4,5])
if __name__ == "__main__":
    loop_slicer([1,2,3,4,5])