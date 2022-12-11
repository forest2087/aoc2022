partOneStrategy = {
  "A Y": "win",
  "B Z": "win",
  "C X": "win",
  "A X": "draw",
  "B Y": "draw",
  "C Z": "draw",
  "A Z": "lose",
  "B X": "lose",
  "C Y": "lose",
}

partOnePoints ={
  "X": 1,
  "Y": 2,
  "Z": 3,
  "lose": 0,
  "draw": 3,
  "win": 6,
}

partTwoStrategy = {
  "X": { "A": "scissors", "B": "rock", "C": "paper" }, # lose
  "Y": { "A": "rock", "B": "paper", "C": "scissors" }, # draw
  "Z": { "A": "paper", "B": "scissors", "C": "rock" }, # win
}

partTwoPoints = {
  "rock": 1,
  "paper": 2,
  "scissors": 3,
  "X": 0,
  "Y": 3,
  "Z": 6,
}

def solv1(f):
    score = 0
    while True:
        ln = f.readline().strip()
        if not ln:
            break
        
        a, b = ln.split(' ')
        score+=partOnePoints[partOneStrategy[a+' '+b]]+partOnePoints[b]
        # print(a, b, score)
    
    print(score)
    
def solv2(f):
    score = 0
    while True:
        ln = f.readline().strip()
        if not ln:
            break
        
        a, b = ln.split(' ')
        score+=partTwoPoints[partTwoStrategy[b][a]]+partTwoPoints[b]
        # print(a, b, score)
    
    print(score)
    