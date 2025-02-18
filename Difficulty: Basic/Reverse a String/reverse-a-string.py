#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        return s[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        
        ob = Solution()
        print(ob.revStr(s))
        print("~")
# } Driver Code Ends