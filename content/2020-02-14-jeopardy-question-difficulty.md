---
Title: Jeopardy Question Difficulty
Date: 2020-02-14
Category:
Tags: jeopardy
Description: Everyone who watches Jeopardy knows the $1000 question is harder than the $200 question. But how much harder? And how does difficulty compare between rounds? How difficult are Daily Doubles and Final Jeopardy compared to other questions? This post will answer each of these questions, and also explore how difficulty varies by category.
Slug: jeopardy-question-difficulty
---

I made [Trivia Trainer][1] to help myself (and other aspiring Jeopardy contestants) get better at Trivia. It works by allowing users to quiz themselves on questions in 53 specific categories (e.g. Literature, Sports, Geography) so that they can track their improvement and identify their weaknesses.

Unlike on Jeopardy (where usually only a single contestant answers a question), on Trivia Trainer many users answer the same question so the percentage of attempts that are correct nicely captures how easy a question is. Throughout this post I call this _percent correct_. And for any given grouping of questions (e.g. Final Jeopardy questions) the percent correct is simply the average percentage correct across all questions in that group.

In this post I'll explore how Jeopardy question difficulty varies by question type. __Specifically, in this post I'll cover:__

* __How does difficulty increase within a round?__ Is a $400 question twice as difficult as a $200 question?
* __How does difficulty compare between rounds?__ Is a $400 question in the Jeopardy round actually the same difficulty as a $400 question in the Double Jeopardy round?
* __How difficult are Daily Doubles relative to other questions in their round?__
* __What about Final jeopardy?__

And since Trivia Trainer organizes questions into 53 categories I wanted to see how difficulty varied by category.

(A quick sidenote: all information here is in aggregate and no individual Trivia Trainer user’s data will ever be shared or made public.)


## How does Difficulty Increase within the Jeopardy Round?

![Percent correct in the Jeopardy round](/images/jeopardy-question-difficulty/first-round.png "Percent correct in the Jeopardy round")

For every step down the board the correct rate drops by about 7%, from 72% down to 43%. The decrease in percentage correct (i.e. increase in difficulty) makes sense since Jeopardy writers presumably try to increase the difficulty of each question in a round, so when averaging across tens of thousands of questions at each dollar value that trend shows up. Still, I was surprised the change was so regular.


## How do the Jeopardy and Double Jeopardy Rounds Compare?

The plot below contains the same information as the first one but adds in the Double Jeopardy Round.

![Percent correct in the Jeopardy and Double Jeopardy rounds](/images/jeopardy-question-difficulty/first-and-second-rounds.png "Percent correct in the Jeopardy and Double Jeopardy rounds")


The Double Jeopardy round starts out more difficult (72% vs 68% for the first question) and is more difficult at each step down the board.

Both rounds show the same linearly decreasing relationship in percent correct, but Double Jeopardy’s difficulty increases a little more quickly, with percent correct dropping 8.2% at each new depth compared to just 7% for the first round.

Interestingly the difficulty isn’t dependent on dollar value: the $400 and $800 questions in the Jeopardy round are respectively easier than the $400 and $800 questions in the Double Jeopardy round.


## How Difficult are Daily Doubles and Final Jeopardy?

The plot below shows all the values in the Jeopardy and Double Jeopardy rounds, which we already saw above. It also has the Daily Double in each round and Final Jeopardy.

![Percent correct in all rounds](/images/jeopardy-question-difficulty/three-rounds-and-DD.png "Percent correct in all rounds")

In the Jeopardy Round the Daily Double is correct 53% of the time, making it comparably difficult to the depth four question ($800) in the Jeopardy Round at 52%. In the Double Jeopardy round the Daily Double is correct 46.5% of the time, putting it closest to the depth three question $1200) at 49% correct.

Overall this suggests that Jeopardy clue creators are attempting to make Daily Doubles about as difficult as where they show up, which according to [this interesting Reddit post][2] is centered on the second to last row in a given category. I suspect that the writers first create the board and after decide where to put the Daily Double, so a Daily Double found in the $1200 square would be easier than one found in the $1600 square. Unfortunately my dataset only indicates a question is a Daily Double but not where on the board it was found so I couldn’t verify this.

At 39% correct Final Jeopardy falls in between the second hardest (42% for $1600) and hardest (35% for $2000) questions in the Double Jeopardy round. Trivia Trainer users typically only take a few seconds to respond to questions, including the Final Jeopardy question, so I was expecting the percentage correct to be lower here since Final Jeopardy usually requires some time to think a little more creatively.


## How does Difficulty Vary Across Categories?

Here are the percent correct values for the twenty most popular categories in Trivia Trainer. For reference, the global average across all questions in all categories is 53%.

![Percent correct by category](/images/jeopardy-question-difficulty/by-category.png "Percent correct by category")

Unsurprisingly (at least for me) the most challenging category is Literature. It’s both very wide and deep, and tends to be very academic. Compare this with something like Wordplay that typically doesn’t require very specific knowledge.

We can get a little more granular here and dig into Literature, which encompasses many Jeopardy categories like “Short Stories”, “Novels”, etc.

![Percent correct by literature category](/images/jeopardy-question-difficulty/within-literature.png "Percent correct by literature category")

Let me know if there are things you think I should look at or if you’ve done a similar analysis!

[1]: http://www.trivia-trainer.com/?blog
[2]: https://www.reddit.com/r/Jeopardy/comments/bs6fyz/locations_of_daily_doubles/
