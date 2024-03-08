def make_shirt(printing_message,size='large'):
    """Information about a t-shirt."""
    print(f"The shirt size is: {size}")
    print(f"The message that should be printed on the shirt is:\n{printing_message.title()}.")

#make_shirt('I love python')
#make_shirt('i love python',size= 'medium')
make_shirt('knowledge is power', 'small')