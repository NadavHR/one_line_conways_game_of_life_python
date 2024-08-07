import os, time
# memory clear clears stdout
# memory init initializes field
# memory update updates the field
# memory field is [field]
# memory print prints the field
# memory run_generations starts running generations
# memory start starts the game
memory = {'clear': lambda: (os.system("cls")),
          'init': lambda mem: mem['field'].append(*(
                ([([[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]] * 10) +
                ([[0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]] * 10)]))),
          'update': lambda mem: (field := mem['field'][0],
                                 new_field := [[0 if (sum([field[(y + i - 1) % 20][(x + j - 1) % 20]
                                    for j in range(3) for i in range(3)]) - field[y][x]) <= 1
                                    or (sum([field[(y + i - 1) % 20][(x + j - 1) % 20]
                                    for j in range(3) for i in range(3)]) - field[y][x]) >= 4
                                    else 1 for x in range(len(field[y]))] for y in range(len(field))],
                                 mem['field'].clear(),
                                 mem['field'].append(new_field)),
          'print': lambda mem: (field := mem['field'][0],
                                print("\n".join(["".join('#' if j == 1 else ' ' for j in i) for i in field]))),
          'run_generations': lambda mem: (mem['clear'](), mem['print'](mem), time.sleep(1), mem['update'](mem), mem['run_generations'](mem)),
          'start': lambda mem: (mem['init'](mem), (lambda mem: [mem['run_generations'](mem) for _ in iter(int, 1)])(mem)),
          'field': []}
memory['start'](memory)
