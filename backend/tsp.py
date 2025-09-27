import graph
import random

MAX_VALUE = 2147483647

class TSP:
    def __init__(self, graph, start, generations = 100):
        self.graph = graph

        self.genes = ""
        nodes = list(self.graph.nodes)
        for i in range(len(nodes)):
            self.genes += nodes[i]

        self.pop_size = 10
        self.genomes = []
        self.population = []
        self.start = start
        self.generations = generations
        self.keep_amount = 3


    def create_genome(self):
        '''
        Description: Creates a random path starting and ending at the designated starting node
        INPUT: self
        OUTPUT: a path starting and ending at self.start. Randomly choosing unique genes from self.genes
        '''
        genes = self.genes.replace(self.start, "")
        genome = f"{self.start}"
        for _ in range(len(genes)):
            index = int(random.random() * len(genes))
            genome += genes[index]
            genes = genes[:index] + genes[index + 1:]
        genome += self.start

        return genome
    
    def create_population(self):
        '''
        Description: Creates self.pop_size genes
        INPUT: self
        OUTPUT: none
        '''
        for _ in range(self.pop_size):
            self.population.append(self.create_genome())
    
    def path_length(self, genome):
        '''
        Description: The fitness function, counts up path_lengths
        INPUT: genome - The path starting and ending at self.start
        OUTPUT: The sum of the path lengths in genome
        '''
        total = 0
        for i in range(len(self.genes)):
            key = genome[i]
            nextKey = genome[i+1]
            subdict = self.graph.edges.get(key, -1)
            if subdict == -1:
                return MAX_VALUE
            
            length = subdict.get(nextKey, MAX_VALUE)
            if length == MAX_VALUE:
                return MAX_VALUE
            total += length
        return total
    
    def mutation(self, genome):
        '''
        Description: Randomly swaps 2 nodes in the genome
        INPUT: genome - a string representing the path
        OUTPUT: the genome with 2 random nodes (not start or end) swapped
        '''
        indices = random.sample(range(1, len(genome)-1), 2)
        min_index = min(indices)
        max_index = max(indices)

        genome = genome[:min_index] + genome[max_index:max_index + 1] + genome[min_index + 1:max_index] + genome[min_index: min_index + 1] + genome[max_index+1:]

        return genome
    
    def choose(self, fitness_func):
        '''
        Description: Randomly choose a parent weighted by how fit it is
        INPUT: fitness_func - a function to calculate the fitness of a gene
        OUTPUT: a single randomly chosen parent to mutate'''
        return random.choices(
            population=self.population,
            weights=[1/fitness_func(genome) for genome in self.population])[0]
    
    def evolution(self):
        '''
        Description: Randomly chooses a parent, mutates it, and returns it
        INPUT: self - path_length
        OUTPUT: the child with a randomly mutated path
        '''
        parent = self.choose(self.path_length)
        child = self.mutation(parent)
        
        return child



    def run_tsp(self):
        self.create_population()

        self.population = sorted(self.population, 
                                key = lambda genome: self.path_length(genome))

        n = 0

        for n in range(self.generations):
            
            next_gen = self.population[0:self.keep_amount]

            for _ in range(self.pop_size - self.keep_amount):
                child = self.evolution()
                next_gen.append(child)

            self.population = sorted(next_gen, 
                                    key = lambda genome: self.path_length(genome))
            

        print(self.population)
        print([self.path_length(item) for item in self.population])
        print(f"After {n+1} generations, the shortest path found is:")
        print(self.population[0])
        print("Weight:", self.path_length(self.population[0]))
        return self.population[0]

    
        

# edges = (
#     ('A', 'B', 5),
#     ('B', 'A', 6),
#     ('B', 'C', 3),
#     ('C', 'A', 7))

#https://www.researchgate.net/figure/TSP-Solution-The-figure-2-shows-the-TSP-solution-for-this-graph-The-integer-optimal_fig2_274371114
# edges = (
#     ('A', 'F', 16),
#     ('A', 'E', 9),
#     ('B', 'A', 12),
#     ('B', 'F', 15),
#     ('B', 'C', 19),
#     ('C', 'B', 19),
#     ('C', 'D', 21),
#     ('D', 'B', 12),
#     ('D', 'E', 10),
#     ('D', 'F', 16),
#     ('E', 'D', 10),
#     ('E', 'F', 10),
#     ('F', 'A', 16),
#     ('F', 'B', 15),
#     ('F', 'C', 17),
#     ('F', 'D', 16))

#https://hotcore.info/act/kareff-072024p.html
edges = (('A', 'B', 2),
    ('A', 'C', 1),
    ('A', 'D', 1),
    ('A', 'E', 1),
    ('B', 'A', 2),
    ('B', 'C', 2),
    ('B', 'D', 1),
    ('B', 'E', 1),
    ('C', 'A', 1),
    ('C', 'B', 2),
    ('C', 'D', 1),
    ('C', 'E', 1),
    ('D', 'A', 1),
    ('D', 'B', 1),
    ('D', 'C', 1),
    ('D', 'E', 2),
    ('E', 'A', 1),
    ('E', 'B', 1),
    ('E', 'C', 1),
    ('E', 'D', 2))


g = graph.Graph(edges)
tsp = TSP(g, 'E', generations = 100)
answer = tsp.run_tsp(False)
g.plot_graph(False)
g.draw_tsp(answer)

