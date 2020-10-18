# Start at 20.
# Divide by 7, 8, 9, 10, 11, 12.

# Search space starts at 20. Goes up by 10. (Outer)

#for x in range(20,30001,10):
for x in range(10, 100, 1):



# Inner loop does modulo (division test (8%2=0  7%3=1)).

    if x%7!=0:
        break
    else:
     #   if x%8 !=0:
      #      break
       # else:
        print (x)

  
  
# then make it work for 7 AND 8