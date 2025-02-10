from pantograph.server import Server

def parse_tactics():
    tactics = [ # Example tactic, same as autoformalize.py
        "intro p q h",
        "rcases h with hp | hq",
        "right",
        "exact hp",
        "left",
        "exact hq"
    ]
    return tactics

if __name__ == '__main__':
    server = Server(project_path="./")
    state = server.goal_start("forall (p q: Prop), Or p q -> Or q p")

    i = 0

    tactics = parse_tactics()

    while not state.is_solved:
        prev_state = state
        print(f"state{i}: {state} \n")
        tactic = tactics.pop(0)

        try:
            new_state = server.goal_tactic(state, goal_id=0, tactic=tactic)
            i+= 1
            state = new_state

        except Exception as e:
            tactics.append(tactic)
            print(e)
            state = prev_state
