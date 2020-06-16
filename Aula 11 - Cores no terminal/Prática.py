print("""
\033[4:31:45mVictor\033[m\n
\033[1:36:43mRamalho\033[m\n
\033[7:33:47mTiago\033[m\n
\033[0:34:41mPedro\033[m\n
\033[7:47:40mFernando\033[m\n
\033[1:32:45mSimone\033[m\n
\033[1:30:42mChico\033[m
""")

cores = {'roxogay' : '\033[7:35:40m', 'limpa' : '\033[m'}

print('Você é {}gay{}, Gustavo?'.format('\033[7:35:40m', '\033[m'))
print('Você é {}gay{}, Gustavo?'.format(cores['roxogay'], cores['limpa']))

#colorize mto mais decente
