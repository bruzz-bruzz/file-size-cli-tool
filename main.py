import argparse
from pathlib import Path
parser = argparse.ArgumentParser(description="Greet a user")
parser.add_argument('-d',"--dir", help="Name of the person to greet",default=Path.cwd(),type=Path)
args = parser.parse_args()
print(args)
p = Path(args.dir or '/')
print(p.stat().st_size)
print(p.resolve())