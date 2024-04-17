idx = 3
seq = [0,0,1]
for i in range(40):
  seq.append(seq[idx-1]+seq[idx-2]+seq[idx-3])
  idx += 1
rq_idx = int(input())-1
print(seq[rq_idx])
