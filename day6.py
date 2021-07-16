# Day 6 - Let's Review

# Enter your code here. Read input from STDIN. Print output to STDOUT
def rearrange(word):
    left = ""
    right = ""
    for i in range(0,len(word)):
        if i%2 == 0:
            left += word[i]
        else:
            right += word[i]
    print(f"{left} {right}")
        
    
    
T = int(input().strip())
for i in range(0,T):
    rearrange(input())
    
    
