---
Title: Seinfeld Script Data
Date: 2014-11-02 17:02:00
Modified: 2020-03-05 23:00:00
Category: data
Tags: seinfeld, seinfeld scripts
Slug: seinfeld-script-data
---

I grew up watching Seinfeld and for better or worse it formed a large part of my personality. I was too young to watch the early seasons live, but for the later ones I clearly remember the excitement I'd feel at 8:30pm Thursday night when Friends started because that meant it was only half an hour until Seinfeld would come on.

So when I was experimenting with various natural language processing algorithms I thought it'd be fun to use Seinfeld scripts as a corpus. I packaged up the scripts in a SQLite database, and this post outlines the schema and how you can interact with it.


### Data ###

If you want to generate this data yourself check out [the code on my github](http://github.com/colinpollock/seinfeld-scripts). If you just want the SQLite DB file please feel free to send me a message on github or email me.


### Database Schema ###

#### Episode ####
```sql
sqlite> .schema episode
CREATE TABLE episode(
    id INTEGER PRIMARY KEY,
    season_number INTEGER NOT NULL,
    episode_number INTEGER NOT NULL,
    title TEXT,
    the_date TEXT,
    writer TEXT,
    director TEXT,
    UNIQUE(season_number, episode_number)
);
```

```sql
sqlite> SELECT * FROM EPISODE LIMIT 1;
id	season_number	episode_number	title	the_date	writer	director
3	6	16	The Beard	February 9, 1995	Carol Leifer	Andy Ackerman
```


#### Utterance ####
```sql
sqlite> .schema utterance
CREATE TABLE utterance(
    id INTEGER PRIMARY KEY,
    episode_id INTEGER NOT NULL,
    utterance_number INTEGER NOT NULL,

    speaker TEXT NOT NULL,
    UNIQUE(episode_id, utterance_number),
    FOREIGN KEY(episode_id) REFERENCES episode(id)
);
```

```sql
sqlite> SELECT * FROM UTTERANCE LIMIT 1;
id	episode_id	utterance_number	speaker
1	1	1	JERRY
```


#### Sentence ####
```sql
sqlite> .schema sentence
CREATE TABLE sentence(
    id INTEGER PRIMARY KEY,
    utterance_id INTEGER NOT NULL,
    sentence_number INTEGER NOT NULL,
    text TEXT NOT NULL,
    UNIQUE(utterance_id, sentence_number),
    FOREIGN KEY(utterance_id) REFERENCES utterance(id)
);
```


```sql
sqlite> SELECT * FROM SENTENCE LIMIT 1;
id	utterance_id	sentence_number	text
3	1	3	It's too high!
```


### Some Simple Statistics ###

There are a lot of potentially interesting things to do with this data, most of which would require further processing. There are some basic but interesting questions that can be answered by simple SQL queries.


#### Which characters speak the most lines? ####

```sql
SELECT speaker, COUNT(*) AS count
FROM utterance
GROUP BY speaker
ORDER BY count DESC
LIMIT 10;

JERRY       14645
GEORGE      9613
ELAINE      7967
KRAMER      6656
NEWMAN      625
MORTY       502
HELEN       470
FRANK       429
SUSAN       382
ESTELLE     273
```

That seems about right-- the show is definitely dominated by the four main characters.


#### Which characters have speaking roles in the greatest number of episodes? ####

```sql
SELECT u.speaker, COUNT(DISTINCT e.id) AS num_episodes
FROM episode e JOIN utterance u ON e.id = u.episode_id
GROUP BY u.speaker
ORDER BY num_episodes DESC
LIMIT 10;

JERRY       173
GEORGE      171
KRAMER      170
ELAINE      169
MAN         53
WOMAN       44
NEWMAN      43
SUSAN       28
FRANK       26
ESTELLE     24
```

The appearances are also dominated by the main cast. Interestingly, some lines are attributed to "MAN" and "WOMAN", which points to some data quality issues. Ideally unnamed characters would have unique names like "MAN WATERING PLANTS".


### Project Ideas ###

#### Script Viewer ####
One of the main reasons I initially got this data together was to learn some front-end skills by developing a better UI for browsing through Seinfeld scripts. I had imagined all kinds of cross-linking between episodes and possibly links off to Wikipedia.

#### Exploration of the Characters ####
* Do particular characters have catch phrases (maybe high TF-IDF ngrams where TF is within the character's lines and IDF is for all speakers)?
* Are there characters who gain screen time over time?
* How many episodes are heavy on just a few of the main characters (e.g. a Jerry and George episode)?
* How positive, on average, are the various characters? Are there other interesting stylistic characteristics to look at?

#### Corpus for Exploring NLP Algorithms ####
I like playing with Wikipedia, but it'll be fun to have something a bit smaller and closer to my heart. It'd be fun to play around with language models and to generate sentences for particular characters (e.g. a Kramerish sentence).
