def make_shirt(size, printing_message):
    """Summarizing information about a shirt"""
    
    print(f"The shirt size is: {size}.")
    print(f"The message that should be printed on the shirt is:\n {printing_message.title()}.")
#make_shirt('medium', 'teamwork makes the dream work')
make_shirt(printing_message= 'no pain, no gain', size= 'large')
