class Solution(object):
    
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        
        flag=0
        med=(m+n)//2+1
        if (m+n)%2==1:
            flag=1
        if n==0 and flag==1:
            return nums1[med-1]
        if n==0 and flag==0:
            return float(nums1[med-2]+nums1[med-1])/2
        if m==0 and flag==1:
            return nums2[med-1]
        if m==0 and flag==0:
            return float(nums2[med-2]+nums2[med-1])/2
        n1=0
        n2=0
        lastnum=0
        if(nums1[0]>nums2[0]):
            lastnum=num=nums2[0]
            n2+=1
        else:            
            lastnum=num=nums1[0]            
            n1+=1
        s=1
        print(med)
        if(s==med):
            return float(nums1[0]+nums2[0])/2
        else:
            while(s!=med):            
                lastnum=num
                if n1+1>m:
                    num=nums2[n2]
                    n2+=1
                elif n2+1>n:
                    num=nums1[n1]
                    n1+=1
                else:
                    if nums1[n1]>nums2[n2]:                                                 
                        num=nums2[n2]
                        n2+=1           
                    else:                              
                        num=nums1[n1]
                        n1+=1         
                s+=1
            if flag==1:
                print("n1:{}".format(n1))
                print("n2:{}".format(n2))
                print(lastnum)
                return num            
            else:
                print("n1:{}".format(n1))
                print("n2:{}".format(n2))
                print(lastnum)
                print(num)
                return (float(lastnum)+float(num))/2            

# def main(): 
#     nums1=[1]
#     nums2=[]
#     so=Solution
#     print(so.findMedianSortedArrays(so,nums1,nums2))
# if __name__=="__main__": 
#     main() 