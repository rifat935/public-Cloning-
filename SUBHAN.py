import platform
bit=platform.architecture()[0]
if bit =='64bit':
    from SUBHAN import main
    menu()
else:
    print('Sorry Your Device Not Support Mr.SUBHAN Tools')
    main()
