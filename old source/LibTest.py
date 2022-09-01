import numpy as np

def main():
    print("")
    a = np.array([2.0001])
    b = np.array([0.1])
    c = np.array([0])
    c = a + b
    print(c)
    print(2.0001+0.1)
    print(type(c[0]))
    print(np.arange(1,5,1))

if __name__ == "__main__":
    main()
