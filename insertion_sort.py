import random
from datetime import datetime

def randomNumArrayGen(max, length):
	arr = []
	for count in range(length):
		arr.append(int(round(random.random()*max)))
	return arr

# def insertionSort(arr):
# 	for i in range(0,len(arr)):
# 		# print i
# 		swap = "false"
# 		for n in reversed(range(0, i)):
# 			insertAt = i
# 			print "is", arr[i], "less than", arr[n]
# 			if arr[i] < arr[n]:
# 				print "Swap!"
# 				insertAt = n
# 				swap = "true"
# 		if swap == "true":
# 			#DONT SWAP PUSH IT BACK
# 			ins = arr[i]
# 			for count in range(insertAt, i+1):
# 				temp = arr[count]
# 				arr[count] = ins
# 				ins = temp
# 			print arr
# 	return arr

def insertionSort(arr):
	for i in range(len(arr)):
		tracker = 0
		for n in reversed(range(0, i)):
			print arr[i], "<", arr[n]
			if arr[i] < arr[n]:
				print "swap!"
				tracker += 1
				print arr
		startPos = i
		for k in reversed(range(tracker)):

			(arr[startPos-1], arr[startPos]) = (arr[startPos],arr[startPos-1])
			startPos-=1
	return arr





now1 = datetime.now().microsecond
# print insertionSort([2, 6, 9, 9, 7, 7, 7, 3, 2, 10])
print insertionSort(randomNumArrayGen(1000000, 100))
now2 = datetime.now().microsecond
print(str(now2 - now1) + " microseconds")
