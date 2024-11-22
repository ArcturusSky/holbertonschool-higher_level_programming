# Introduction à la manipulation du DOM avec JavaScript

La manipulation du DOM (Document Object Model) est une compétence essentielle en JavaScript qui permet de modifier la structure, le contenu et le style des pages web dynamiquement. Ce cours présente les bases nécessaires pour interagir avec le DOM.

---

- [Introduction à la manipulation du DOM avec JavaScript](#introduction-à-la-manipulation-du-dom-avec-javascript)
  - [Le DOM (Document Object Model)](#le-dom-document-object-model)
  - [Accéder aux éléments du DOM](#accéder-aux-éléments-du-dom)
  - [Modifier le contenu d'un élément](#modifier-le-contenu-dun-élément)
  - [Ajouter un nouvel élément au DOM](#ajouter-un-nouvel-élément-au-dom)
  - [Modifier le style des éléments](#modifier-le-style-des-éléments)
  - [Supprimer un élément du DOM](#supprimer-un-élément-du-dom)
- [Liste des méthodes et fonctions pour la manipulation du DOM](#liste-des-méthodes-et-fonctions-pour-la-manipulation-du-dom)
  - [Accès aux éléments du DOM](#accès-aux-éléments-du-dom)
    - [`document.getElementById`](#documentgetelementbyid)
    - [`document.getElementsByClassName`](#documentgetelementsbyclassname)
    - [`document.getElementsByTagName`](#documentgetelementsbytagname)
    - [`document.querySelector`](#documentqueryselector)
    - [`document.querySelectorAll`](#documentqueryselectorall)
  - [Modification des éléments du DOM](#modification-des-éléments-du-dom)
    - [`.textContent`](#textcontent)
    - [`.innerHTML`](#innerhtml)
    - [`.outerHTML`](#outerhtml)
  - [Création et ajout d'éléments](#création-et-ajout-déléments)
    - [`document.createElement`](#documentcreateelement)
    - [`.appendChild`](#appendchild)
    - [`.insertBefore`](#insertbefore)
  - [Suppression et remplacement d'éléments](#suppression-et-remplacement-déléments)
    - [`.remove`](#remove)
    - [`.replaceChild`](#replacechild)
  - [Modification des styles](#modification-des-styles)
    - [`.style`](#style)
  - [Classes CSS](#classes-css)
    - [`.classList.add`](#classlistadd)
    - [`.classList.remove`](#classlistremove)
    - [`.classList.toggle`](#classlisttoggle)
    - [`.classList.contains`](#classlistcontains)
  - [Gestion des attributs](#gestion-des-attributs)
    - [`.getAttribute`](#getattribute)
    - [`.setAttribute`](#setattribute)
    - [`.removeAttribute`](#removeattribute)
  - [Dimensions et position](#dimensions-et-position)
    - [`.offsetHeight` / `.offsetWidth`](#offsetheight--offsetwidth)
    - [`.getBoundingClientRect`](#getboundingclientrect)
  - [Événements](#événements)
    - [`.addEventListener`](#addeventlistener)
    - [`.removeEventListener`](#removeeventlistener)


---

## Le DOM (Document Object Model)

**Définition :**  
Le DOM est une représentation en arbre des éléments HTML d'une page web. JavaScript peut accéder et modifier cet arbre pour mettre à jour la page de manière dynamique.

---

## Accéder aux éléments du DOM

**Définition :**  
Pour manipuler un élément du DOM, il faut d'abord le sélectionner. JavaScript propose plusieurs méthodes pour accéder aux éléments HTML.

**Syntaxe de base :**

```javascript
// Sélectionner un élément par son ID
document.getElementById('idElement');

// Sélectionner des éléments par leur classe
document.getElementsByClassName('nomDeClasse');

// Sélectionner des éléments par leur balise
document.getElementsByTagName('nomDeBalise');

// Sélectionner des éléments avec un sélecteur CSS
document.querySelector('sélecteurCSS'); 
document.querySelectorAll('sélecteurCSS');
```

**Explication de la syntaxe :**  
- `getElementById` retourne un seul élément correspondant à l'ID spécifié.  
- `getElementsByClassName` retourne une collection d'éléments partageant la même classe.  
- `querySelector` retourne le **premier** élément correspondant au sélecteur CSS donné.  
- `querySelectorAll` retourne **tous** les éléments correspondants au sélecteur.

**Exemple concret et simple :**

```javascript
// HTML : <div id="titre">Bonjour, monde !</div>

// Sélectionner l'élément par ID
let titre = document.getElementById('titre');
console.log(titre.textContent);
// Résultat attendu : "Bonjour, monde !"
```

**Décomposition de l'exemple :**  
- `document.getElementById('titre')` localise l'élément `<div>` avec l'ID `titre`.  
- `.textContent` permet d'accéder au contenu texte de l'élément.

---

## Modifier le contenu d'un élément

**Définition :**  
Vous pouvez modifier le texte ou le contenu HTML d'un élément pour mettre à jour l'affichage.

**Syntaxe de base :**

```javascript
// Modifier le texte
element.textContent = "Nouveau texte";

// Modifier le contenu HTML
element.innerHTML = "<strong>Texte en gras</strong>";
```

**Exemple concret et simple :**

```javascript
// HTML : <p id="paragraphe">Ancien texte</p>

// Modifier le texte
let paragraphe = document.getElementById('paragraphe');
paragraphe.textContent = "Nouveau texte";

console.log(paragraphe.textContent);
// Résultat attendu : "Nouveau texte"
```

**Décomposition de l'exemple :**  
- `getElementById('paragraphe')` localise l'élément `<p>` avec l'ID `paragraphe`.  
- `textContent` est utilisé pour remplacer "Ancien texte" par "Nouveau texte".  

---

## Ajouter un nouvel élément au DOM

**Définition :**  
JavaScript permet de créer et d'ajouter dynamiquement des éléments HTML au DOM.

**Syntaxe de base :**

```javascript
// Créer un nouvel élément
let nouvelElement = document.createElement('nomDeBalise');

// Ajouter du contenu
nouvelElement.textContent = "Contenu de l'élément";

// Insérer l'élément dans le DOM
parentElement.appendChild(nouvelElement);
```

**Exemple concret et simple :**

```javascript
// HTML : <ul id="liste"></ul>

// Créer un nouvel élément <li>
let liste = document.getElementById('liste');
let nouvelItem = document.createElement('li');

// Ajouter du texte au nouvel élément
nouvelItem.textContent = "Nouvel item";

// Ajouter l'élément à la liste
liste.appendChild(nouvelItem);

console.log(liste.innerHTML);
// Résultat attendu : "<li>Nouvel item</li>"
```

**Décomposition de l'exemple :**  
- `createElement('li')` crée un élément `<li>`.  
- `textContent` ajoute le texte "Nouvel item" à cet élément.  
- `appendChild(nouvelItem)` insère le nouvel élément dans `<ul>`.

---

## Modifier le style des éléments

**Définition :**  
Vous pouvez modifier les styles CSS d'un élément pour personnaliser son apparence.

**Syntaxe de base :**

```javascript
// Modifier un style individuel
element.style.nomDuStyle = "valeur";
```

**Exemple concret et simple :**

```javascript
// HTML : <p id="texte">Texte stylé</p>

// Modifier la couleur du texte
let texte = document.getElementById('texte');
texte.style.color = "red";

console.log(texte.style.color);
// Résultat attendu : "red"
```

**Décomposition de l'exemple :**  
- `style.color` modifie la propriété CSS `color` pour que le texte devienne rouge.

---

## Supprimer un élément du DOM

**Définition :**  
Pour supprimer un élément du DOM, vous pouvez utiliser sa méthode `remove`.

**Syntaxe de base :**

```javascript
// Supprimer un élément
element.remove();
```

**Exemple concret et simple :**

```javascript
// HTML : <div id="aSupprimer">Supprime-moi !</div>

// Supprimer l'élément
let element = document.getElementById('aSupprimer');
element.remove();

console.log(document.getElementById('aSupprimer'));
// Résultat attendu : null
```

**Décomposition de l'exemple :**  
- `remove()` enlève l'élément `<div>` identifié par `aSupprimer` du DOM.

---

# Liste des méthodes et fonctions pour la manipulation du DOM

Voici une liste organisée des méthodes et fonctions courantes pour manipuler le DOM. Les méthodes sont classées par ordre alphabétique et regroupées logiquement pour faciliter la compréhension.

---

## Accès aux éléments du DOM

### `document.getElementById`

**Définition :**  
Sélectionne un élément unique dans le DOM en fonction de son ID.

**Syntaxe :**  

```javascript
let element = document.getElementById('idElement');
```

---

### `document.getElementsByClassName`

**Définition :**  
Sélectionne tous les éléments qui partagent une même classe.

**Syntaxe :**  

```javascript
let elements = document.getElementsByClassName('nomDeClasse');
```

---

### `document.getElementsByTagName`

**Définition :**  
Sélectionne tous les éléments qui ont une balise spécifique.

**Syntaxe :**  

```javascript
let elements = document.getElementsByTagName('nomDeBalise');
```

---

### `document.querySelector`

**Définition :**  
Sélectionne le premier élément correspondant à un sélecteur CSS.

**Syntaxe :**  

```javascript
let element = document.querySelector('sélecteurCSS');
```

---

### `document.querySelectorAll`

**Définition :**  
Sélectionne tous les éléments correspondant à un sélecteur CSS.

**Syntaxe :**  

```javascript
let elements = document.querySelectorAll('sélecteurCSS');
```

---

## Modification des éléments du DOM

### `.textContent`

**Définition :**  
Accède ou modifie le texte contenu dans un élément.

**Syntaxe :**  

```javascript
element.textContent = "Nouveau texte";
```

---

### `.innerHTML`

**Définition :**  
Accède ou modifie le contenu HTML (balises incluses) d'un élément.

**Syntaxe :**  

```javascript
element.innerHTML = "<strong>Nouveau contenu HTML</strong>";
```

---

### `.outerHTML`

**Définition :**  
Accède ou remplace un élément HTML complet (y compris lui-même).

**Syntaxe :**  

```javascript
element.outerHTML = "<div>Nouveau HTML</div>";
```

---

## Création et ajout d'éléments

### `document.createElement`

**Définition :**  
Crée un nouvel élément HTML.

**Syntaxe :**  

```javascript
let nouvelElement = document.createElement('nomDeBalise');
```

---

### `.appendChild`

**Définition :**  
Ajoute un élément enfant à un parent existant.

**Syntaxe :**  

```javascript
parentElement.appendChild(nouvelElement);
```

---

### `.insertBefore`

**Définition :**  
Insère un élément avant un autre élément enfant.

**Syntaxe :**  

```javascript
parentElement.insertBefore(nouvelElement, elementExistant);
```

---

## Suppression et remplacement d'éléments

### `.remove`

**Définition :**  
Supprime un élément du DOM.

**Syntaxe :**  

```javascript
element.remove();
```

---

### `.replaceChild`

**Définition :**  
Remplace un élément enfant par un autre dans le DOM.

**Syntaxe :**  

```javascript
parentElement.replaceChild(nouvelElement, ancienElement);
```

---

## Modification des styles

### `.style`

**Définition :**  
Modifie directement les styles CSS d'un élément.

**Syntaxe :**  

```javascript
element.style.color = "blue";
```

---

## Classes CSS

### `.classList.add`

**Définition :**  
Ajoute une ou plusieurs classes CSS à un élément.

**Syntaxe :**  

```javascript
element.classList.add('nouvelleClasse');
```

---

### `.classList.remove`

**Définition :**  
Supprime une ou plusieurs classes CSS d'un élément.

**Syntaxe :**  

```javascript
element.classList.remove('classeExistante');
```

---

### `.classList.toggle`

**Définition :**  
Ajoute ou supprime une classe CSS selon qu'elle est déjà présente ou non.

**Syntaxe :**  

```javascript
element.classList.toggle('classe');
```

---

### `.classList.contains`

**Définition :**  
Vérifie si un élément possède une classe spécifique.

**Syntaxe :**  

```javascript
let aLaClasse = element.classList.contains('classe');
```

---

## Gestion des attributs

### `.getAttribute`

**Définition :**  
Récupère la valeur d'un attribut d'un élément.

**Syntaxe :**  

```javascript
let valeur = element.getAttribute('nomAttribut');
```

---

### `.setAttribute`

**Définition :**  
Ajoute ou modifie la valeur d'un attribut d'un élément.

**Syntaxe :**  

```javascript
element.setAttribute('nomAttribut', 'valeur');
```

---

### `.removeAttribute`

**Définition :**  
Supprime un attribut d'un élément.

**Syntaxe :**  

```javascript
element.removeAttribute('nomAttribut');
```

---

## Dimensions et position

### `.offsetHeight` / `.offsetWidth`

**Définition :**  
Renvoie la hauteur ou la largeur totale d'un élément, incluant les bordures et le padding.

**Syntaxe :**  

```javascript
let hauteur = element.offsetHeight;
let largeur = element.offsetWidth;
```

---

### `.getBoundingClientRect`

**Définition :**  
Renvoie les dimensions et la position d'un élément par rapport à la fenêtre.

**Syntaxe :**  

```javascript
let rect = element.getBoundingClientRect();
console.log(rect.top, rect.left, rect.width, rect.height);
```

---

## Événements

### `.addEventListener`

**Définition :**  
Attache un gestionnaire d'événement à un élément.

**Syntaxe :**  

```javascript
element.addEventListener('typeEvenement', fonctionCallback);
```

---

### `.removeEventListener`

**Définition :**  
Détache un gestionnaire d'événement d'un élément.

**Syntaxe :**  

```javascript
element.removeEventListener('typeEvenement', fonctionCallback);
```
--- 

