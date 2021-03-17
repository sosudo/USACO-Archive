# Problem Statement
Alice and Barbara played some friendly games of one-on-one basketball after work, and you agreed to help them keep score. The rules of the game were simple:
> Each successful shot by a player earns them either one or two points. <br>
> The first player to eleven points wins, with one exception. <br>
> If the score is tied 10–10, the previous rule is replaced by a “win by 2” rule: the first player to lead the other by at least two points wins.<br>

So for example, 11–7, 9–11, and 14–12 are possible final scores (but not 14–13).

Whenever Alice or Barbara scored points, you jotted down an A or B (indicating a score by Alice or by Barbara) followed by a 1 or 2 (the number of points scored). You have some records of the games Alice and Barbara played in this format, but do not remember who won each game. Can you reconstruct the winner from the game record?

# Input
The input consists of a single line with no more than 200 characters: the record of one game. The record consists of single letters (either A or B) alternating with single numbers (either 1 or 2), and includes no spaces or other extraneous characters. Each record will be a correct scoring history of a single completed game, played under the rules described above.

# Output
Print a single character, either A or B: the winner of the recorded game.

# Sample 1
> Input: A2B1A2B2A1A2A2A2<br>
> Output: A

# Sample 2
> Input: A2B2A1B2A2B1A2B2A1B2A1A1B1A1A2<br>
> Output: A

# Reference
Problem Link: https://open.kattis.com/contests/mcpc19open/problems/basketballoneonone<br>
Problem ID: basketballoneonone<br>
Runtime Limit: 1s<br>
Memory Limit: 1024MB<br>
Difficulty: 1.7 (Very Easy)<br>
Sample Data Link: https://open.kattis.com/problems/basketballoneonone/file/statement/samples.zip<br>
Authors: Jingbo Shang, Etienne Vouga<br>
Source: 2019 ICPC Mid-Central Regional<br>
License: Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)

# Status
Annotated<br>
Runtime: 0.06s<br>
Filesize: 2485B<br>
