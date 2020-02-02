from math import log2

"""
    A (d_1, ..., d_n) detecting matrix is a 0-1 matrix of size kxn
    whose corresponding linear transform is injective
    on the product set of the {0, ..., d_i-1}.

    Moreover its inverse can be computed in polynomial time.
"""

def hamming_weight(a):
    s = 0
    while a > 0:
        s += a % 2
        a //= 2
    return s

def get_evaluations(a, b, log_k):
    ans = []
    for x in range(1 << log_k):
        cur = 1
        for i in range(log_k):
            if (a >> i) & 1 and ((b >> i) & 1) == ((x >> i) & 1):
                cur = 0
        ans.append(cur)
    return ans

def check_precondition(d, log_k):
    n = len(d)
    lhs = (log_k - 2) * 2 ** (log_k - 1)
    rhs = (2 ** log_k) * log2(d[n - 2 ** log_k - 1])
    for i in range(n - 2 ** log_k):
        rhs += log2(d[i])
    print(log_k, lhs, rhs)
    return lhs <= rhs

def find_log_k(d):
    n = len(d)
    log_k = 2
    last = -1
    while (1 << log_k) < n:
        if check_precondition(d, log_k):
            last = log_k
        log_k += 1
    #if check_precondition(d, log_k - 1):
    #    print("IT GOES BEYOND")
    #    exit(0)
    if last == -1:
        return log_k + 1
    print("we found one!")
    print(last)
    return last

def construct_detecting_matrix(d):
    # d1 <= ... <= dn
    # todo: check preconditions on log_k
    log_k = find_log_k(d)
    n = len(d)
    k = 2 ** log_k

    if k > n:
        print("todo implement this")
        return []
    M = [[0] * n for i in range(k)]
    r = 0
    for a in range(k):
        ub = 2 ** (hamming_weight(a) - 1)
        prod = 1
        b = a
        subsz = 0
        l = 0
        print("a = ", a, "prod*d[r] = ", prod*d[r], "ub = ", ub, sep = " ")
        while r < n - k and prod * d[r] <= ub:
            if l > 0:
                for lin in range(k):
                    M[lin][r] = M[lin][r - 1]
            print("heloooo", r, n-k)
            while subsz < prod:
                if hamming_weight(b) % 2 == 0:
                    cur = get_evaluations(a, b, log_k)
                    #print("normal mode we put ", a, b, hamming_weight(b), cur, sep = " ")
                    for lin in range(k):
                        M[lin][r] += cur[lin]
                    subsz += 1
                b = (b - 1) & a
            prod *= d[r]
            r += 1
            l += 1
        print("fill ", n-k+a, sep=" ")
        cur = get_evaluations(a, l, log_k)
        if l > 0:
            #print("WE INIT")
            for lin in range(k):
                M[lin][n - k + a] = M[lin][r - 1]
        while subsz < prod:
            if hamming_weight(b) % 2 == 0:
                cur = get_evaluations(a, b, log_k)
                #print("add the function ", a, b, cur, sep = " ")
                for lin in range(k):
                    M[lin][n - k + a] += cur[lin]
                subsz += 1
            b = (b - 1) & a
    return M

def comp(M, u):
    n = len(M)
    m = len(u)
    ans = [0] * n
    for i in range(n):
        cur = 0
        for k in range(m):
            cur += M[i][k] * u[k]
        ans[i] = cur
    return ans

d = [2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8]
cur = [0] * len(d)
M = construct_detecting_matrix(d)
seen = {}
print(M)


def gen(d, cur, i = 0):
    if i >= len(d):
        tmp = tuple(comp(M, cur))
        if tmp in seen:
            print("wooooow")
            print(tmp, cur, seen[tmp])
        seen[tmp] = cur[:]
        return
    for j in range(d[i]):
        cur[i] = j
        gen(d, cur, i + 1)


#gen(d, cur)


