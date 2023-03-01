> KHIAL Omar et LAFFONT Léo

# Stéganographie
## INFO002 Cryptologie

### Question 1
Écriture de la fonction `hide_msg` dans `./Model/Steganography.py`.

Pour cacher un message : `python .\main.py -H -i <image_entree> -m <message> -o <sortie>`. <br>
Ex :
```sh
python .\main.py -H -i .\images\Blanc.png -m "Vivement les vacances !" -o ./images/sortie.png
```


Écriture de la fonction `find_msg` dans `./Model/Steganography.py`.

Pour retrouver un message : `python .\main.py -F -i <image_entree>`. <br>
Ex :
```sh
python .\main.py -F -i .\images\sortie.png
```
