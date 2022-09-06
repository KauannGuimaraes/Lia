# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
steps = {}
def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)
  number=7
  move = "R"
  if len(opponent_history) > number:
    pattern = join(opponent_history[-number:])
    if join(opponent_history[-(number + 1):]) in steps.keys():
      steps[join(opponent_history[-(number + 1):])] += 1
    else:
      steps[join(opponent_history[-(number + 1):])] = 1
    possible = [pattern + "R", pattern + "P", pattern + "S"]
    for i in possible:
      if not i in steps.keys():
        steps[i] = 0
    predict = max(possible, key=lambda key: steps[key])
    if predict[-1] == "P":
      move = "S"
    if predict[-1] == "R":
      move = "P"
    if predict[-1] == "S":
      move = "R"
  return move
def join(moves):
  return "".join(moves)