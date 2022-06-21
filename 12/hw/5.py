for i in range(1000):
    for j in range(100):
            s = '0' + '1' * i + '2' * j + '0'
            while '00' not in s:
                s = s.replace('021', '102', 1)
                s = s.replace('022', '301', 1)
                s = s.replace('02', '20', 1)
                s = s.replace('01', '10', 1)
                if s.count('1') == 27 and s.count('2') == 9 and s.count('3') == 4:
                    print(i, j)
                    break
# for i in range (1,1000):
#     for b in range(1,1000):
#         s='0'+'1'*i+'2'*b+'0'
#         while not '00' in s:
#             s=s.replace('021','102',1)
#             s=s.replace('022','301',1)
#             s=s.replace('02','20',1)
#             s=s.replace('01','10',1)
#             if s.count('1')==27 and s.count('2')==9 and s.count('3')==4:
#                 print(b)