# Tic-Tac-Toe
This is a python program for Tic-Tac-Toe.


Main function is invoked from [play_game()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L158).

Once [play_game()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L28) function is invoked, the game board is displayed by [display_board()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L21) function and X's turn is asked as input from [handle_turn()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L48) function.

In [handle_turn()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L48) the player's input is validated and assigned to the board. After updating the players are fliped using [flip_player()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L98)and the updated board is displayed awaiting the other player input .

For every move [check_if_game_over()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L77) checks whether the game is over (some one won or tied) or not


[check_if_win()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L82) checks if its any match in rows or columns or diagonals and if there is any match, then [game_still_going](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L113) is set to False and the match ends

[check_if_tie()](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L90) checks if the moves are over and if the moves are over, then [game_still_going](https://github.com/alyysa/Tic-Tac-Toe/blob/9b0278a0e7bf5fbb3aba44f25464398774c379db/main.py#L94) is set to False and the match ties




