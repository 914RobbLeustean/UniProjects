"""def SumOfKNaive(S, n, k):
    if k == 0:
        return [] #We found a subset that has the sum of K, we return an empty list
    if n == 0 and k != 0:
        return None #We ran thru all elements in S and we haven't found 
                    #a subset with sum of K 

    if S[n - 1] > k: #Checking if the element we're on is larger than the sum
        return SumOfKNaive(S, n - 1, k) #If so, then we skip it since it wouldn't fit

    curr = SumOfKNaive(S, n - 1, k - S[n - 1]) #Include the current element and subtract it
    if curr is not None:                       #from the target sum 
        return curr + [S[n - 1]]
    else:
        return SumOfKNaive(S, n - 1, k) #Exclude the current element and
                                        #continue the search 

   #If any of these calls return a valid subset, we return the result                                       

S = [2, 3, 5, 7, 8]
k = 12
rez = SumOfKNaive(S, len(S), k)

if rez:
    print("Subset that sums to", k, "is:", rez)
else:
    print("No subset found that sums to", k)
    """



def SumofKDP(S, k):
    n = len(S)
    dp = [[False for _ in range(k + 1)] for _ in range(n + 1)] #Matrice with n+1 rows
                                                               #and k+1 columns,each elem.
                                                               #of the row meaning a 
                                                               #possible sum
   #All values of dp initialized as false since no calculations have been done yet

    for i in range(n + 1): #Initializing all the values of the first column as True
        dp[i][0] = True #Cause its possible to be an empty subset(with a sum of 0) for any 
                                                                              #set in S

    for i in range(1, n + 1):
        for j in range(1, k + 1): #nested loop to check if the curr elem. is < = j
            if S[i - 1] > j:
                dp[i][j] = dp[i - 1][j] #If curr elem. is > than the sum,we cant include it  
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - S[i - 1]]
                #the curr elem can potentially be included, so we check if it's possible
                #to obtain the sum with or without including the curr elem. in the subset
    print("Dynamic Programming Matrix:")
    for row in dp:
        print(row)
 
    if not dp[n][k]:
        return None #We look for a valid subset in dp, if not then we return none

    rez = [] #We have a valid subset so we will store the values in rez
    i, j = n, k #We want to backtrack thru dp starting from the last cell
    while i > 0 and j > 0: #cond:as long as the sum is positive and theres elems. left in S
        if dp[i][j] and not dp[i - 1][j]: 
            rez.append(S[i - 1]) #We add the element thats apart of the subset to the result
            j -= S[i - 1] #Subtract the element we added from the sum
        i -= 1 #backtracking by moving to the previous row

    return rez
  
S = [3, 5, 7, 8]
k = 10
rez = SumofKDP(S, k)

if rez:
    print("Subset that sums to", k, "is:", rez)
else:
    print("No subset found that sums to", k)

