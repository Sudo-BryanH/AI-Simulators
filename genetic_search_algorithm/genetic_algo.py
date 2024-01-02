import numpy as np

# each individual with properties [A-G]
current_pop = [[1,1,1,1,1,1,1,1],
[2,2,2,2,2,2,2,2],
[3,3,3,3,3,3,3,3],
[4,4,4,4,4,4,4,4],
[1,2,3,4,1,2,3,4],
[4,3,2,1,4,3,2,1],
[1,2,1,2,1,2,1,2],
[3,4,3,4,3,4,3,4]
]


# checks constraints for each individual
def constraintCheck(p):
    '''
    The function to check constraints
    '''
    count = 0
    met_constraints = []
    

    if  (p[6] < p[0]):
        # print("A > G", p[6], p[0])
        count += 1
        met_constraints.append(1)
    if  abs(p[6] - p[2]) == 1:
        # print("|G – C| = 1", p[6], p[2])
        count += 1
        met_constraints.append(2)
    if  p[2] != p[3]:
        # print("D != C", p[3], p[2])
        count += 1
        met_constraints.append(3)
    if  p[6] != p[5]:
        # print("G != F", p[6], p[5])
        count += 1
        met_constraints.append(4)
    if  abs(p[4] - p[5])%2 != 0:
        # print("|E – F| is odd", p[4], p[5])
        count += 1
        met_constraints.append(5)
    if  (p[0] <= p[7]):
        # print("A ≤ H", p[0], p[7])
        count += 1
        met_constraints.append(6)
    if  abs(p[7] - p[2]) %2 == 0:
        # print("|H – C| is even", p[7], p[2])
        count += 1
        met_constraints.append(7)
    if  p[4] != p[2]:
        # print("E != C", p[4], p[2])
        count += 1
        met_constraints.append(8)
    if  p[5] != p[7]:
        # print("H != F", p[7], p[5])
        count += 1
        met_constraints.append(9)
    if  abs(p[5] - p[1]) == 1:
        # print("|F – B| = 1", p[5], p[1])
        count += 1
        met_constraints.append(10)
    if  p[7] != p[3]:
        # print("H != D", p[7], p[3])
        count += 1
        met_constraints.append(11)
    if  p[4] < p[3] - 1:
        # print("E < D – 1", p[4], p[3])
        count += 1
        met_constraints.append(12)
    if p[2] != p[5]:
        # print("C != F", p[2], p[5])
        count += 1
        met_constraints.append(13)
    if  p[6] < p[7]:
        # print("G < H", p[6], p[7])
        count += 1
        met_constraints.append(14)
    if  p[3] >= p[6]:
        # print("D ≥ G", p[3], p[6])
        count += 1
        met_constraints.append(15)
    if  p[4] != p[7] - 2:
        # print("E != H – 2", p[4], p[7])
        count += 1
        met_constraints.append(16)
    if  p[3] != p[5] - 1:
        # print("D != F – 1", p[3], p[5])
        count += 1
        met_constraints.append(17)
    
    return count, met_constraints



def calc_prob(scores):
    '''
    calculate the probabilities of each individual to be chosen for repdudction. Prints out the continuous distribution for each individual to be chosen
    '''
    denom = sum(scores)
    sum_so_far = 0
    scores_norm = []
    probs = []
    

    for i in scores:
        
        prob_param = (sum_so_far, sum_so_far+i/denom)
        sum_so_far+=i/denom
        scores_norm.append(prob_param)
        probs.append(round(i/denom, 3))
    return [(round(a[0], 3), round(a[1], 3)) for a in scores_norm], probs

def find(prob, norm_score):

    for i, p in list(enumerate(norm_score)):
        if prob > p[0] and prob < p[1]:
            return i


def pairings(world, norm_scores):
    '''
    Determine the pairs or individuals to pair together and mutate. Prints mutations and pairings
    '''
    char_map = {
        0:"A", 
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
        6:"G",
        7:"H"
    }
    newresults = []
    for i in range(4):
        one = np.random.rand(1)
        two = np.random.rand(1)
        at = np.random.randint(1, 8)

        m1 = np.random.randint(1, 8)
        m2 = np.random.randint(1, 4)
        m3 = np.random.randint(1, 8)
        m4 = np.random.randint(1, 4)
        
        print(f"{char_map[find(one, norm_scores)]}, {world[find(one, norm_scores)]}, {char_map[find(two, norm_scores)]}, {world[find(two, norm_scores)]}, at: {at}")
        print(f"mutate {char_map[find(one, norm_scores)]} at {m1 + 1} to {m2}")
        print(f"mutate {char_map[find(two, norm_scores)]} at {m3 + 1} to {m4}")
    
        a1 = world[find(one, norm_scores)][0:at]
        a2 = world[find(one, norm_scores)][at:]
        b1 = world[find(two, norm_scores)][0:at]
        b2 = world[find(two, norm_scores)][at:]
        a = a1 + b2
        a[m1] = m2
        b = b1 + a2
        b[m3] = m4
        newresults.append(a)
        newresults.append(b)

    return newresults





def genetic_algo(population, attempts):
    '''
    Main genetic search algorithm function:
    '''
    world = population
    scores = []
    iter = attempts

    while iter != 0:
        for i in world:
            count, met = constraintCheck(i)
            print(i, "meets", count, "of 14 constraints")
            if count == 14:
                print("This world meets all constraints:", i)
                return i
            scores.append(count)

        norm, reg = calc_prob(scores)
        print(norm, reg)
        world = pairings(world, norm)
        print("New worlds:", world)
        scores = []
        iter-=1
    
    print("not found in", attempts, "mutations")

if __name__ == '__main__':
    genetic_algo(current_pop, 10)

