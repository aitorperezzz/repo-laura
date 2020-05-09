def main():
    print('Hola Laura')
    print('Hola Aitor')
    x = calculandoCosas()
    print(x)
    print('La suma de 10 y 12 es {}'.format(calculaSuma(10, 12)))

def calculaSuma(x, y):
    return x + y

def calculandoCosas():
    return 5

if __name__ == '__main__':
    main()