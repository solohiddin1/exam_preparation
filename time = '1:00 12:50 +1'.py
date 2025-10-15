n = int(input())

def check(n):
	if n <=1:
		return 0
if n <= 1:
	check(n)

l = [int(input()) for _ in range(n)]
opp = 0
for i in range(0,n):
	for j in range(i+1,n):
		if l[j] > l[i]:
			opp += 1
print(opp)



n = int(input())

if n <= 1:
	print(0)
	exit()
l = [int(input()) for _ in range(n)]

opp = sum(1 for i in range(1,n) if l[i] > l[0])
print(opp)

# departure = input().strip()
# arrival = input().strip()
# timezone = int(input().strip())

# departure = int(departure.split(":")[0]) * 60 + int(departure.split(":")[1])
# arrival = int(arrival.split(":")[0]) * 60 + int(arrival.split(":")[1])

# arrival -= timezone * 60

# t = arrival - departure

# if t < 0:
#     t += 24 * 60

# h = t // 60
# m = t % 60
# print(f"{h}:{m:02d}")

# # departure = input('departure time -> ')
# # arrival = input('arrival time -> ')
# # timezone = input("timezone -> ")

# # try:
# #     timezone = int(timezone)
# #     if timezone < -12 or timezone > 14:
# #         raise ValueError("Timezone difference must be between -12 and +14.")
# #     departure = int(departure.split(":")[0]) * 60 + int(departure.split(":")[1])
# #     arrival = int(arrival.split(":")[0]) * 60 + int(arrival.split(":")[1]) - timezone * 60
    
# # except ValueError:
# #     print("Invalid time format. Please use HH:MM.")
# #     exit(1)

# # t = arrival-departure
# # if t < 0:
# #     t += 24 * 60
# # print("t = ", t)
# # h = t // 60
# # m = t % 60
# # res = f"{h}:{m:02d}"
# # print(f"res = {res}")