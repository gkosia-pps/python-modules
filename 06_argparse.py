import argparse

parser = argparse.ArgumentParser(
                    prog='My app',
                    description='The app demo argparse module',
                    epilog='This is the epilog')


parser.add_argument('-f', '--filename',type=str,help="The filename to process",required=True)

args = parser.parse_args()

print(f"Received {args.filename} from command prompt")