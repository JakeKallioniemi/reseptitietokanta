# Post-mortem

## Toteutumatta jääneet toiminnallisuudet

Alussa oli tarkoitus, että reseptiin voisi liittää raaka-aineita ja että niiden perusteella voisi hakea reseptejä. Tämä jäi toteuttamatta, mutta tarvittavat raaka-aineet voi kuitenkin kirjoittaa reseptin ohjekenttään. Myös muita hakutoimintoja jäi toteuttamatta esim. valmistusajan perusteella. Minkäänlaista järjestämis mahdollisuutta en myöskään ehtinyt toteuttaa.

Profiilisivu oli viimehetken lisäys ja sen toiminnallisuus jäi sen takia pieneksi. Esimerkiksi lisää tilastoja ja pelkästään omien reseptien listaus voisivat olla mahdollisia lisätoiminnallisuuksia. Myös asetukset ja vaikkapa salasanan vaihto voisivat olla hyviä lisäyksiä. Mahdollisuus muiden henkilöiden profiilien tarkasteluuun ja linkki reseptistä sen tekijän profiiliin tekisi sivusta hyödyllisemmän.

## Ongelmat ja puutteet

- Reseptien listauksessa ei ole käytetty sivutusta, vaikka käyttäjän on mahdollista hakea kaikki tietokannassa olevat reseptit
- Haussa tag-kenttä on tekstikenttä eikä drop-down menu, mikä on hölmöä sillä kaikki tagit on valmiiksi määritelty tietokantaan ja niitä on pieni määrä.
- Hakua tehdessä käyetetyt arvot eivät jää näkyviin lomakkeeseen.
- Haussa rating-kenttää ei ole rajoitettu välille 1-5. Varsinaisesti kyseessä ei kuitenkaan ole suuri ongelma sillä haku toimii odotetulla tavalla.
- Haussa sekä arvioinnissa tehdään validointia, mutta käyttäjälle ei anneta minkäänlaista virheviestiä.
- Sovellus on ulkonäöltään käyttökelpoinen, mutta esimerkiksi reseptin luonnissa kenttiä ei ole aseteltu kovin siististi.
- Resepteistä on hyvin vähän tietoa listauksessa. Hakuja voi tehdä arvosanan ja tagien perusteella mutta ne eivät näy suoraan listauksessa.

## Työtavat ja välineet

- Ajankäyttö oli melko huonoa. Työtä tuli tehtyä aina juuri ennen deadlinea.
- Todennäköisesti olisi ollut helpompaa käyttää PostgreSQL-tietokantaa myös paikallisesti.
- Olisi pitänyt käyttää enemmän aikaa kätettyjen työkalujen dokumentoinnin lukemiseen. Hyödyllisiä ominaisuuksia jäi nyt käyttämättä.

## Mikä meni hyvin

- Sovelluksen laajuus oli sopiva tämän kurssin puitteisiin.
- Valitut toiminnallisuudet olivat vaikeustasoltaan sopivia, en jäänyt jumiin mihinkään kovin pitkäksi aikaa.
- Sovellusta voi laajentaa melko helposti.
