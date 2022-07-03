import argparse
import sys

def calc(args):
    if args.o =='add':
        return args.X + args.y
    elif args.o =='mul':
        return args.X * args.Y
    elif args.o =='sub':
        return args.X - args.Y
    elif args.o =='div':
        return args.X / args.Y

    else:
        return 'something went wrong'

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--X",type=float,default=1.0,
    help="Enter first number: this is a utility for calculation. please contact harry bhai")

    parser.add_argument("--Y",type=float,default=1.0,
    help="Enter second Number: this is a utility for calculation. please contact harry bhai")

    parser.add_argument("--o",type=str,default=1.0,
    help="this is a utility for calculation. please contact harry bhai")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))