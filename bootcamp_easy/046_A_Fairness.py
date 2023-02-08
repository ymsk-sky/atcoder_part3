s = input()
N, W, S, E = s.count("N"), s.count("W"), s.count("S"), s.count("E")
if (N > 0 and S == 0) or (S > 0 and N == 0) or (W > 0 and E == 0) or (E > 0 and W == 0):
    print("No")
else:
    print("Yes")
