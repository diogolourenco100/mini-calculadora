Pelo meu comando usando a biblioteca OS, configurei para limpar o terminal apenas do Windows usando o comando "os.system('cls')".
Portanto se for usado em dispositivos Linux, em que o comando é "clear", poderá dar erro.
Recomendo que antes de executar o código, se for usuário Linux, mudar "os.system('cls')" para "os.system('clear')", ou simplesmente apagar toda a linha com "os.system('cls')".
