
data = print("       ")

opening = input("Input:")


if opening.endswith('?'):
    print("This is known as a question or a sarcastic statement. ")

if opening.endswith('.'):
    print("""This is known as a statement or a probability(46%) of
          mispunctuate. """)
    
if opening.endswith('!'):
    print("""This is known as a exclamation or a probability(21%) of
          incomplete or inaccurate grammar.""")