#User function Template for python3
class Solution:
    def URLify(self, s):
        res=""
        for i in s:
            if i==' ' :
                res+="%20"
            else:
                res+=i
        return res
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input()
        obj = Solution()
        print(obj.URLify(str))
        print("~")

# } Driver Code Ends