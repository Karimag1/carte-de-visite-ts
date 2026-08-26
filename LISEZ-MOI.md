# Carte de visite virtuelle – hébergement gratuit sur GitHub Pages

Résultat : une adresse publique du type `https://TON-COMPTE.github.io/carte-louis-hage/`,
en HTTPS, gratuite, sans serveur à gérer, accessible à tout le monde **sans compte**.
Le QR code qui ouvre la carte est généré automatiquement à chaque publication.

## Contenu du dossier

```
index.html                       la carte (logo, polices et QR vCard intégrés)
louis-hage.vcf                   la fiche contact (bouton « Ajouter aux contacts »)
carte-virtuelle-louis-hage.png   image d'aperçu pour les partages WhatsApp / Teams / mail
make_qr.py                       génère le QR code de l'adresse de la carte
.nojekyll                        indique à GitHub de publier les fichiers tels quels
.github/workflows/pages.yml      publication automatique + génération du QR
```

## Mise en ligne (10 minutes, une seule fois)

1. **Compte GitHub** : créer un compte gratuit sur github.com si besoin.

2. **Créer le dépôt** : bouton « New repository », nom `carte-louis-hage`,
   visibilité **Public** (obligatoire pour Pages en gratuit), puis « Create repository ».

3. **Envoyer les fichiers**, au choix :

   *Avec git (Mac : Terminal, Windows : Git Bash / Windows Terminal)* :
   ```bash
   cd carte-louis-hage-github
   git init -b main
   git add -A
   git commit -m "Carte de visite virtuelle"
   git remote add origin https://github.com/TON-COMPTE/carte-louis-hage.git
   git push -u origin main
   ```

   *Sans git, depuis le navigateur* : dans le dépôt, « Add file → Upload files »,
   glisser **tout le contenu** du dossier (y compris le dossier caché `.github`
   et le fichier `.nojekyll` – activer l'affichage des fichiers cachés), puis « Commit changes ».
   Si le dossier `.github` ne passe pas, créer le fichier à la main :
   « Add file → Create new file », nom `.github/workflows/pages.yml`, coller le contenu.

4. **Activer Pages** : Settings → Pages → *Build and deployment* → Source : **GitHub Actions**.

5. Onglet **Actions** : le workflow « Publier la carte sur GitHub Pages » tourne (~1 min).
   À la fin, il affiche l'adresse de la carte. Le QR code est disponible à :

   ```
   https://TON-COMPTE.github.io/carte-louis-hage/qr-carte.png     (et .svg)
   ```

   C'est ce fichier que tu donnes aux gens : le scan ouvre la carte.

## Vérification

- Ouvrir l'adresse depuis un téléphone en 4G : la carte s'affiche, sans connexion à quoi que ce soit.
- Scanner `qr-carte.png` avec l'appareil photo : la carte s'ouvre.
- « Ajouter aux contacts » : le téléphone propose de créer la fiche.
- Le QR **dans** la carte contient la fiche contact elle-même (fonctionne même hors ligne).

## Nom de domaine de l'entreprise (facultatif)

Pour une adresse comme `https://carte.triomphe-securite.fr` :
1. Chez le registrar du domaine : enregistrement **CNAME** `carte` → `TON-COMPTE.github.io`.
2. Settings → Pages → *Custom domain* : `carte.triomphe-securite.fr`, cocher *Enforce HTTPS*.
3. Relancer le workflow (Actions → Run workflow) : le QR est regénéré avec la nouvelle adresse.

Attention : l'adresse contenue dans un QR déjà imprimé ne change pas. Choisir l'adresse
définitive **avant** d'imprimer.

## Mettre à jour les coordonnées

Modifier `index.html` (section `rows`) et `louis-hage.vcf`, puis `git push` (ou
« Upload files » à nouveau) : la carte est republiée automatiquement. Le QR vCard intégré
dans la page contient les coordonnées : il doit alors être regénéré (demander à Claude).

## Alternative GitLab Pages

Même principe ; remplacer le workflow par un `.gitlab-ci.yml` qui copie les fichiers dans
`public/`. Demander à Claude si besoin.
