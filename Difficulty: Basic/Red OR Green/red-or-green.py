#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        c=0
        d=0
        for i in S:
            if i=="R":
                c+=1
            else:
                d+=1
        if d<c:
            return d
        return c
                
            
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
        print("~")
# } Driver Code Ends