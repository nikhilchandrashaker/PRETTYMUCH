import csv, collections
S,E,A="single","EP","album"
NA="Non-album"
# year, date(ISO or partial), title, type, project, featured, label_era, precision, note
R=[
(2017,"2017-07","Would You Mind",S,"PrettyMuch So Far...","","Syco","month","Debut single; written by Savan Kotecha and Jacob Kasher"),
(2017,"2017-10","Teacher",S,"PrettyMuch So Far...","","Syco","month",""),
(2017,"2017-10-27","Open Arms",S,"PrettyMuch So Far...","","Syco","day",""),
(2017,"2017","No More",S,"PrettyMuch So Far...","French Montana","Syco","year","Performed on the UK X Factor final"),
(2018,"2018-03-23","PrettyMuch So Far...",E,"","","Syco","day",""),
(2018,"2018-02","10,000 Hours",S,"PRETTYMUCH an EP","","Syco","month","Single release approx.; EP followed April 19"),
(2018,"2018","Hello",S,"PRETTYMUCH an EP","","Syco","year",""),
(2018,"2018","Healthy",S,"PRETTYMUCH an EP","","Syco","year",""),
(2018,"2018","On My Way",S,"PRETTYMUCH an EP","","Syco","year",""),
(2018,"2018-04-19","PRETTYMUCH an EP",E,"","","Syco","day",""),
(2018,"2018-06-21","Summer on You",S,NA,"","Syco","day","Written by Ed Sheeran, produced by Steve Mac"),
(2018,"2018-09-28","Solita",S,NA,"Rich the Kid","Syco","day",""),
(2018,"2018-10-17","Real Friends",S,NA,"","Syco","day","Released to promote the Funktion Tour"),
(2018,"2018-12-14","Jello",S,NA,"","Syco","day",""),
(2019,"2019-01-25","Blind",S,NA,"","Syco","day",""),
(2019,"2019-04-26","Phases",S,"Phases - EP","","Syco","day",""),
(2019,"2019-05-20","Gone 2 Long",S,"Phases - EP","","Syco","day","Written and produced by Brandon Arreaga"),
(2019,"2019-05-24","Phases - EP",E,"","","Syco","day","Six songs"),
(2019,"2019","Eyes Off You",S,"Phases - EP","","Syco","year",""),
(2019,"2019-07-19","Lying",S,NA,"Lil Tjay","Syco","day",""),
(2019,"2019","Rock Witchu",S,NA,"","Syco","year",""),
(2019,"2019","Me Necesita",S,"INTL:EP","CNCO","Syco","year",""),
(2019,"2019","Up to You",S,"INTL:EP","NCT Dream","Syco","year",""),
(2019,"2019-11-22","INTL:EP",E,"","CNCO; NCT Dream; Luisa Sonza; Inigo Pascual","Syco","day",""),
(2021,"2021-01-22","Stars",S,"Smackables","","Sire","day","First release after the label change"),
(2021,"2021-01-29","Smackables",E,"","","Sire","day","First EP on Sire Records"),
(2021,"2021","Lonely",S,"Smackables (Deluxe Edition)","","Sire","year",""),
(2021,"2021-02-26","Smackables (Deluxe Edition)",E,"","","Sire","day","Adds Corpus Christi and the title track"),
(2021,"2021-07-30","Trust",S,NA,"","Sire","day","Video edited by Brandon Arreaga"),
(2021,"2021","I Don't Wanna Leave",S,NA,"Jeremih","Sire","year",""),
(2022,"2022","Talking 2 You",S,NA,"","Unconfirmed","year",""),
(2022,"2022-10-07","H2L",S,NA,"","Independent","day","Released on Sound.xyz; first release as a four-piece; not in the source's singles table"),
(2023,"2023","Same Place",S,"This Thing Called Love","","Independent","year",""),
(2023,"2023","Wrong?",S,"This Thing Called Love","","Independent","year",""),
(2023,"2023-03-31","Excited",S,"This Thing Called Love","","Independent","day","Released with Maria"),
(2023,"2023-03-31","Maria",S,"This Thing Called Love","","Independent","day","Released with Excited"),
(2023,"2023","Alone",S,"This Thing Called Love","","Independent","year",""),
(2023,"2023","Before You",S,NA,"angelbaby","Independent","year",""),
(2023,"2023-05-26","This Thing Called Love",A,"","","Independent","day","Debut studio album"),
]
V=[(2017,"Would You Mind","Emil Nava"),(2017,"Teacher","Noah Duran"),(2017,"Open Arms","Noah Duran"),(2017,"No More","Emil Nava"),(2018,"10,000 Hours","Noah Duran"),(2018,"Hello","Noah Duran"),(2018,"Summer on You","Tim Mattia"),(2018,"Jello","The Young Astronauts"),(2019,"Blind","The Young Astronauts"),(2019,"Phases","The Young Astronauts"),(2019,"Lying","The Young Astronauts"),(2019,"Me Necesita","Isaac Rentz"),(2019,"The Weekend","Isaac Rentz"),(2019,"Love","Isaac Rentz"),(2021,"Stars","Natalie Falt"),(2021,"Parking Spot","Steven Mertens"),(2021,"Free","Keenan O'Reilly"),(2021,"Lonely","Natalie Falt"),(2021,"Smackables","Ian Eastwood"),(2021,"Corpus Christi","Boni Mata"),(2021,"Trust","Ian Eastwood"),(2021,"I Don't Wanna Leave","Lucas Chemotti"),(2023,"Same Place","Brandon Arreaga"),(2023,"Excited","Brandon Arreaga"),(2023,"Alone","Brandon Arreaga")]
EV=[(2017,"appearance","Teen Choice Awards","Performed Would You Mind (August)","","confirmed"),
(2017,"appearance","MTV VMAs red carpet","Sang Would You Mind a cappella","","confirmed"),
(2017,"tour_support","Jack & Jack Tour","Opening act","","unverified (earlier search)"),
(2017,"appearance","MTV TRL","Performed Would You Mind (October)","","confirmed"),
(2017,"appearance","The X Factor UK final","Performed No More","","confirmed"),
(2018,"appearance","Good Morning America","Performed","2018-01-15","confirmed"),
(2018,"appearance","MTV TRL","Performed Open Arms and No More","2018-01-17","confirmed"),
(2018,"tour_headline","PrettyMuch Everywhere Tour","US tour","","confirmed"),
(2018,"tour_support","Roxy Tour","Opening act","","unverified (earlier search)"),
(2018,"appearance","The Late Late Show with James Corden","Performed Summer on You","","confirmed"),
(2018,"appearance","MTV VMAs","Push Artist Stage","2018-08-20","confirmed"),
(2018,"tour_headline","Funktion Tour","Fall headline tour","","confirmed"),
(2019,"tour_headline","FOMO Tour","Opened in Dallas with Kenzie Ziegler","2019-07-11","confirmed"),
(2020,"tour_support","Camila Cabello's The Romance Tour","Announced as opener for select US dates; cancelled (COVID-19)","2020-03-10","confirmed"),
(2021,"event","Smackables release party","Online party hosted by Moment House","2021-03-04","confirmed"),
(2021,"appearance","Good Morning America","Performed Stars","2021-03-16","confirmed")]
AW=[(2018,"iHeartRadio Music Awards","Best Boyband","Nominated"),(2018,"MTV Video Music Awards","Push Artist of the Year","Nominated"),(2018,"MTV Europe Music Awards","Best Push","Nominated"),(2018,"MTV Europe Music Awards","Best Group","Nominated (ambiguous in source)"),(2019,"Teen Choice Awards","Choice Music Group","Nominated"),(2019,"MTV Video Music Awards","Best Group","Nominated")]
M=[("Austin Porter","1997-08-14","Charlotte, North Carolina, US","2016-2023","","Solo pop album One Love (2013); unreleased rap EP"),
("Brandon Arreaga","1999-12-14","Corinth, Texas, US","2016-2023","","Writer/producer; last to join; directed 2023 videos"),
("Edwin Honoret","1999-02-12","The Bronx, New York, US","2016-2023","","Instagram covers"),
("Nick Mara","1997-11-08","Born New York; raised Englishtown, New Jersey, US","2016-2022","2022-10-07","ICONic Boyz dance crew; left for a solo career"),
("Zion Kuwonu","1999-06-29","Ottawa, Canada","2016-2023","","Vine covers; noticed by Sony Music")]
def w(n,h,rows):
    with open(n,"w",newline="",encoding="utf-8") as f:
        c=csv.writer(f);c.writerow(h);c.writerows(rows)
w("releases.csv",["year","release_date","title","type","project","featured_artist","label_era","date_precision","notes"],R)
w("videos.csv",["year","title","director"],V)
w("events.csv",["year","category","name","detail","date","verification"],EV)
w("awards.csv",["year","award","category","result"],AW)
w("members.csv",["name","born","origin","years_in_group","left_date","notes"],M)
cnt=collections.Counter(r[0] for r in R)
era={2016:"Syco",2017:"Syco",2018:"Syco",2019:"Syco",2020:"Label change",2021:"Sire",2022:"Independent",2023:"Independent"}
mem={2016:5,2017:5,2018:5,2019:5,2020:5,2021:5,2022:4,2023:0}
w("timeline.csv",["year","era","members_at_year_end","releases_in_dataset","videos_in_dataset"],[(y,era[y],mem[y],cnt.get(y,0),sum(1 for v in V if v[0]==y)) for y in range(2016,2024)])
print(len(R),collections.Counter(r[3] for r in R),len(V),len(EV),len(AW))
