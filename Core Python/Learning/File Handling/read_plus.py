with open('Core Python/Demos/File Handling/intro3.txt','r+') as fp:
    
    print(fp.tell())

    fp.seek(0,2) # Manually Change
    ####Whench
    # 0 - beginning
    # 1 - current
    # 2 - end

    print(fp.tell())

    fp.write('\n333333')

    fp.seek(0, 0)

    content = fp.read()
    print(content)