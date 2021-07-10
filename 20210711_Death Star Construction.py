# Death Star Construction
# https://www.codewars.com/kata/5a996f3d5084d73a7100040c/train/python

# 나의 풀이
# 철 100, 강철 75, 크롬 50
def death_star(week, attack):
    r = [100, 75, 50]
    for i in range(attack):
        for j in range(3):
            r[j] -= week[i][j]
            if r[j] < 0: r[j] = 0
    result = f'The station is destroyed! It needed {r[0]} iron, {r[1]} steel and {r[2]} chromium for completion.'
    return result if sum(r) != 0 else 'The station is completed!'

# 다른 사람의 풀이
def death_star1(week, attack):
    iron = sum(w[0] for w in week[:attack])
    steel = sum(w[1] for w in week[:attack])
    chromium = sum(w[2] for w in week[:attack])

    if (iron>=100 and steel>=75 and chromium>=50):
        return 'The station is completed!'
    else:
        return f'The station is destroyed! It needed {max(0, 100-iron)} iron, {max(0, 75-steel)} steel and {max(0, 50-chromium)} chromium for completion.'

print(death_star([[100, 75, 49],
                  [20, 15, 20],
                  [10, 15, 10],
                  [50, 50, 20],
                  [20, 15, 10],
                  [20, 15, 10],
                  [20, 15, 10]], 1),
      'The station is destroyed! It needed 0 iron, 0 steel and 1 chromium for completion.')
print(death_star([[20, 15, 10],
                  [20, 15, 20],
                  [10, 15, 10],
                  [50, 50, 20],
                  [20, 15, 10],
                  [20, 15, 10],
                  [20, 15, 10]], 5),
      'The station is completed!')