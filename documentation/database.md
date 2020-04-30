# Tietokannan kuvaus

Recipe ja Review tauluihin löytyy täysi CRUD toiminnallisuus. 

## Tietokantakaavio
![Tietokantakaavio](https://github.com/JakeKallioniemi/reseptitietokanta/blob/master/documentation/final_diagram.png)

## CREATE TABLE-lauseet

#### Account-taulu
```
CREATE TABLE account (
  id INTEGER NOT NULL,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(144) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (username)
)
```
#### Recipe-taulu
```
CREATE TABLE recipe (
  id INTEGER NOT NULL,
  name VARCHAR(50) NOT NULL,
  duration INTEGER NOT NULL,
  instructions TEXT NOT NULL,
  account_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY(account_id) REFERENCES account (id)
)
```
#### Tag-taulu
```
CREATE TABLE tag (
  id INTEGER NOT NULL,
  name VARCHAR(50) NOT NULL,
  category VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
)
```
#### RecipeTag-taulu
```
CREATE TABLE recipe_tag (
  recipe_id INTEGER,
  tag_id INTEGER,
  FOREIGN KEY(recipe_id) REFERENCES recipe (id),
  FOREIGN KEY(tag_id) REFERENCES tag (id)
)
```
#### Review-taulu
```
CREATE TABLE review (
  id INTEGER NOT NULL,
  rating INTEGER NOT NULL,
  recipe_id INTEGER NOT NULL,
  account_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(recipe_id) REFERENCES recipe (id),
  FOREIGN KEY(account_id) REFERENCES account (id)
)
```
## Indeksit

```
CREATE INDEX ix_recipe_duration ON recipe (duration)
CREATE INDEX ix_recipe_name ON recipe (name)
CREATE INDEX ix_review_rating ON review (rating)
```
## Tietokannan alustus
Kun ohjelma käynnistetään tarkistetaan onko tagit tietokannassa
```
SELECT * FROM tag
```
jos ei niin ne lisätään
```
INSERT INTO tag (name, category) VALUES ('Appetizer', 'course'),('Main course', 'course'),
    ('Dessert', 'course'),('Snack', 'course'),('Breakfast', 'course'),('Dairy-Free', 'diet'),
    ('Gluten-Free', 'diet'),('Vegan', 'diet')
```
