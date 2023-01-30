import random
#Generalization of problem from https://gilkalai.wordpress.com/2017/09/07/tyi-30-expected-number-of-dice-throws/

def simulate(prior=[2,4],win=[6],n=6.,ntrials=10000):
    timelimit = 100
    limit = 30

    rolls = [0]*limit
    trials = 0 
    random.seed(a=None, version=2)

    for i in range(0,ntrials):
        t = 0
        k = 0
        r = random.randint(1,n)
        while((r not in win) and t<limit and k<timelimit): 
            if r in prior:
                t += 1     
            else:
                t = 0
            r = random.randint(1, n)
            k += 1
        if k<timelimit:
            trials += 1
        rolls[t] += 1
    return rolls,trials
    
def print_results(rolls,trials):
    print("Total Trials:",trials)
    for i in range(0,15):
        percent = rolls[i]/trials
        print("Number of Rolls with Length of ", i+1 , ":",rolls[i],",Percentage of Trials:","{0:.2%}".format(percent))
        
    expected = 0.0
    for i in range(0,len(rolls)):
        percent = rolls[i]/trials
        expected += percent*(float(i)+1.0)
    print("Expected Value: ","%.6f"%expected)

