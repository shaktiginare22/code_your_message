# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

import random

st = input("Enter message")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      list1=['opj', 'qsx', 'wgb', 'lwv', 'frh', 'zpc', 'cmo', 'bqj', 'lgs', 'fqy', 'pvl', 'doj', 'xsk', 'ijh', 'hjm', 'zji', 'kbd', 'dzz', 'tfb', 'ywr', 'tsb', 'lol', 'tyo', 'zei', 'kgb', 'rdw', 'hfj', 'rxx', 'bxt', 'fea', 'ohm', 'rzt', 'und', 'yxd', 'kce', 'epb', 'qtg', 'znl', 'yap', 'nyo', 'lvb', 'oyb', 'ocm', 'vzj', 'gba', 'xbc', 'gsy', 'rrd', 'zcw', 'mue', 'jnh', 'rkx', 'ywz', 'rxg', 'mtl', 'ypi', 'sgh', 'sec', 'kfm', 'fjt', 'rsk', 'vsf', 'sol', 'pys', 'ego', 'xx_']

      list2=['ebr', 'pwp', 'wud', 'dzl', 'hzb', 'znq', 'bpb', 'gzo', 'qbw', 'sxt', 'jqs', 'tey', 'vxc', 'xed', 'gku', 'rvn', 'zcr', 'syy', 'cwg', 'umb', 'die', 'zdw', 'dkf', 'mbz', 'rzz', 'pjk', 'bum', 'igl', 'whf', 'ghc', 'iul', 'wlz', 'jef', 'ypb', 'tmf', 'hkb', 'bqn', 'oax', 'lbs', 'mqg', 'dcg', 'lje', 'nqe', 'tqe', 'lku', 'gus', 'yre', 'bso', 'xsb', 'kxq', 'sws', 'sca', 'mam', 'qdm', 'bwl', 'swc', 'cpf', 'sab', 'gev', 'zhl', 'udo', 'tts', 'gai', 'mku', 'lfd', 'zfb']

      r1 = random.choice(list1)
      r2 = random.choice(list2) 
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))


#credit codewithharry
  
  
