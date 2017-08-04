import primedict


def get_prime(index):
    """Check primedict's dictionary and return nth prime. 

    If not there, finds all primes up until n and permenantly writes them into dictionary, before returning nth prime. 
    The first time using this function with a fresh dictionary will take substantially longer, but then go to an instant lookup time.
    """
    try:
        return primedict.primes[index]
    except KeyError:
        new_primes = []
        num = primedict.primes[max(primedict.primes)]
        while len(new_primes) + len(primedict.primes) < index:
            num += 2
            try:
                for key in primedict.primes:
                    1 / (num % primedict.primes[key])
                for other_prime in new_primes:
                    1 / (num % other_prime)
                new_primes.append(num)
            except ZeroDivisionError:
                pass
        with open('primedict.py', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for i in range(len(lines)):
                if lines[i] != '}':
                    file.write(lines[i])
            for x in range(len(new_primes)):
                file.write('{}:{}, \n'.format(len(lines) + x - 1, new_primes[x]))
            file.write('}')
            file.truncate()
            file.close()
        return new_primes[-1]




if __name__ == '__main__':
    # for i in range(1, 6):
    #     print(get_prime(i))
    print(get_prime(10))