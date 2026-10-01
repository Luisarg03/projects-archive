
def pares(limite):

	num=1

	while num<limite:

		yield num*2

		num+=1

almacenpares=pares(10)

for i in almacenpares:

	print(i)