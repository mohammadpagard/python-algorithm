num = input("")

def number_printer(number: str):
    if len(number) <= 100:
        for n in number:
            yield '{}: {}'.format(n, n*int(n)) 

for i in number_printer(num):
    print(i)


problem_link = "https://quera.org/problemset/9774?tab=description"
