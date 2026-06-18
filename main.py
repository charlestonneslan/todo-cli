from store import load_tasks, write_tasks
from commands import parser

def main():
    load_tasks()
    args = parser.parse_args()
    args.func(args)
    write_tasks()

if __name__ == "__main__":
    main()

