mid, score_mid = input().split()
fin, score_fin = input().split()
edu, score_edu = input().split()

score = float(mid) * int(score_mid) + float(edu) * int(score_edu) + float(fin) * int(score_fin)

print('%.1f' %score)