from random import randint
import matplotlib.pyplot as plt

def calcFitness(payoff_matrix,num_doves, num_hawks):
    total = num_doves + num_hawks
    cum_dove_score = 0 # Cumulative dove score
    cum_hawk_score = 0

    while(total > 0):
        # Generate random strategies for each player
        p1_strategy = 0 if randint(1, total) <= num_doves else 1
        p2_strategy = 0 if randint(1, total) <= num_doves else 1

        # Decrement number of remaining strategies to be considered
        if p1_strategy == 0:
            num_doves -= 1
        else:
            num_hawks -= 1

        if p2_strategy == 0:
            num_doves -= 1
        else:
            num_hawks -= 1

        # Compute Player 1 strategy's fitness and add to cumulative score
        p1_fitness = payoff_matrix[p1_strategy][p2_strategy]
        if (p1_strategy == 0):
            cum_dove_score += p1_fitness
        else:
            cum_hawk_score += p1_fitness

        # Compute Player 2 strategy's fitness and add to cumulative score
        p2_fitness = payoff_matrix[p2_strategy][p1_strategy]
        if (p2_strategy == 0):
            cum_dove_score += p2_fitness
        else:
            cum_hawk_score += p2_fitness


        total = num_doves + num_hawks
        if (total == 0):
            break

    return 200*(cum_dove_score/(cum_dove_score+cum_hawk_score)), 200*(cum_hawk_score/(cum_dove_score+cum_hawk_score))

# def normalize_helper(total, val1, val2):
#     return (val1 / (val1 + val2))*total, (val2 / (val1 + val2))*total

def runGenerationalAlgo(num_generations, init_dove_pop, init_hawk_pop, payoff_matrix):
    dove_pop = init_dove_pop
    hawk_pop = init_hawk_pop
    generation_pops = [(dove_pop, hawk_pop)]
    for i in range(num_generations):
        cum_dove_score, cum_hawk_score = calcFitness(payoff_matrix, 100, 100)
        dove_pop = cum_dove_score 
        hawk_pop = cum_hawk_score 

        generation_pops.append((dove_pop, hawk_pop))
    return generation_pops


def main():
    payoff_matrix = [[.5,0],[1,.2]]
    
    generation_props = runGenerationalAlgo(50, 100, 100, payoff_matrix)
    for i in generation_props:
        print(i)

    #plot the proportion of hawks and doves in the population
    dove_list = [x[0] for x in generation_props]
    hawk_list = [x[1] for x in generation_props]
    plt.plot (dove_list)
    plt.plot (hawk_list)
    plt.ylabel('Population')
    plt.xlabel('Generations')
    plt.show()
if __name__ == "__main__":
    main()