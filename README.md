### [Connect 4 game](https://www.mathsisfun.com/games/connect4.html)

### How to run the program

    python <program>

Clear instructions will be provided while you play.

* As far as the heuristic is considered, I’m calculating the score for the intermediate states as the tree cannot reach the leaf node in every branch.  
* I’m looking if there are any moves where the computer can move aggressively rather than being in the defense state. For this continuous 3-4 coins of the same player are checked before making a move.

### Alphabeta pruning

It’s just a small condition where alpha and beta are initialized and updated as we move through the branches, but this ignores the unnecessary branches which doesn't lead to a better move.

    And when alpha>=beta we no longer need to go through the other
    branches from that particular node.
In the code, as it is hard to go till the leaf nodes, I’m looking only till 6 steps ahead, it takes for normal minimax algorithm to make a move, whereas alpha beta pruning does it in no time. You can change the depth to 4 to immediately see the move of the computer.

### Analysis
I tried a lot but couldn’t beat the program. Please let me know if you can break the code, so that there is still a possibility to make the heuristic better.
As far as my friends and me tried, computer won 100% times.

### Run time
* Initially when there are almost no coins on the board,
simple minimax algorithm with a depth of 6 took almost 12sec to output a move whereas the alphabeta pruning algorithm just took 4sec.
* We can see a significant amount of decrease in the run time for the algorithm. It’s an indication of how many branches it avoided.
