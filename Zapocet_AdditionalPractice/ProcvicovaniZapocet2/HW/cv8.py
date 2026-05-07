def fib(n: int) -> int:
    if n >=2: 
     return fib(n-1)+fib(n-2)
    if n ==1:
       return 1
    if n==0:
       return 0

def fib_mem(n: int, lookup: dict[int, int]) -> int:
    if n in lookup:
       return lookup[n]
    if n >=2: 
        lookup[n] = fib_mem(n-1,lookup)+fib_mem(n-2,lookup)
        return lookup[n]
    if n==1:
       lookup[1] = 1
       return lookup[1]
    if n==0:
       lookup[0] = 0
       return lookup[0]
    
def fib_bottom(n: int) -> int:
   nums=[0,1]
   for i in range(n):
      nums.append(nums[i]+nums[i+1])
   return nums[n]

def knapsack(data:str, maxTime: int):
   rating = []
   time = []
   with open(data,"r",encoding="utf-8") as f:
      for line in f:
         line.strip().split(" ")
         rating.append(line[0])
         time.append(line[1])


'''def fib_noList(n: int) -> int:
   f1=0
   f2=1
   for i in range(1,n):
    f3_prev=f3
    f3 = f1+f2
    f1 = f2
    f2 = f3_prev
   return f3
'''
def main():
    lookup = {}
    data = "./08-knapsack/data/songs.txt"
    print(f"{fib(10)}")
    print(f"{fib_mem(50,lookup)}")
    print(f"{fib_bottom(10)}")
    print(f"{fib_bottom(50)}")
    #print(f"{fib_noList(0)}")
    knapsack(data)

if __name__ == "__main__":
    main()