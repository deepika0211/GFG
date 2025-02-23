#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        a=""
        for i in S:
            if 'A'<=i<='Z':
                a+=chr(ord('Z')-(ord(i)-ord('A')))
            elif 'a'<=i<='z':
                a+=chr(ord('z')-(ord(i)-ord('a')))
            else:
                a+=i
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.reciprocalString(S))
        print("~")
# } Driver Code Ends