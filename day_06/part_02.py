with open('input.txt','r') as file:
    signal = list(file.readlines()[0])
    step = 14

    for i in range(len(signal)-step):
        fours = signal[i:i+step]
        fours_unique = list(set(signal[i:i+step]))
        
        if len(fours) == len(fours_unique):
            print(i+step)
            break

