import random


#this functin creates the individual chromosomes that populate the generation
def createIndividualChromosome(chromosomeLength): #generates chromosome
    chromosome = ""
    chromosomeFitness = 0
    for i in range(chromosomeLength):
        code = random.randint(0,1)
        chromosomeFitness += code
        chromosome = chromosome + str(code)
    return chromosome,chromosomeFitness

#populates array with chromosome
def createPopulation(popSize,chromosomeLength): 
  #sends population size and length of chromosmes 
  totalPopulationFitness = 0
  populationCount = 0
  population = []
  fittest = []
  secondFittest = []
  for i in range(popSize):
      chromosome = createIndividualChromosome(chromosomeLength)
      totalPopulationFitness += int((chromosome[1]))
      populationCount += 1
      population.append(chromosome)     
  population = sorted(population,key=lambda x: x[1],reverse = True)    
  return (population)

# function test poplulation to get overall fitness value
def testPopulation(population,popSize):
  TPF = 0
  index = 0
  for i in range(popSize):
    TPF += population[index][1] 
    index += 1
  return (int(TPF))


 #function makes selection of fittest individuals  
def selection(population):
  # make sure population is sorted to easily pick top two
  SortedPop = sorted(population,key=lambda x: x[1],reverse = True) #rever sorted 
  fittest = SortedPop[0]
  secondFittest = SortedPop[1]
  return (fittest,secondFittest)

#function acually does the single crossoverpoint 
def crossover(topC):
  chromList = []
  #probability for crossover point to happen 
  if random.randint(0,9) in range(0,2):
   
   string1, string2 = topC[0]
   string3, string4 = topC[1]
   FirstFitOff = string1[::2] +  string3[::-2]
   SecondFitOff = string3[::2] +  string1[::-2]
   chromList.append(FirstFitOff)
   chromList.append(SecondFitOff)
  
  else:
    chromList.append(topC[0][0])
    chromList.append(topC[1][0])
  return chromList

 #function that does random mutaion on random mutation point to help stop termination of chromsomes failing to progress
def Mutation(crossResults,chromosomeLength):
 fitcount1 = 0
 fitcount2 = 0
 index = 0
 index2 = 0
 string1 = (crossResults[0])
 string2 = (crossResults[1])
 listString1 = list(string1)
 listString2 = list(string2)
 i = 0

 while i < 1:
   #random point in chromosome list
  mutationPoint = random.randint(0,chromosomeLength-1)
  i += 1
  if random.randint(0,9) in range(0,3):
   if listString1[mutationPoint] == '0':
    listString1[mutationPoint] = '1'
 
   if listString2[mutationPoint] == '0':
    listString2[mutationPoint] = '1'
  
 for i in range(chromosomeLength):
  #checks for 1 in the chromosome length is specified so it matches indicated length
  if '1' in listString1[index]:
    
    fitcount1 += 1
    index += 1
  else:
    index += 1
 
#checks again for second string
  if '1' in listString2[index2]:
    
    fitcount2 += 1
    index2 += 1
  else:
    index2 += 1


 if fitcount1 > fitcount2:
   # join them again to make them strings
   bestfit = ["".join(listString1),fitcount1] #
 else:
   bestfit = ["".join(listString2),fitcount2]

 return bestfit

#run function
def runGA(popSize,chromosomeLength,runs):
  #popSize = 100
  #chromosomeLength = 20
  #goalFitness = 0
  f= open("GeneticAlgorithm.txt","w+")
  bestfit = [0,0]
  generationt = 0
  gencount = 1
  runs = 0
  print("Genetric Algroithm Practice")
  print('Author: Harold Sullivan')
  print('created: May 11 2019')
  print('###########################################################')
  population = createPopulation(popSize,chromosomeLength)
  while runs < 50 :
    totalPoplulationFitness = testPopulation(population,popSize)
    topC = selection(population)
    crossResults = crossover(topC)
    bestfit = Mutation(crossResults,chromosomeLength)
    #print(population)
    population.pop()
    #print(population)
    #print(bestfit)  
    population.append(bestfit)
    population = sorted(population,key=lambda x: x[1],reverse = True)#print(population)

    #print(population)

    
    #print(population.append(bestfit))
    #print(population)
    a = generationt
    b = bestfit[1]
    c = totalPoplulationFitness/popSize
    runs +=1
    generationt += 1
    
    print('Generation:',a,'Best Fitness: ',b,'Average fitness: ',round(float(c),2))

    f.write("%s  Best Fitnes: %s Average Fitness: %s \n " % (a, b, round(float(c),2)))
  f.close()
    #print('generation: ',a,'best Fitness: ',b,'avg Fitness: ',c)
   
     
#popSize = 100
#chromosomeLength = 20
#goalFitness = 0   
runGA(100,20,50)
print('###########################################################')

print("result saved in text file")


