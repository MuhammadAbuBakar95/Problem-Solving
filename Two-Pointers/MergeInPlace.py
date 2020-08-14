
def mergeInPlace(arr1, arr2):
	first_idx = 0
	second_idx = 0
	first_insert = 0
	first_len = len(arr1)
	first_items = 0
	
	
	while first_items < first_len:
		if arr1[first_idx] <= arr2[second_idx]:
			first_idx += 1
			first_items += 1
		else:
			tmp = arr1[first_insert]
			arr1[first_insert] = arr2[second_idx]
			arr2[second_idx] = tmp
			first_insert += 1
			second_idx += 1

