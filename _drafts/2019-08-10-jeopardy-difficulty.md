---
layout: post
title:  "Jeopardy Difficulty"
tags: jeopardy
---


Anyone who watches Jeopardy knows that the first question in a category is usually a gimme (e.g. "PRESIDENTS: this president" todo: use a real one). And things definitely get harder. But I was curious exactly how much harder they get. Is a $400 question twice as hard as a $200 question? Is an $800 question in the first round exactly as hard as an $800 question in the second round? And what about Final Jeopardy-- are those way harder than everything else?


How to do it
------------

If we have a way of assigning a difficulty score to an individual question then we can just aggregate across all questions in each square on the board (the difficulty for R1 $200 questions would be the average difficulty for all R1 $200 questions). So how can we get that difficulty score?

How could you calculate the difficulty of different rounds and values? One way is to get a bunch of people to answer each question and have the proportion of people who get it right be the difficulty. We can *almost* do this using actual Jeopardy game data, but the Jeopardy format causes an issue: as soon as a contestant answers correctly no one else can ring in and we're left with no data on how many people knew the answer. I do think this would be possible to do this, as I outlined in {this section below}, but for now let's consider another approach.

Users of the website [Trivia Trainer](trivia-trainer.com) answer thousands of Jeopardy questions per day. Unlike Jeopardy where only a single contestant answers a question on Trivia Trainer many users answer the same question.

So we can get our difficulty score simply for a question simply by taking the average number of users who got the question right the first time they saw it.

[[ put note about never revealing non-aggregate data]]




### How does difficulty increase in a round? ###

[[plot showing increasing difficulty in R1]]
How would you expect difficulty to increase as the dollar amount increases in the first
round? It turns out that there is a gradual increase in difficulty from the $200 to the
$1000 question. This makes sense since Jeopardy clue writers presumably try to increase
the difficulty in each question in a round, so when averaging across tens of thousands
of questions at each dollar value that trend shows through.

Trivia Trainer users get about {{}} of $200 questions correctly. For every step down the
board the correct rate drops by about 5%, all the way down to {{}}% for the $1000
question. It's surprising and amazing how regular this is.



### How do the first and second round compare? ###
How much more difficult would you expect the second round to be? Is the easiest question
in the second round more difficult than the hardest question in the first round? Are all
the questions in the second round harder than all the questions in the first round?

The difficulty of the dollar values on the second 
* is the rate drop the same?
* is the start the same?


### What about Final Jeopardy? ###
Interestingly Final Jeopardy questions are a little easier than the $2000 question from
the second round, but harder than all other questions. I was surprised by this because
I expected Final Jeopardy questions to be harder than all other

 I've heard from a number of
Trivia Trainer users that they try to move through questions fairly quickly


### What about Double Jeopardy? ###
Are all Double Jeopardy questions the same difficulty, or does the difficulty depend on where they're found (i.e. is a DD question found in the $800 row the same difficulty as
one found in the $1000 row)?

This question is particularly interesting since it has implications for actual strategy.
If you know that a DD's difficulty depends on where it's found on the board and that you
came across it on the bottom row then you may want to wager lightly. On the other hand,
if you know the difficulty is similar to that of a $400 question and you found the $400
question to be fairly easy then you probably want to wager more.



### Different Categories ###

Trivia Trainer organizes Jeopardy questions into 53 different categories in order to
help users focus their studying efforts. So naturally I was curious whether the same
trends help for all categories.

things to look at:
* 


All categories have the same general trends that we saw before (difficulty increases
linearly as the dollar value increases), but they have different baseline difficulties.

Literature is the most difficult category at a correct rate of {{}}%. Its $200 question
is answered correctly {{}}% of the time, and 
For example, Literature, the most difficult category at {{}}% correct on average, has



For example, Trivia Trainer users get {{}}% of Literature questions correct on average.




While different categories have different baseline difficulties the trend does hold.

Other Ways to Slice the Data
----------------------------
This post examines how a question's difficulty depends on its round and dollar value. There
are some other interesting ways we could potentially slice the data:
* How do the difficulty of Teen, College, and Teacher Jeopardy relate to each other and
  to standard Jeopardy.



Using Jeopardy instead of Trivia Trainer
----------------------------------------
So here's how I thought about approaching this. I could pull down Jeopardy data from j-archive and for each question get the number of contestants who rang in and how many were incorrect. I could then score each question using the following table:
[[]]

The basic intuition is this: a question's difficulty is the number of people that *may* have known the answer. So if the first contestant answers the question correctly all three contestants may have known the answer. If no contestants ring in then zero could have known the answer. If one rings in and is incorrect and then another rings in and is correct then two contestants could have known the answer.

It may be true that an incorrect guess means a question is harder than no guess, since if a contestant is willing to try they probably have some idea about the answer.

The main challenge here is that Jeopardy contestants are really good. And there are three really good contestants who get to answer a question correctly and censure all our amazing data.

This presents a challenge because with correctness rates all super high we need more statistical power to measure meaningful differences between them. We could get that statistical power by looking at tons of questions. I suspect that if I looked at thousands of games there would be some patterns. So even if the R1 $200 question is answered correctly by the first contestant 99% of the time it's probably the case that the R1 $400 question is answered correctly by a little less often, maybe 98% of of the time.

I think that if we plotted this for all squares on the two boards (single and double Jeopardy) there would be a trend of correct rates decreasing as we got further down the board. But the numbers wouldn't be as interpretable as when using the Trivia Trainer data, where "55%" means "55% of users got this right".

