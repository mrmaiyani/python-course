dictionary = {} # this called empty dictionary
marks = {
    'radhe':100,
    'utsav':51,
    'meet':71
}
print(marks['utsav'])

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({'radhe':101,'utsav':100,'suhali':82})
print(marks)
print(marks.get('krishn'))  #get gives none
print(marks['krishn'])  # give return error