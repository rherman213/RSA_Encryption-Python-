from rqh5359 import *

if __name__ == '__main__':

    q1_a1 = [22, 43, 89, 16, 13]
    q1_a2 = [11, 87, 267, 62, 17]
    q1_ans = [11, 1, 89, 2, 1]

    for i in range(5):  # testing 22 and 11, 43 and 87,... and so on
        if gcd(q1_a1[i], q1_a2[i]) != q1_ans[i]:
            print("incorrect GCD for ", q1_a1[i], q1_a2[i], ". Should be ", q1_ans[i])
    print("Test cases passed for GCD")



    q2_a1 = [2, 12, 109]
    q2_a2 = [3, 11, 101]
    for i in range(3):
        ans = inverse(q2_a1[i], q2_a2[i])
        if ((q2_a1[i] * ans)%q2_a2[i] != 1):
            print("incorrect inverse for input ", q1_a1[i], q1_a2[i], " since ans * ", q2_a1[i], " != ", q2_a2[i] )
    print("Test cases passed for Extended GCD")

    primes1 = [13, 19, 23, 29]
    primes2 = [17, 31, 37, 41]
    for i in range(4):
        public, private = generate_key(primes1[i], primes2[i])
        e, n = public
        d, n = private
        check1 = (primes1[i]*primes2[i] == n)
        if (not(check1)):
            print("n is incorrect")
        k = (primes1[i] - 1)*(primes2[i] - 1)
        if (gcd(e, k) != 1):
            print("Something is incorrect. gcd(e, k) must be equal to 1")
        if (not(1 < e < k)):
            print("Something is wrong. e must be between 1 and k")
        if ((d*e)%k != 1):
            print("Something is incorrect. d * e mod k must be equal to 1")

    p1 = 13
    p2 = 17
    public, private = generate_key(p1, p2)
    e, n = public
    d, n = private
    print("encrypting abcdefghijklmnopqrstuvwxyz: ")
    lst = encrypt(public, "abcdefghijklmnopqrstuvwxyz")
    print(lst)
    print()
    print("decrypting: ")
    txt = decrypt(private, lst)
    print(txt)
    if (txt != "abcdefghijklmnopqrstuvwxyz"):
        print("something wrong. decrepting an encrypted value must give same string")
