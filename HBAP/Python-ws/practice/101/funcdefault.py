import json


def get_me(parm1, parm2=3):
    return round(parm1 / parm2, 2)


def main():
    res = {a: get_me(a) for a in range(10)}
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
