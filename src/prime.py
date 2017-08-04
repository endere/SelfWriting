import primedict


def get_prime(index):
    try:
        return primedict.primes[index]
    except KeyError:
        with open('primedict.py', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for i in lines:
                if i != '}':
                    file.write(i)
                else:
                    file.write('4:5, \n')
                    file.write('}')
            file.truncate()
            file.close()




if __name__ == '__main__':
    for i in range(1, 6):
        print(get_prime(i))