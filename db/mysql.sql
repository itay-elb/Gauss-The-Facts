use project;

create table facts(
    fact_id integer primary key auto_increment,
    true_a varchar(30),
    false_a varchar(30),
    answer varchar(500),
    question varchar(300)
);

insert into facts (true_a,false_a,answer,question) values
("Suden","Egypt","Sudan has more pyramids than any country in the world","Which country has the most pyramids?"),
("96,560km","154.8km"," The circulatory system is more than 96,560km long!","how long is are circulatory"),
("Texas","German","German chocolate cake was invented in Texas","German chocolate cake was invented in?"),
("rubber ducks","cars","In 1992, a cargo ship carrying approximately 29,000 bath toys spilled in the northern Pacific Ocean.",
"in 1992 a large shipment of _____ is lost at sea" ),
("8","11","there are identical, fraternal, half-identical,mirror image, mixed, chromosome, superfecundation, and superfetation .",
"There are___different types of twins."),
("No","Yes","no, but they can swim up to speeds of 25 mph.","Penguins can fly?"),
("No","Yes","It is Minerva. Minnie Mouse is a nickname that was given to the character by Ub Iwerks and Walt Disney. Minnie’s actual name is rarely used. ",
"Minnie the Mouse’s real name is Minnie?"),
("70-80","50-60","75 burgers are sold in McDonald’s every second.","how match Mcburgers are sold in seconds?"),
("False","True","False. You can’t hum while holding your nose.","True or False: You can hum while holding your nose?"),
("False","True","False. Your eyeballs do not grow or change their size as you age.","True or False: your eyeballs grow over the yers?"),
("Australia","The Moon","The moon sits at 3,400 kilometers in diameter, while Australia’s diameter from east to west is almost 4,000 km.","who is wider?"),
("Yes","No","There is,Scotland chose the unicorn as its national animal.","Is there any country that has chosen a mystical animal as its national animal?"),
("fruits","vegetables","Avocados are fruits because they are single-seeded berries.","Avocados is a____"),
("Ketchup","Mayonnaise","Ketchup used to be sold as medicine.","What sauce is sold as medicine?"),
("No","Yes","No, Pigs can't look up into the sky.","Pigs can see the sky?"),
("car mechanic","Operational compassion","During World War II, Queen Elizabeth worked as a car mechanic","Where did Queen Elizabeth work during World War II?"),
("on your birthday","On a day when you feel bad","According to a long-term Swiss study, your chance of dying on your birthday is 13.8% higher than any other day of the year",
"On which day are you more likely to die?"),
("False","True","False, Honey never spoils. If it is stored correctly, you can eat honey even 3,000 years after production","True or False: Does honey spoil?"),
("True","False","True, Apple seeds contain cyanide","True or False: Can apples be dangerous?"),
("not new","yes new","If 3D technology seems relatively new to you, know that the first 3D film was shown somewhere in 1922","Is 3D technology new?");

 create table fansfacts(
    fact_id integer primary key auto_increment,
    fact varchar (500),
    question varchar (300),
    true_option varchar(30),
    false_option varchar(30)
 );
