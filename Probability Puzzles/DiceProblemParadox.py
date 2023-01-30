import random
#Generalization of problem from https://gilkalai.wordpress.com/2017/09/07/tyi-30-expected-number-of-dice-throws/


prior = [1,3,5]
win = [6]
a = 1
b = 6

trials = 50000
timelimit = 100
limit = 30

successful_rolls = [0]*limit
successful_trials = 0 
random.seed(a=None, version=2)

for i in range(0,trials):
    t = 0
    k = 0
    r = random.randint(a, b)
    while((r not in win) and t<limit and k<timelimit): 
        if r in prior:
            t += 1     
        else:
            t = 0
        r = random.randint(a, b)
        k += 1
    if k<timelimit:
        successful_trials += 1
    successful_rolls[t] += 1

print("Total Trials:",trials)
for i in range(0,15):
    percent = successful_rolls[i]/successful_trials
    print("Number of Rolls with Length of ", i+1 , ":",successful_rolls[i],",Percentage of Trials:","{0:.2%}".format(percent))
    
expected = 0.0
for i in range(0,len(successful_rolls)):
    percent = successful_rolls[i]/successful_trials
    expected += percent*(float(i)+1.0)
print("Expected Value: ","%.6f"%expected)

