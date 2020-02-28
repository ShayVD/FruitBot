## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- goodbye
- goodbye
- cya l8r
- goodbye Adam
- see you late
- bye
- goodbye
- see you later
- thanks goodbye
- see you

## intent:affirm
- indeed
- of course
- that sounds good
- correct
- yep
- aye
- do
- yup
- yes
- indeed
- of course
- that sounds good
- correct
- okay then
- It sure does
- Yes please
- sure
- Yes

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- not a hope
- not right now
- Nope
- Nah
- I dont want to
- I said I'm fine
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:why
- why
- what for?
- Why?
- How come
- why is that?
- why should I pay?
- I don't see how that matters
- I don't see how that's relevant
- does that affect how much carbon there is?
- for what reason?
- how does that make a difference
- how is that important
- ok why tho
- what are you asking that for
- what difference does it make
- what do you mean?
- wdym

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:enter_data
- my name is [Shay van Dam](NAME)
- my name is [John Smith](NAME)
- my name is [Alisson Pearson](NAME)
- i am [jane doe](NAME)
- i am [anna reardon](NAME)
- i am [Shaun King](NAME)
- I'm [Donald Glover](NAME)
- I'm [Emma Tracey](NAME)
- I'm [Lindsay Lohan](NAME)
- [shauna hamilton](NAME)
- [jessie jackson](NAME)
- [Graham Burke](NAME)
- my email is [shay.van.dam@maverick-intl.com](EMAIL)
- my email is [j.smith@gmail.com](EMAIL)
- my email is [a.odonoghue@hotmail.co.uk](EMAIL)
- [john@johnson.john](EMAIL)
- [test@example.com](EMAIL)
- [shay@email.com](EMAIL)
- [cathal@cathaltoomey.com](EMAIL)

## intent:what_fruit
- what fruit do you have
- what fruit is there?
- what is there
- what is available
- what is your fruit range
- what fruit?

## intent:want_fruit
- i want fruit
- Id like some fruit
- okay i want fruit
- buy fruit
- order fruit

## intent:thank
- thank you
- thanks
- Thanks a million
- thanking you

## intent:tell_joke
- do you know any jokes?
- tell me a joke
- any jokes?
- Have you a joke for me?

## regex:EMAIL
- \b(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])\b
