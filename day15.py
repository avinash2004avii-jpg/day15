#TASK--1 THE SAMPLE SPACE MAP
import random
random.seed(2)

actions = ['Click','Scroll','Exit']

sample_space = []
for i in actions:
    for j in actions:
        sample_space.append((i,j))
print("sample_space")     
print(sample_space)
clicks = []
for x in sample_space:
    if 'Click' in x:
        clicks.append(x)
event_E = [outcome for outcome in sample_space if "Click" in outcome]

print("\nEvent E (At least one Click):")
print(event_E)
probability = len(clicks) / len(sample_space)
print(f'probability of the event "Clicks" where the customer clicks at least once : {probability:.2f}')

# rolling two dice 1,000 times and calculate the experimental probability of the sum being 7
count = 0
rolling_trails = 1000

for i in range(rolling_trails):
    sample1 = random.randint(1,6)
    sample2 = random.randint(1,6)
    if sample1 + sample2 == 7:
        count += 1
       
print(f'Probability of the sum being 7 : {count/rolling_trails}')

#TASK--2 THE LOGIC OF DEPENDENCY

coin_tossed_head = 1/2
dice_rolling_6 = 1/6
print(f'P(A) * P(B) : {coin_tossed_head * dice_rolling_6 :.3f}')

#finding probability without Replacement
red = 5
blue = 5
picking_1st_marble = red / (red+blue)
picking_2st_marble = (red-1)/(red+blue-1)

prob = picking_1st_marble * picking_2st_marble
print(f'probability that both are Red without Replacement : {prob:.2f}')

      



































































