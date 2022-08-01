# import click
#
# @click.command()
# @click.argument('numbers', nargs=-1)
# @click.option('--shedule')
# def fancy_command(shedule):
#     result = sum(int(s) for s in numbers)
#     print('Numbers sum: {}. Word: {}'.format(result, word))
#
# if __name__ == '__main__':
#     fancy_command()


# import argparse
#
# def some_function(target, end="!"):
#     """Some example funcion"""
#     msg = "hi " + target + end
#     print(msg)
#
#
# def start():
#     # All the logic of argparse goes in this function
#     parser = argparse.ArgumentParser(description='Say hi.')
#     parser.add_argument('target', type=str, help='the name of the target')
#     parser.add_argument('--end', dest='end', default="!",
#                     help='sum the integers (default: find the max)')
#
#     args = parser.parse_args()
#     some_function(args.target, end=args.end)
#
# if __name__ == '__main__':
#   start()
#
# # def main():
# #   print("Ok")
#
# # if __name__ == '__main__':
# #   main()