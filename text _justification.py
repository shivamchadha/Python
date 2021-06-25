#!/usr/bin/env python
# coding: utf-8

import sys



def length(wordLengths, i, j):
    return sum(wordLengths[i- 1:j]) + j - i + 1


def breakLine(text, L):
    
    # wl = lengths of words
    wl = [len(word) for word in text.split()]
    # n = number of words in the text
    n = len(wl)   
    
    # total badness of a text l1 ... li
    m = dict()
    
    # initialization
    m[0] = 0    

    # auxiliary array
    s = dict()

    # the actual algorithm
    for i in range(1, n + 1):
        sums = dict()
        k = i
        while (length(wl, k, i) <= L and k > 0):
            sums[(L - length(wl, k, i))**3 + m[k - 1]] = k
            k -= 1
        m[i] = min(sums)
        s[i] = sums[min(sums)]
        
    #splitting by working backwords
    
    breaks = []
    while n > 1:
        
        breaks.append(s[n])
        n = s[n] - 1
    breaks.reverse()
    return breaks



def reconstruct_text(words,breaks):                                                                                                                
    i = 0 
    text = []
    
    words = words.split()
    while True:
        if i== len(breaks)-1:
            start = breaks[i]-1
            text.append(' '.join((words[start:])))
            break
        start = breaks[i]-1
        end = breaks[i+1]
        text.append(' '.join((words[start:end])))
        
        i+=1
    print('\n'.join(text)) 
    return 


def main():
    L = 70
    text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumyeirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diamvoluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stetclita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'


    if len(sys.argv) == 1:    
        reconstruct_text(text,breakLine(text,L))

    elif len(sys.argv) == 2:
        L = int(sys.argv[1])
        reconstruct_text(text,breakLine(text,L))

    elif len(sys.argv) == 3:
        L = int(sys.argv[1])
        f = open(sys.argv[2], 'r')
        text = f.read()
        f.close()
        reconstruct_text(text,breakLine(text,L))
    else:
        print('Bad input. /n Provide Line Lenght and text file or just line lenght or run with defualt parameters')

if __name__ == "__main__":
    main()



