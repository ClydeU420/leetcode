def longestPalindrome(self, s: str) -> str:

    length=len(str)
    if length<2:
        return str
    dp=[[None *length]*length]
    for y in range(length):
        for x in range(y):

            dp[x][y]=str[x]==str[y] and (y-x<3 or dp[x+1][y-1])
    
        

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()