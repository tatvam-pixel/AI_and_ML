import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	if len(a)*len(a[0]) != new_shape[0]*new_shape[1]:
		return []
	mat = [[] for _ in range(new_shape[0])]
	row = []
	for i in range(len(a)):
		for j in range(len(a[i])):
			row.append(a[i][j])

	count = 0
	for i in range(len(row)):
		if (i) % new_shape[1] == 0 and i!=0:
			count+=1
			mat[count].append(row[i])
		else:
			mat[count].append(row[i])
	
	


	return mat