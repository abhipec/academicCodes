def calculateInversions(data):
	'''	returns number of inversions in a string or a list
		not optimized algo for large string/list length'''
	inversion = 0
	for idx, val in enumerate(data):
		for val2 in data[idx+1:]:
			if val2 != 'X' and str(val2) < str(val):
				inversion += 1
	return inversion

def swap(data, idx1, idx2):
	'''	returns a string with content at location idx1 and idx2 swapped
		if idx1 is greater than idx2 swap them to maintain integrity'''
	if idx1 > idx2:
		tmp = idx1
		idx1 = idx2
		idx2 = tmp
	return data[0:idx1] + data[idx2] + data[idx1+1:idx2] + data[idx1] + data[idx2+1:]