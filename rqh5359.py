from random import randrange
import math;

my_name = "Ryan Herman"
userid = "rqh5359"
# also name your file userid.py

def gcd(a, b):
    # Your code here
    ##234 = 81 * 2 + 72
    quo = math.floor(a / b);
    rem = a % b;
    prev = 0;

    #Precheck if b is a multiple of a
    if a%b==0:
        return b;

    #Euclidean Algorithm
    while (rem != 0):
        a = b;
        b = rem;
        #prev - stores the last remainder
        prev = b;

        quo = math.floor(a/b);
        rem = a%b;

    #return integer
    return prev;

#returns integer
def inverse(a, b):   # use extended euclidean algorithm to find inverse
    #set variables
    x0 = 0;
    x1 = 1;
    y0 = 1;
    y1 = 0;
    #Used to save initial value for later
    initialA = a;
    initialB = b;

    #Run the algorithm
    while a != 0:
        tempA = a;
        (q, a) = divmod(b, a)
        b = tempA;

        tempY0 = y0;
        y0 = y1;
        y1 = tempY0 - q * y1;

        tempX0 = x0;
        x0 = x1;
        x1 = tempX0 - q * x1;

    #Checks to see which variable is right depending on the input
    if (initialA > initialB):
        if (y0 < 0):
            y0 = y0 + initialA;
        return y0;
    if (initialB > initialA):
        if (x0 < 0):
            x0 = x0 + initialB;
        return x0;

    return 1;


def generate_key(a, b):
    # Your code here
    #Create n,k variables
    n = a * b;
    k = (a-1)*(b-1);
    RelativePrime = False;
    e = 0;

    #Runs random number until e is relatively prime to k
    while RelativePrime != True:
        e = randrange(1,k);
        if (gcd(e,k)==1):
            RelativePrime = True;

    d = inverse(e,k);

    # (e, n) is public, (d, n) is private
    # return ((e, n), (d, n))
    return ((e,n), (d,n));
    pass

def encrypt(public_key, txt):
    #Takes variables out of tuple
    e = public_key[0];
    n = public_key[1];
    #Splits up text into characters
    encryptedTxt = [char for char in txt];
    #Change value to integers then encrypt
    for i in range(len(encryptedTxt)):
        encryptedTxt[i] = ord(encryptedTxt[i]);
        encryptedTxt[i] = encryptedTxt[i] ** e;
        encryptedTxt[i] = encryptedTxt[i] % n;

    return encryptedTxt;


def decrypt(private_key, ciphers):
    # Your code here
    #Take out variables from tuple
    d = private_key[0];
    n = private_key[1];

    message = ciphers;
    stringMessage ="";

    #Decrypt the message and change it back to characters
    for i in range(len(message)):
        message[i] = message[i] ** d;
        message[i] = message[i] % n;
        message[i] = chr(message[i]);

    #Turn the character list into a string
    for x in message:
        stringMessage += x;

    #Returns the decrypted string
    return stringMessage;
