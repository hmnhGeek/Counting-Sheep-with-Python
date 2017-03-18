from sleep import *
sleep = sleep()


def readfrom(input_file, output_file):
    f = open(input_file)
    lines = f.readlines()
    f.close()
    
    i = 0
    f = open(output_file, 'w')
    test_cases = lines[0]
    cases = lines[1:]

    if int(test_cases) in range(1, 101):
        for case in cases:
            
            if int(case) in range(0, 10**6 + 1):
                print 'Case #'+str(i+1)+': '+ sleep.start(int(case))
                f.write('Case #'+str(i+1)+': '+ sleep.start(int(case))+'\n')
                i+=1

    f.close()

def run():

    cmd = raw_input('sleep> ')
    l = cmd.split(' ')

    input_file = l[0]
    output_file = l[1]

    try:
        readfrom(input_file, output_file)
    except:
        run()

    run()


run()
