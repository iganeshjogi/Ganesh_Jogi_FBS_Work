with open('Core Python/Demos/File Handling/intro3.txt','a+') as fp:

    print(fp.tell())

    fp.write('\nThis is the next line.')

    fp.seek(0,0)

    content = fp.read()

    print(content)