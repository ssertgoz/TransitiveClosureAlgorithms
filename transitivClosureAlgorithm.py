
import itertools

def transitiveClosureAlgorithm1(alphabet, relations):
	def find_ituples(i, member_set):
		tuple_set = set()
		for element in itertools.product(member_set, repeat=i):
			tuple_set.add(element)
		return sorted(list(tuple_set))

	reflexive_closure = set()
	alphabet = list(alphabet)
	for tupleLength in range(1, len(alphabet) + 1):
		for j in find_ituples(tupleLength, alphabet):
			if tupleLength == 1:
				reflexive_closure.add((j[0], j[0]))
			elif tupleLength == 2:
				if (j[0], j[1]) in relations:
					reflexive_closure.add((j[0], j[1]))
			else:
				indexOfTravelling = 1
				done = False
				while indexOfTravelling != tupleLength:
					if (j[indexOfTravelling - 1], j[indexOfTravelling]) in relations:
						if indexOfTravelling == tupleLength - 1:
							done = True
							break
						indexOfTravelling += 1
					else:
						break
				if done:
					reflexive_closure.add((j[0], j[tupleLength - 1]))
	print(reflexive_closure)



def transitiveClosureAlgorithm2(alphabet, relations):  
    while True:
        relations_until_now = relations | set((x,w) for x,y in relations for q,w in relations if q == y)
        if relations_until_now == relations:
            relations = relations | set((x,x) for x in alphabet)
            break
        relations = relations_until_now
    print (relations)




def transitiveClosureAlgorithm3(alphabet,relations):
    kleeneStarR = relations | set((x,x) for x in alphabet)
    for j in alphabet:
        for i in alphabet:
            for k in alphabet:
                if (((i,j) in kleeneStarR) and ((j,k) in kleeneStarR)):
                    kleeneStarR = kleeneStarR | set(set([(i,k)]))
    print(kleeneStarR)

# You can use this function to test the algorithms
# !!! you need to enter values same way as the example, otherwise algorithms dont work
print("First algorithm : ")
transitiveClosureAlgorithm1(set(["a","b","c","d","e"]),set([("a", "b"),("a", "c"),("b", "d"),("d", "e")]))
print("Second algorithm : ")
transitiveClosureAlgorithm2(set(["a","b","c","d","e"]),set([("a", "b"),("a", "c"),("b", "d"),("d", "e")]))
print("Third algorithm : ")
transitiveClosureAlgorithm3(set(["a","b","c","d","e"]),set([("a", "b"),("a", "c"),("b", "d"),("d", "e")]))