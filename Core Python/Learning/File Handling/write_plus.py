with open('Core Python/Demos/File Handling/intro3.txt','w+') as fp:

    print(fp.tell())

    fp.write('This is content.')

    print(fp.tell())

    fp.seek(0,0)

    content = fp.read() 
    
    print(content)