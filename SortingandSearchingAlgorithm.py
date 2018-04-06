#JOHN DAVE B. FUERTE

#Sorting and Searching Algorithm

#github.com/rameeeen23

#johndavefuerte@gmail.com

def reading_sort(array1, max_val):
    dave = max_val + 1
    count = [0] * dave

    for ainz in array1:
        #count occures
        count [ainz] += 1
    i = 0
    for ainz in range(dave):
        for l in range (count[ainz]):
            array1[i] = ainz
            i += 1
    return array1

print (reading_sort( [1,2,7,3,2,1,4,2,3,2,5,1,4,5,5,4,6],7))
