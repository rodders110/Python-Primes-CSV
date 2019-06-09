import csv

nums = []
candidates = []
primes = []

with open('numList.csv', 'r') as numList:
    numsItems = list(csv.reader(numList))


    for row in numsItems:
        for num in row:
            nums.append(int(num))
    # print(nums)
numList.close()

def isPrime():
    global nums
    prime = nums[0]
    while len(nums) >= prime:
        prime = nums[0]
        for item in nums:
            if item % prime != 0:
                candidates.append(item)
        primes.append(prime)
        nums.clear()
        for no in candidates:
            nums.append(no)
        candidates.clear()


    for item2 in nums:
        primes.append(item2)


isPrime()

with open('primeNumbers.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(primes)
writeFile.close()



