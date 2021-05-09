import math
def szerkeszthető_e(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        print("Egyik érték sem lehet negatív szám vagy nulla")
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        print("A háromszög nem szerkeszthető meg! (Bármely két oldal összegének nagyobbnak kell lenie a harmadik oldalnál)")
        return False
    else:
        return True

def háromszög_kerület(a: float, b: float, c: float) -> float:
    kerület: float = a + b + c
    return kerület


def háromszög_terület(a: float, b: float, c: float) -> float:
    s: float = (a + b + c) / 2
    terület: float = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return terület


def különleges_e (a: float, b: float, c: float) -> None:
    if a * a + b * b == c * c or c * c + b * b == a * a or a * a + c * c == b * b:
        print("A háromszög derékszögű!")
    if a == b or a == c or b == c:
        if a == b == c:
            print("A háromszög egyenlő oldalú!")
        else:
            print("A háromszög egyenlő szárú!")


def main() -> None:
    print("Háromszög kerület terület számítás")
    print("")
    print("Az adatokat cm-ben adja meg")

    a = float(input("Adja meg a háromszög a oldalát:"))
    b = float(input("Adja meg a háromszög a oldalát:"))
    c = float(input("Adja meg a háromszög a oldalát:"))
    if szerkeszthető_e(a, b, c):
        kerület: float = round(háromszög_kerület(a, b, c), 2)
        terület: float = round(háromszög_terület(a, b, c), 2)
        print(f"A háromszög kerülete: {kerület} cm")
        print(f"A háromszög területe: {terület} cm²")
        különleges_e(a, b, c)


if __name__ == '__main__':
    main()
