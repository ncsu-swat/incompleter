string_words = 'United States Declaration of Independence\nFrom Wikipedia, the free encyclopedia\nThe United States Declaration of Independence is the statement\nadopted by the Second Continental Congress meeting at the Pennsylvania State\nHouse (Independence Hall) in Philadelphia on July 4, 1776, which announced\nthat the thirteen American colonies, then at war with the Kingdom of Great\nBritain, regarded themselves as thirteen independent sovereign states, no longer\nunder British rule. These states would found a new nation – the United States of\nAmerica. John Adams was a leader in pushing for independence, which was passed\non July 2 with no opposing vote cast. A committee of five had already drafted the\nformal declaration, to be ready when Congress voted on independence.\n\nJohn Adams persuaded the committee to select Thomas Jefferson to compose the original\ndraft of the document, which Congress would edit to produce the final version.\nThe Declaration was ultimately a formal explanation of why Congress had voted on July\n2 to declare independence from Great Britain, more than a year after the outbreak of\nthe American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The\nSecond Day of July 1776, will be the most memorable Epocha, in the History of America."\nBut Independence Day is actually celebrated on July 4, the date that the Declaration of\nIndependence was approved.\n\nAfter ratifying the text on July 4, Congress issued the Declaration of Independence in\nseveral forms. It was initially published as the printed Dunlap broadside that was widely\ndistributed and read to the public. The source copy used for this printing has been lost,\nand may have been a copy in Thomas Jefferson\'s hand.[5] Jefferson\'s original draft, complete\nwith changes made by John Adams and Benjamin Franklin, and Jefferson\'s notes of changes made\nby Congress, are preserved at the Library of Congress. The best-known version of the Declaration\nis a signed copy that is displayed at the National Archives in Washington, D.C., and which is\npopularly regarded as the official document. This engrossed copy was ordered by Congress on\nJuly 19 and signed primarily on August 2.\n\nThe sources and interpretation of the Declaration have been the subject of much scholarly inquiry.\nThe Declaration justified the independence of the United States by listing colonial grievances against\nKing George III, and by asserting certain natural and legal rights, including a right of revolution.\nHaving served its original purpose in announcing independence, references to the text of the\nDeclaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric\n(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement\non human rights, particularly its second sentence:\n\nWe hold these truths to be self-evident, that all men are created equal, that they are endowed by their\nCreator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.\n\nThis has been called "one of the best-known sentences in the English language", containing "the most potent\nand consequential words in American history". The passage came to represent a moral standard to which\nthe United States should strive. This view was notably promoted by Abraham Lincoln, who considered the\nDeclaration to be the foundation of his political philosophy and argued that it is a statement of principles\nthrough which the United States Constitution should be interpreted.\n\nThe U.S. Declaration of Independence inspired many other similar documents in other countries, the first\nbeing the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands\n(modern-day Belgium). It also served as the primary model for numerous declarations of independence across\nEurope and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the\n19th century.'
word_freq = [word_list.count(n) for n in word_list]
print('String:\n {} \n'.format(string_words))
print('List:\n {} \n'.format(str(word_list)))
print('Pairs (Words and Frequencies:\n {}'.format(str(list(zip(word_list, word_freq)))))