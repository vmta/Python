def bouquets(narcissus_price, tulip_price, rose_price, summ):
	bouquets = 0
	
	nFlowers = int(summ // narcissus_price)
	rFlowers = int(summ // rose_price)
	
	for i in range(nFlowers + 1):
		nValue = i * narcissus_price
		
		for j in range(rFlowers + 1):
			rValue = j * rose_price
			bValue = nValue + rValue
			
			if summ >= bValue:
				tulips = int((summ - bValue) // tulip_price)
				
				if tulips%2 == 0 and (i + j)%2 == 0:
					bouquets = bouquets + tulips//2
				else: 
					bouquets = bouquets + tulips//2 + 1
	return bouquets

				

print "=== TEST START ==="
print bouquets(1,1,1,3) # 34

print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556

print "==== TEST END ===="

exit(0)