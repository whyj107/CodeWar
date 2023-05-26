# Scheduling(Round-Robin)
# https://www.codewars.com/kata/550cb646b9e7b565d600048a/train/python

# 나의 풀이
def round_robin(jobs, time_slice, index):
    result = 0
    while jobs[index] > 0:
        for idx, job in enumerate(jobs):
            tmp = min(job, time_slice)
            result += tmp
            jobs[idx] -= tmp
            if jobs[index] == 0: break
    return result


sample_test_cases = [
    ([10], 4, 0, 10),
    ([10, 20, 1], 5, 0, 16),
    ([10, 20, 1, 2, 3], 5, 0, 21)
]

for jobs, time_slice, index, expected in sample_test_cases:
    print(round_robin(jobs, time_slice, index), expected)