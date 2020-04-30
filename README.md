# Reseptitietokanta

Web-sovellus reseptien tallennukseen, hakemiseen ja arvosteluun.

## Heroku

https://tsoha-cookbook.herokuapp.com/

## Asennus

### Paikallisesti

Asenna vaadittavat kirjastot komennolla
```
pip install -r requirements.txt
```
Tämän jälkeen voit käynnistää ohjelman komennolla
```
python run.py
```
Ohjelma käynnistyy osoitteeseen `http://localhost:5000`  
Voit halutessasi käynnistää ohjelman debug modessa komennolla
```
python run.py --debug
```
### Herokussa

Tarvitset [HerokuCLI](https://devcenter.heroku.com/articles/heroku-cli)  

Luo uusi sovellus Herokuun komennolla
```
heroku create <sovelluksen nimi>
```
Lisää tieto Herokusta paikalliseesn versionhallintaan komennolla
```
git remote add heroku https://git.heroku.com/<sovelluksen nimi>.git
```
Luo tarvittava ympäristömuuttuja komennolla
```
heroku config:set HEROKU=1
```
Lisää Herokuun tietokanta
```
heroku addons:add heroku-postgresql:hobby-dev
```
Lopuksi pushaa sovellus Herokuun
```
git push heroku master
```

## Dokumentaatio

[Käyttöohje](https://github.com/JakeKallioniemi/reseptitietokanta/blob/master/documentation/instructions.md)  
[Tietokannan kuvaus](https://github.com/JakeKallioniemi/reseptitietokanta/blob/master/documentation/database.md)  
[User storyt](https://github.com/JakeKallioniemi/reseptitietokanta/blob/master/documentation/user_stories.md)  
[Ongelmat, puutteet ja muuta pohdintaa](https://github.com/JakeKallioniemi/reseptitietokanta/blob/master/documentation/post-mortem.md)
