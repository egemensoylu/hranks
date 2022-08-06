names = []
for N_itr in range(N):
    #first_multiple_input = input().rstrip().split()
    first_multiple_input = lines[N_itr].rstrip().split()

    firstName = first_multiple_input[0]
    emailID = first_multiple_input[1]

    if emailID.split('@')[-1] == 'gmail.com':
        names.append(firstName)


print(sorted(names))