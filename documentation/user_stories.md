# User stories ja toimintoja vastaavat SQL-lauseet

## Käyttäjäryhmät

Sovelluksen käyttäjäryhminä ovat kirjautuneet ja kirjautumattomat käyttäjät. Kirjautunut käyttäjä pystyy tekemään myös kaikki kirjautumattoman käyttäjän toiminnot paitsi uuden käyttäjän luonti, jota varten täytyy kirjautua ulos.

## Rekisteröinti ja kirjautuminen

- [x] Käyttäjänä voin luoda uuden tilin
  ```
  INSERT INTO account (username, password) VALUES (?, ?)
  ```
- [x] Käyttäjänä voin kirjatua olemassa olevalle tililleni
  ```
  SELECT account.id AS account_id, account.username AS account_username, account.password AS account_password 
  FROM account 
  WHERE account.id = ?
  ```

## Reseptit

- [x] Kirjautuneena käyttäjänä voin lisätä reseptejä  
  - Haetaan halutut tagit tietokannasta
    ```
    SELECT tag.id AS tag_id, tag.name AS tag_name, tag.category AS tag_category 
    FROM tag
    ```
  - Lisätään resepti
    ```
    INSERT INTO recipe (name, duration, instructions, account_id) VALUES (?, ?, ?, ?)
    ```
  - Yhdistetään tagit reseptiin
    ```
    INSERT INTO recipe_tag (recipe_id, tag_id) VALUES (?, ?)
    ```  
- [x] Kirjautuneena käyttäjänä voin muokata omia reseptejäni
  - Tässä on muokattu ainoastaan nimeä
    ```
    UPDATE recipe SET name=? WHERE recipe.id = ?
    ```
  - Jos tageja muutetaan vanhat yhteydet poistetaan
    ```
    DELETE FROM recipe_tag WHERE recipe_tag.recipe_id = ? AND recipe_tag.tag_id = ?
    ```
  - Ja uudet yhteydet lisätään samalla tavalla kuin reseptin lisäyksessä
  
- [x] Kirjautuneena käyttäjänä voin poistaa omia reseptejäni
  - Ensin poistetaan mahdolliset tagit ja arvostelut (nämä kyselyt näkyvät muissa storyissa), sitten poistetaan itse resepti
    ```
    DELETE FROM recipe WHERE recipe.id = ?
    ```
- [x] Käyttäjänä voin selata reseptejä
  ```
  SELECT recipe.id, recipe.name, recipe.duration FROM recipe
  ```
- [x] Käyttäjänä voin lukea tietyn reseptin tiedot
  - Haetaan resepti
    ```
    SELECT recipe.id AS recipe_id, recipe.name AS recipe_name, recipe.duration AS recipe_duration, recipe.instructions AS recipe_instructions, recipe.account_id AS recipe_account_id 
    FROM recipe 
    WHERE recipe.id = ?
    ```
  - Haetaan reseptiin liittyvät tagit
    ```
    SELECT tag.id AS tag_id, tag.name AS tag_name, tag.category AS tag_category 
    FROM tag, recipe_tag 
    WHERE ? = recipe_tag.recipe_id AND tag.id = recipe_tag.tag_id
    ```
- [x] Käyttäjänä voin nähdä tietokannassa olevien reseptien määrän
  ```
  SELECT COUNT(recipe.id) FROM recipe
  ```

## Arvostelu

- [x] Kirjautuneena käyttäjänä voin arvostella reseptejä
  ```
  INSERT INTO review (rating, recipe_id, account_id) VALUES (?, ?, ?)
  ```
- [x] Kirjautuneena käyttäjänä voin muuttaa arvostelujani
  ```
  UPDATE review SET rating=? WHERE review.id = ?
  ```
- [x] Kirjautuneena käyttäjänä voin poistaa arvostelujani
  ```
  DELETE FROM review WHERE review.account_id = ? AND review.recipe_id = ?
  ```
- [x] Käyttäjänä voin nähdä reseptien saamien arvosteluiden keskiarvon
  ```
  SELECT ROUND(AVG(rating), 1) FROM Review WHERE recipe_id = ?
  ```
- [x] Kirjautuneena käyttäjänä voin nähdä kaikkien lisäämieni reseptien keskiarvon
  ```
  SELECT ROUND(AVG(average_rating), 2) FROM (
    SELECT AVG(rating) AS average_rating FROM review
    INNER JOIN account ON review.account_id = account.id
    INNER JOIN recipe ON review.recipe_id = recipe.id
    WHERE recipe.account_id = ?
    GROUP BY recipe.id
  ) AS averages
  ```

## Haku ja järjestäminen

- [ ] Käyttäjänä voin järjestää reseptejä arvosanan perusteella
- [x] Käyttäjänä voin hakea reseptejä arvosanan perusteella
  ```
  SELECT recipe.id, recipe.name, recipe.duration FROM recipe
  LEFT JOIN review ON review.recipe_id = recipe.id
  GROUP BY recipe.id
  HAVING AVG(review.rating) >= ?
  ```
- [x] Käyttäjänä voin hakea reseptejä nimen perusteella
  ```
  SELECT recipe.id, recipe.name, recipe.duration FROM recipe
  WHERE recipe.name LIKE ?
  ```
- [x] Käyttäjänä voin hakea reseptejä tagien perusteella
  ```
  SELECT recipe.id, recipe.name, recipe.duration FROM recipe
  LEFT JOIN recipe_tag ON recipe_tag.recipe_id = recipe.id
  INNER JOIN tag ON tag.id = recipe_tag.tag_id
  WHERE UPPER(tag.name) = ?
  ```
- [ ] Käyttäjänä voin hakea reseptejä valmistusajan perusteella
- [ ] Käyttäjänä voin hakea reseptejä ainesosien perusteella
- [x] Käyttäjänä voin hakea reseptejä useammalla kriteerillä samaan aikaan
  - Haku useammalla kriteereillä on yhdistelmä aiempia hakuja. Haun muoto riippuu siitä mitä kriteerejä käytetään. Tässä esimerkkikyselyssä on käytetty kaikkia kolmea hakukriteeriä.
    ```
    SELECT recipe.id, recipe.name, recipe.duration FROM recipe
    LEFT JOIN review ON review.recipe_id = recipe.id
    LEFT JOIN recipe_tag ON recipe_tag.recipe_id = recipe.id
    INNER JOIN tag ON tag.id = recipe_tag.tag_id
    WHERE UPPER(tag.name) = ? AND recipe.name LIKE ?
    GROUP BY recipe.id
    HAVING AVG(review.rating) >= ?
    ```
