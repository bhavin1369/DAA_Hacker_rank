#!/bin/python3

import os
import sys
from functools import lru_cache   # <<< THIS FIXES THE lru_cache NameError

# movement vectors
DIRS = {
    'Q': [(-1,0), (1,0), (0,-1), (0,1),
          (-1,-1), (1,1), (-1,1), (1,-1)],
    'R': [(-1,0), (1,0), (0,-1), (0,1)],
    'B': [(-1,-1), (1,1), (-1,1), (1,-1)],
    'N': [(-2,-1), (-2,1), (2,-1), (2,1),
          (-1,-2), (1,-2), (-1,2), (1,2)]
}

def inb(r, c):
    return 0 <= r < 4 and 0 <= c < 4

def next_states(pieces, opps):
    """
    pieces, opps: tuples of (type, (r, c))
    return list of (new_pieces, new_opps) for all legal moves
    """
    res = []
    for i, (t, (r, c)) in enumerate(pieces):
        if t == 'N':
            # Knights: jumps
            for dr, dc in DIRS['N']:
                nr, nc = r + dr, c + dc
                if not inb(nr, nc):
                    continue
                # can't land on own piece
                if any(pos == (nr, nc) for _, pos in pieces):
                    continue
                newP = list(pieces)
                newP[i] = (t, (nr, nc))
                # capture opponent if present
                newO = [o for o in opps if o[1] != (nr, nc)]
                res.append((tuple(newP), tuple(newO)))
        else:
            # Sliding pieces (Q, R, B)
            for dr, dc in DIRS[t]:
                nr, nc = r + dr, c + dc
                while inb(nr, nc):
                    # blocked by own piece
                    if any(pos == (nr, nc) for _, pos in pieces):
                        break
                    newP = list(pieces)
                    newP[i] = (t, (nr, nc))
                    # capture at most one opponent
                    captured = False
                    newO = []
                    for o in opps:
                        if not captured and o[1] == (nr, nc):
                            captured = True
                            continue
                        newO.append(o)
                    res.append((tuple(newP), tuple(newO)))
                    if captured:
                        break
                    nr += dr
                    nc += dc
    return res

def whiteQueenDead(W):
    return not any(t == 'Q' for t, _ in W)

def blackQueenDead(B):
    return not any(t == 'Q' for t, _ in B)

@lru_cache(None)
def solve_state(W, B, depth, maxd, white_turn):
    """
    W, B: tuples of (type, (r, c))
    depth: moves played so far
    maxd: maximum allowed moves
    white_turn: True if white to move
    returns True if White can force a win from this state
    """
    W = list(W)
    B = list(B)

    if blackQueenDead(B):
        return True
    if whiteQueenDead(W):
        return False
    if depth == maxd:
        return False

    if white_turn:
        moves = next_states(tuple(W), tuple(B))
        for W2, B2 in moves:
            if solve_state(W2, B2, depth + 1, maxd, False):
                return True
        return False
    else:
        moves = next_states(tuple(B), tuple(W))
        # If Black has no moves, White eventually wins
        if not moves:
            return True
        for B2, W2 in moves:
            # Black wants to prevent White's win
            if not solve_state(W2, B2, depth + 1, maxd, True):
                return False
        return True

def simplifiedChessEngine(whites, blacks, moves):
    # Clear memo between games
    solve_state.cache_clear()

    def col(c):
        return ord(c) - ord('A')

    W = []
    for s in whites:
        t, c, r = s.split()
        W.append((t, (int(r) - 1, col(c))))

    B = []
    for s in blacks:
        t, c, r = s.split()
        B.append((t, (int(r) - 1, col(c))))

    Wt = tuple(W)
    Bt = tuple(B)

    can_win = solve_state(Wt, Bt, 0, moves, True)
    return "YES" if can_win else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(sys.stdin.readline().strip())
    for _ in range(g):
        w, b, m = map(int, sys.stdin.readline().split())
        whites = [sys.stdin.readline().strip() for __ in range(w)]
        blacks = [sys.stdin.readline().strip() for __ in range(b)]
        result = simplifiedChessEngine(whites, blacks, m)
        fptr.write(result + '\n')

    fptr.close()
