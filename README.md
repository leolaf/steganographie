# Stéganographie

> KHIAL Omar et LAFFONT Léo

## INFO002 Cryptologie

### Question 1

Écriture de la fonction `hide_msg` dans `./Model/Steganography.py`.

Exemples d'utilisation :

```sh
python .\main.py -H -i .\images\Blanc.png -o ./images/sortie.png -m "Vivement les vacances !"
python .\main.py --hide -i .\images\Blanc.png -o ./images/sortie.png -m "Vivement les vacances !"
```


Écriture de la fonction `find_msg` dans `./Model/Steganography.py`.

Exemples d'utilisation :

```sh
python .\main.py -F -i .\images\sortie.png
python .\main.py --find -i .\images\sortie.png
```
