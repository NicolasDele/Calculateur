def is_digit(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False
# Définition de la fonction evaluer() qui prend en entrée une chaîne de caractères représentant une expression arithmétique
# et qui retourne le résultat de l'évaluation de cette expression sous forme d'un entier.

def longueur(string: str) -> int:
    count = 0
    while string[count:]:
        count += 1
    return count

def pop_1(liste):
    if longueur(liste) == 0:
        return None
    else:
        last = liste[-1]
    return last

def pop_2(liste):
    if longueur(liste) == 0:
        return None
    else:
        liste = liste[:-1]
    return liste

def append(liste, element):
    liste += [element]
    return liste


def operande(pile, char):
    op2 = int(pop_1(pile))
    pile = pop_2(pile)
    op1 = int(pop_1(pile))
    pile = pop_2(pile)
    resultat = checkOperande(char, op1, op2)
    pile = append(pile,resultat)
    return pile

def checkOperande(char, op1, op2):
    # Selon l'opérateur, on effectue l'opération correspondante avec op1 et op2 et on empile le résultat sur la pile.
    if char == '+':
        resultat = op1 + op2
    elif char == '-':
        resultat = op1 - op2
    elif char == '*':
        resultat = op1 * op2
    elif char == '/':
        if op2!=0:
            resultat = op1 / op2
        else:
            return 'Impossible'
    return resultat

 # Initialisation de la pile qui va stocker les opérandes pendant l'évaluation de l'expression dans les paramètres.
def evaluer(expression: str,pile = [],var = '',space = 0, i = 0) -> int:

  # Parcours de la chaîne de caractères de l'expression, caractère par caractère.
  while i < longueur(expression):
    char = expression[i]
    i += 1
    if char!=' ' and char !='+'and char !='-'and char !='*'and char !='/':
        var+=char
    else:
        if char==' ':
            space+=1
        # Si le caractère est un chiffre, c'est un opérande : on le convertit en entier et on l'empile sur la pile.
        if is_digit(var) and char !='+'and char !='-'and char !='*'and char !='/':
          pile = append(pile,int(var))
          var = ''
        # Si le caractère est un opérateur, on effectue l'opération avec les deux opérandes qui se trouvent au sommet de la pile.
        elif char =='+'or char =='-'or char =='*' or char =='/':
            pile = operande(pile, char)
  # Lorsque l'expression a été entièrement évaluée, le résultat se trouve au sommet de la pile. On le retourne.
  return pile[-1]



# Définition de la fonction saisie() qui permet à l'utilisateur de saisir l'expression à évaluer et qui retourne cette expression sous forme de chaîne de caractères.
def saisie() -> str:
  expression = input("Veuillez saisir l'expression à évaluer(ne pas oublier de mettre des espaces entre tous les characteres) : ")
  return expression

# Définition de la fonction gestion_erreurs() qui prend en entrée une chaîne de caractères représentant une expression arithmétique
# et qui retourne True si l'expression est bien formée, False sinon.
def gestion_erreurs(expression: str) -> bool:
  # Si le nombre d'opérateurs dans l'expression est différent du nombre de chiffres moins le nombre d'espaces,
  # cela signifie que l'expression est mal formée.
  if (expression[-1]!= '/' and expression[-1]!= '*' and expression[-1]!= '+' and expression[-1]!= '-'):
    # On affiche un message d'erreur et on retourne False.
    print(expression[-1])
    print("Erreur : l'expression est mal formée.")
    return False
  #Si l'expression est bien formée, on retourne True.
  return True

def main() :
    #Appel de la fonction saisie() pour récupérer l'expression saisie par l'utilisateur.
    expression = saisie()
    resultat = 0
    #Appel de la fonction gestion_erreurs() pour vérifier que l'expression est bien formée.
    if gestion_erreurs(expression):

      #Si l'expression est bien formée, on appelle la fonction evaluer() pour évaluer l'expression.
      resultat = evaluer(expression)

    #On affiche le résultat.
    print(f"Résultat : {resultat}")


main()


