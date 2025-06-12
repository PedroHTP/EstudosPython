def main():
    X = list(map(int, input()))

    if X[1] == X[2] and X[2] == X[3]:
        msg = '*'
    else:
        if X[1] != X[2] and X[1] != X[3]:
            msg = 'A'
        elif X[2] != X[3] and X[2] != X[1]:
            msg = 'B'
        else:
            msg = 'C'
    print(msg)   
    
if __name__ == "__main__":
    main()
