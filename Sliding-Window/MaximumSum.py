# Find maximum possible sum for K consecutive elements in an array
# Subarray of size K with maximum possible sum size

def MaxPossibleSum(arr, k):

	if len(arr) < k:
		return 0

	start = 0
	end = 0
	window_sum = 0
	
	while end < k:
		window_sum += arr[end]
		end += 1
	
	maximum = window_sum
	while end < len(arr):
		window_sum += arr[end]
		window_sum -= arr[start]
		maximum = max(window_sum, maximum)
		start += 1
		end += 1

	return maximum

arr = [300, 200, 400, 100, 500, 10]
k = 3

print MaxPossibleSum(arr, k)