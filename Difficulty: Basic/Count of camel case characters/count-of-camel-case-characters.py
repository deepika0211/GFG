#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        c=0
        for i in s:
            if i.isupper():
                c+=1
        return c
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends