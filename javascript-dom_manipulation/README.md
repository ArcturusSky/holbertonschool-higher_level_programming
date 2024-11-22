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
  - [Suppression d'éléments](#suppression-déléments)
    - [`.remove`](#remove)
  - [Modification des attributs d'éléments](#modification-des-attributs-déléments)
    - [`.setAttribute`](#setattribute)
    - [`.getAttribute`](#getattribute)
    - [`.removeAttribute`](#removeattribute)
  - [Événements](#événements)
    - [`.addEventListener`](#addeventlistener)
    - [`.removeEventListener`](#removeeventlistener)
    - [`.dispatchEvent`](#dispatchevent)
  - [Manipulation des classes](#manipulation-des-classes)
    - [`.classList.add`](#classlistadd)
    - [`.classList.remove`](#classlistremove)
    - [`.classList.toggle`](#classlisttoggle)
  - [Méthodes + avancées](#méthodes--avancées)
    - [Sélection d'éléments avancée](#sélection-déléments-avancée)
      - [`document.closest`](#documentclosest)
      - [`document.activeElement`](#documentactiveelement)
    - [Gestion des événements avancée](#gestion-des-événements-avancée)
      - [`.dispatchEvent`](#dispatchevent-1)
    - [Création d'événements personnalisés](#création-dévénements-personnalisés)
      - [`CustomEvent`](#customevent)


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

---

## Accès aux éléments du DOM

### `document.getElementById`

**Définition :**  
Sélectionne un élément unique dans le DOM en fonction de son ID.

**Syntaxe :**  

 ```javascript
let element = document.getElementById('idElement');
 ```

**Breakdown de la syntaxe :**  
- `document` : fait référence à l'objet global représentant le DOM.
- `getElementById` : méthode utilisée pour sélectionner un élément par son ID unique.
- `'idElement'` : l'ID de l'élément que vous souhaitez sélectionner.

**Exemple concret :**

 ```javascript
let bouton = document.getElementById('monBouton');
console.log(bouton);
 ```

**Breakdown de l'exemple :**  
- `monBouton` est l'ID d'un élément `<button>` dans le DOM.  
- La méthode retourne cet élément, et la fonction `console.log()` affiche les détails dans la console.

---

### `document.getElementsByClassName`

**Définition :**  
Sélectionne tous les éléments qui partagent une même classe.

**Syntaxe :**  

 ```javascript
let elements = document.getElementsByClassName('nomDeClasse');
 ```

**Breakdown de la syntaxe :**  
- `document` : référence au DOM.
- `getElementsByClassName` : méthode qui retourne une collection de tous les éléments avec la classe spécifiée.
- `'nomDeClasse'` : la classe à cibler.

**Exemple concret :**

 ```javascript
let paragraphs = document.getElementsByClassName('texte');
console.log(paragraphs);
 ```

**Breakdown de l'exemple :**  
- Cette méthode renvoie une collection d'éléments qui ont la classe `texte`.  
- La méthode `console.log()` affichera tous les éléments de cette collection dans la console.

---

### `document.getElementsByTagName`

**Définition :**  
Sélectionne tous les éléments qui ont une balise spécifique.

**Syntaxe :**  

 ```javascript
let elements = document.getElementsByTagName('nomDeBalise');
 ```

**Breakdown de la syntaxe :**  
- `document` : fait référence à l'objet DOM.
- `getElementsByTagName` : méthode qui retourne tous les éléments de la balise spécifiée.
- `'nomDeBalise'` : le nom de la balise HTML à cibler (par exemple, `'div'`, `'p'`, etc.).

**Exemple concret :**

 ```javascript
let divs = document.getElementsByTagName('div');
console.log(divs);
 ```

**Breakdown de l'exemple :**  
- Cette méthode renverra toutes les balises `<div>` dans le DOM.  
- La méthode `console.log()` affiche ces éléments dans la console.

---

### `document.querySelector`

**Définition :**  
Sélectionne le premier élément correspondant à un sélecteur CSS.

**Syntaxe :**  

 ```javascript
let element = document.querySelector('sélecteurCSS');
 ```

**Breakdown de la syntaxe :**  
- `document` : objet représentant le DOM.
- `querySelector` : méthode qui retourne le premier élément qui correspond au sélecteur CSS spécifié.
- `'sélecteurCSS'` : sélecteur CSS (peut être un ID, une classe, une balise, etc.).

**Exemple concret :**

 ```javascript
let header = document.querySelector('#header');
console.log(header);
 ```

**Breakdown de l'exemple :**  
- Ici, `#header` est un sélecteur CSS qui cible l'élément avec l'ID `header`.  
- `querySelector` sélectionne cet élément et le log dans la console.

---

### `document.querySelectorAll`

**Définition :**  
Sélectionne tous les éléments correspondant à un sélecteur CSS.

**Syntaxe :**  

 ```javascript
let elements = document.querySelectorAll('sélecteurCSS');
 ```

**Breakdown de la syntaxe :**  
- `document` : représente le DOM.
- `querySelectorAll` : méthode qui retourne tous les éléments correspondants au sélecteur CSS spécifié sous forme de NodeList.
- `'sélecteurCSS'` : un sélecteur CSS.

**Exemple concret :**

 ```javascript
let buttons = document.querySelectorAll('.button');
buttons.forEach(button => {
  console.log(button);
});
 ```

**Breakdown de l'exemple :**  
- `.button` est un sélecteur CSS qui cible tous les éléments avec la classe `button`.  
- `querySelectorAll` retourne tous les éléments correspondants sous forme de NodeList.  
- Ensuite, `forEach` est utilisé pour parcourir cette liste et afficher chaque bouton.

---

## Modification des éléments du DOM

### `.textContent`

**Définition :**  
Accède ou modifie le texte contenu dans un élément.

**Syntaxe :**  

 ```javascript
element.textContent = "Nouveau texte";
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément dont on veut modifier le contenu texte.
- `.textContent` : propriété qui permet de définir ou récupérer le texte à l'intérieur de l'élément.

**Exemple concret :**

 ```javascript
let title = document.getElementById('title');
title.textContent = 'Bienvenue sur ma page!';
 ```

**Breakdown de l'exemple :**  
- L'élément avec l'ID `title` se voit attribuer un nouveau texte grâce à `textContent`.
- Le texte affiché devient "Bienvenue sur ma page!".

---

### `.innerHTML`

**Définition :**  
Accède ou modifie le contenu HTML (balises incluses) d'un élément.

**Syntaxe :**  

 ```javascript
element.innerHTML = "<strong>Nouveau contenu HTML</strong>";
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément dont on veut modifier le contenu HTML.
- `.innerHTML` : propriété qui permet de définir ou récupérer le contenu HTML de l'élément.

**Exemple concret :**

 ```javascript
let content = document.getElementById('content');
content.innerHTML = '<p><strong>Texte avec du HTML</strong></p>';
 ```

**Breakdown de l'exemple :**  
- L'élément avec l'ID `content` est mis à jour pour inclure du texte HTML, ici un paragraphe avec du texte en gras.
- L'élément contiendra désormais un paragraphe avec un texte formaté.

---

### `.outerHTML`

**Définition :**  
Accède ou remplace un élément HTML complet (y compris lui-même).

**Syntaxe :**  

 ```javascript
element.outerHTML = "<div>Nouveau HTML</div>";
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément que vous voulez remplacer.
- `.outerHTML` : permet de remplacer l'élément complet avec du nouveau contenu HTML.

**Exemple concret :**

 ```javascript
let box = document.getElementById('box');
box.outerHTML = '<section><p>Contenu dans une section</p></section>';
 ```

**Breakdown de l'exemple :**  
- L'élément avec l'ID `box` est entièrement remplacé par une nouvelle balise `<section>`, incluant un paragraphe à l'intérieur.

---

## Création et ajout d'éléments

### `document.createElement`

**Définition :**  
Crée un nouvel élément HTML.

**Syntaxe :**  

 ```javascript
let nouvelElement = document.createElement('nomDeBalise');
 ```

**Breakdown de la syntaxe :**  
- `document` : l'objet représentant le DOM.
- `createElement` : méthode qui crée un nouvel élément HTML basé sur le nom de la balise spécifiée.

**Exemple concret :**

 ```javascript
let newDiv = document.createElement('div');
newDiv.textContent = 'Ceci est une nouvelle div';
document.body.appendChild(newDiv);
 ```

**Breakdown de l'exemple :**  
- La méthode `createElement` crée un élément `<div>`.
- Le texte de ce nouvel élément est défini grâce à `textContent`.
- L'élément est ensuite ajouté au corps du document avec `appendChild`.

---

### `.appendChild`

**Définition :**  
Ajoute un élément enfant à un parent existant.

**Syntaxe :**  

 ```javascript
parentElement.appendChild(nouvelElement);
 ```

**Breakdown de la syntaxe :**  
- `parentElement` : l'élément parent auquel vous voulez ajouter un nouvel enfant.
- `.appendChild` : méthode qui ajoute un enfant à l'élément spécifié.

**Exemple concret :**

 ```javascript
let ul = document.querySelector('ul');
let li = document.createElement('li');
li.textContent = 'Nouvel élément';
ul.appendChild(li);
 ```

**Breakdown de l'exemple :**  
- L'élément `<ul>` est sélectionné, et un nouvel élément `<li>` est créé.
- Cet élément `<li>` est ensuite ajouté à la liste `<ul>`.

---

### `.insertBefore`

**Définition :**  
Insère un élément avant un autre élément enfant.

**Syntaxe :**  

 ```javascript
parentElement.insertBefore(nouvelElement, referenceElement);
 ```

**Breakdown de la syntaxe :**  
- `parentElement` : l'élément parent auquel vous voulez ajouter un enfant avant un autre élément.
- `insertBefore` : méthode qui insère un élément avant un autre élément déjà présent dans le DOM.
- `referenceElement` : l'élément avant lequel vous souhaitez insérer le nouvel élément.

**Exemple concret :**

 ```javascript
let ul = document.querySelector('ul');
let newLi = document.createElement('li');
newLi.textContent = 'Élément ajouté avant';
let firstLi = ul.querySelector('li');
ul.insertBefore(newLi, firstLi);
 ```

**Breakdown de l'exemple :**  
- Un nouvel élément `<li>` est créé et inséré avant le premier élément `<li>` existant dans la liste `<ul>`.

---

## Suppression d'éléments

### `.remove`

**Définition :**  
Supprime l'élément lui-même du DOM.

**Syntaxe :**  

 ```javascript
element.remove();
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément à supprimer.
- `.remove()` : méthode utilisée pour supprimer l'élément du DOM.

**Exemple concret :**

 ```javascript
let box = document.getElementById('box');
box.remove();
 ```

**Breakdown de l'exemple :**  
- L'élément avec l'ID `box` est complètement supprimé du DOM.

---

## Modification des attributs d'éléments

### `.setAttribute`

**Définition :**  
Modifie ou ajoute un attribut à un élément HTML.

**Syntaxe :**  

 ```javascript
element.setAttribute('attribut', 'valeur');
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément auquel vous souhaitez ajouter ou modifier un attribut.
- `setAttribute` : méthode pour définir un attribut avec une valeur spécifique.
- `'attribut'` : le nom de l'attribut à ajouter ou modifier.
- `'valeur'` : la valeur que vous voulez attribuer à l'attribut.

**Exemple concret :**

 ```javascript
let img = document.getElementById('image');
img.setAttribute('src', 'nouvelle-image.jpg');
 ```

**Breakdown de l'exemple :**  
- L'attribut `src` de l'élément `<img>` est modifié pour pointer vers `nouvelle-image.jpg`.

---

### `.getAttribute`

**Définition :**  
Récupère la valeur d'un attribut d'un élément HTML.

**Syntaxe :**  

 ```javascript
let valeur = element.getAttribute('attribut');
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément dont vous souhaitez obtenir la valeur de l'attribut.
- `getAttribute` : méthode qui récupère la valeur de l'attribut spécifié.
- `'attribut'` : le nom de l'attribut dont vous voulez obtenir la valeur.

**Exemple concret :**

 ```javascript
let link = document.getElementById('monLien');
let href = link.getAttribute('href');
console.log(href);
 ```

**Breakdown de l'exemple :**  
- La méthode `getAttribute` récupère la valeur de l'attribut `href` de l'élément `<a>` avec l'ID `monLien`.

---

### `.removeAttribute`

**Définition :**  
Supprime un attribut d'un élément HTML.

**Syntaxe :**  

 ```javascript
element.removeAttribute('attribut');
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément dont vous souhaitez supprimer un attribut.
- `removeAttribute` : méthode qui supprime l'attribut spécifié de l'élément.
- `'attribut'` : le nom de l'attribut à supprimer.

**Exemple concret :**

 ```javascript
let bouton = document.getElementById('monBouton');
bouton.removeAttribute('disabled');
 ```

**Breakdown de l'exemple :**  
- L'attribut `disabled` de l'élément `<button>` avec l'ID `monBouton` est supprimé, permettant ainsi de réactiver le bouton.

---

## Événements

### `.addEventListener`

**Définition :**  
Ajoute un gestionnaire d'événements à un élément.

**Syntaxe :**  

 ```javascript
element.addEventListener('typeEvenement', fonction);
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément auquel vous voulez ajouter un gestionnaire d'événement.
- `.addEventListener` : méthode qui permet d'ajouter un écouteur d'événement à un élément.
- `'typeEvenement'` : type d'événement à écouter (par exemple, `'click'`, `'mouseover'`, `'keydown'`).
- `fonction` : fonction qui sera exécutée lorsqu'un événement se produira.

**Exemple concret :**

 ```javascript
let bouton = document.getElementById('monBouton');
bouton.addEventListener('click', function() {
  alert('Bouton cliqué!');
});
 ```

**Breakdown de l'exemple :**  
- Lorsqu'on clique sur l'élément avec l'ID `monBouton`, l'alerte `Bouton cliqué!` s'affiche.

---

### `.removeEventListener`

**Définition :**  
Supprime un gestionnaire d'événements ajouté à un élément.

**Syntaxe :**  

 ```javascript
element.removeEventListener('typeEvenement', fonction);
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément auquel vous souhaitez retirer un gestionnaire d'événement.
- `.removeEventListener` : méthode qui supprime un écouteur d'événements.
- `'typeEvenement'` : type d'événement à arrêter d'écouter.
- `fonction` : fonction à retirer du gestionnaire d'événements.

**Exemple concret :**

 ```javascript
let bouton = document.getElementById('monBouton');
function clicBouton() {
  alert('Bouton cliqué!');
}
bouton.addEventListener('click', clicBouton);
// Pour supprimer l'événement plus tard :
bouton.removeEventListener('click', clicBouton);
 ```

**Breakdown de l'exemple :**  
- Un gestionnaire d'événement `clicBouton` est attaché à l'élément `monBouton` pour afficher une alerte à chaque clic.
- Après l'ajout, `removeEventListener` est utilisé pour retirer ce gestionnaire d'événements.

---

### `.dispatchEvent`

**Définition :**  
Déclenche un événement sur un élément manuellement.

**Syntaxe :**  

 ```javascript
element.dispatchEvent(event);
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément sur lequel vous souhaitez déclencher un événement.
- `.dispatchEvent` : méthode utilisée pour déclencher un événement sur l'élément spécifié.
- `event` : l'événement à déclencher (généralement un objet `Event`).

**Exemple concret :**

 ```javascript
let bouton = document.getElementById('monBouton');
let evenement = new Event('click');
bouton.dispatchEvent(evenement);
 ```

**Breakdown de l'exemple :**  
- L'événement `click` est déclenché manuellement sur l'élément `monBouton` à l'aide de `dispatchEvent`. Cela simule un clic sur le bouton.

---

## Manipulation des classes

### `.classList.add`

**Définition :**  
Ajoute une ou plusieurs classes à un élément.

**Syntaxe :**  

 ```javascript
element.classList.add('nomDeClasse');
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément auquel vous souhaitez ajouter une ou plusieurs classes.
- `.classList.add` : méthode qui permet d'ajouter des classes CSS à un élément.

**Exemple concret :**

 ```javascript
let div = document.getElementById('maDiv');
div.classList.add('nouvelleClasse');
 ```

**Breakdown de l'exemple :**  
- La classe `nouvelleClasse` est ajoutée à l'élément avec l'ID `maDiv`.

---

### `.classList.remove`

**Définition :**  
Supprime une ou plusieurs classes d'un élément.

**Syntaxe :**  

 ```javascript
element.classList.remove('nomDeClasse');
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément dont vous souhaitez supprimer des classes.
- `.classList.remove` : méthode pour supprimer une ou plusieurs classes de l'élément.

**Exemple concret :**

 ```javascript
let div = document.getElementById('maDiv');
div.classList.remove('ancienneClasse');
 ```

**Breakdown de l'exemple :**  
- La classe `ancienneClasse` est retirée de l'élément avec l'ID `maDiv`.

---

### `.classList.toggle`

**Définition :**  
Ajoute ou supprime une classe d'un élément, selon qu'elle est déjà présente.

**Syntaxe :**  

 ```javascript
element.classList.toggle('nomDeClasse');
 ```

**Breakdown de la syntaxe :**  
- `element` : l'élément sur lequel vous voulez ajouter ou supprimer la classe.
- `.classList.toggle` : méthode qui ajoute la classe si elle est absente, ou la retire si elle est déjà présente.

**Exemple concret :**

 ```javascript
let div = document.getElementById('maDiv');
div.classList.toggle('active');
 ```

**Breakdown de l'exemple :**  
- La méthode vérifie si `active` est présente dans les classes de l'élément. Si elle est présente, elle est retirée ; sinon, elle est ajoutée.

--- 

## Méthodes + avancées

### Sélection d'éléments avancée  

#### `document.closest`  

**Définition :**  
Renvoie le premier ancêtre d’un élément (ou l'élément lui-même) qui correspond à un sélecteur CSS donné.  

**Syntaxe :**  
 ```javascript  
let ancetre = element.closest('sélecteurCSS');  
 ```  

**Breakdown de la syntaxe :**  
- **`element`** : L'élément sur lequel on effectue la recherche.  
- **`closest`** : Méthode qui parcourt la chaîne parentale.  
- **`'sélecteurCSS'`** : Le sélecteur utilisé pour identifier l'ancêtre recherché.  

**Exemple simple concret :**  
 ```javascript  
// HTML : <div class="parent"><div class="child"></div></div>  
let enfant = document.querySelector('.child');  
let parent = enfant.closest('.parent');  
console.log(parent); // Renvoie l'élément avec la classe "parent"  
 ```  

**Breakdown de l'exemple :**  
1. **Sélection de l'élément `child`** : On cible l'élément ayant la classe "child".  
2. **Recherche du parent avec `closest`** : On recherche le premier ancêtre correspondant au sélecteur `.parent`.  
3. **Résultat** : L'élément "parent" est retourné et affiché dans la console.  

---  

#### `document.activeElement`  

**Définition :**  
Renvoie l'élément actuellement actif dans le document (par exemple, un champ de texte sélectionné).  

**Syntaxe :**  
 ```javascript  
let actif = document.activeElement;  
 ```  

**Breakdown de la syntaxe :**  
- **`document`** : Représente le document DOM entier.  
- **`activeElement`** : Propriété qui retourne l'élément actif.  

**Exemple simple concret :**  
 ```javascript  
// Utiliser un input actif dans la page  
let actif = document.activeElement;  
if (actif.tagName === 'INPUT') {  
    console.log("Un champ de saisie est actif.");  
}  
 ```  

**Breakdown de l'exemple :**  
1. **Vérification de l'élément actif** : On utilise `document.activeElement` pour détecter l'élément actuellement actif.  
2. **Condition** : Si l'élément actif est une balise `<input>`, un message s'affiche dans la console.  

---  

### Gestion des événements avancée  

#### `.dispatchEvent`  

**Définition :**  
Déclenche manuellement un événement sur un élément donné.  

**Syntaxe :**  
 ```javascript  
element.dispatchEvent(nouvelEvenement);  
 ```  

**Breakdown de la syntaxe :**  
- **`element`** : L'élément sur lequel déclencher l'événement.  
- **`dispatchEvent`** : Méthode pour lancer l'événement.  
- **`nouvelEvenement`** : Objet `Event` ou `CustomEvent` représentant l'événement à déclencher.  

**Exemple simple concret :**  
 ```javascript  
let bouton = document.querySelector('button');  
let evenement = new Event('click');  
bouton.dispatchEvent(evenement);  
 ```  

**Breakdown de l'exemple :**  
1. **Création d'un événement** : Un événement `click` est créé à l'aide du constructeur `Event`.  
2. **Déclenchement** : L'événement est déclenché sur un bouton via `dispatchEvent`.  
3. **Résultat** : Tout gestionnaire `click` associé au bouton sera exécuté.  

---  

### Création d'événements personnalisés  

#### `CustomEvent`  

**Définition :**  
Crée un événement personnalisé avec des données supplémentaires attachées.  

**Syntaxe :**  
 ```javascript  
let customEvent = new CustomEvent('nomEvenement', { detail: données });  
 ```  

**Breakdown de la syntaxe :**  
- **`CustomEvent`** : Constructeur pour créer des événements personnalisés.  
- **`'nomEvenement'`** : Nom de l'événement.  
- **`{ detail: données }`** : Objet contenant des données attachées à l'événement.  

**Exemple simple concret :**  
 ```javascript  
let element = document.querySelector('#customElement');  

// Création de l'événement  
let monEvenement = new CustomEvent('monEvenement', {  
    detail: { message: 'Salut, DOM !' }  
});  

// Écouteur pour l'événement  
element.addEventListener('monEvenement', (e) => {  
    console.log(e.detail.message);  
});  

// Déclenchement de l'événement  
element.dispatchEvent(monEvenement);  
 ```  

**Breakdown de l'exemple :**  
1. **Création d'un événement personnalisé** : `monEvenement` inclut des détails supplémentaires dans `detail`.  
2. **Ajout d'un écouteur** : L'écouteur intercepte l'événement et affiche les données de `detail`.  
3. **Déclenchement** : L'événement est déclenché, activant l'écouteur.  

---  
