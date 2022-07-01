"""
@author: jhalls

"""


from gensim.summarization import summarize, keywords
text = "A. Introduction" + \
" The Nirmohi Akhara represents a religious sect amongst the Hindus,"+ \
"known as the Ramanandi Bairagis. The Nirmohis claim that they were, at all"+\
"material times, in charge and management of the structure at the disputed site"+\
"which according to them was a ‗temple‘ until 29 December 1949, on which date"+\
"an attachment was ordered under Section 145 of the Code of Criminal Procedure "+\
"1898. In effect, they claim as shebaits in service of the deity, managing its affairs"+\
"and receiving offerings from devotees. Theirs is a Suit of 1959 for the"+\
"management and charge of ‗the temple‘."+\
" The Uttar Pradesh Sunni Central Board of Waqf (―Sunni Central Waqf"+\
"Board‖) and other Muslim residents of Ayodhya instituted a suit in 1961 for a"+\
"declaration of their title to the disputed site. According to them, the old structure"+\
"was a mosque which was built on the instructions of Emperor Babur by Mir Baqi"+\
"who was the Commander of his forces, following the conquest of the subcontinent by the Mughal Emperor in the third decade of the sixteenth century."+\
"The Muslims deny that the mosque was constructed on the site of a destroyed"+\
"temple. According to them, prayers were uninterruptedly offered in the mosque"+\
"until 23 December 1949 when a group of Hindus desecrated it by placing idols"+\
"within the precincts of its three-domed structure with the intent to destroy,"+\
"damage and defile the Islamic religious structure. The Sunni Central Waqf Board"+\
"claims a declaration of title and, if found necessary, a decree for possession."+\
"7. A suit was instituted in 1989 by a next friend on behalf of the deity"+\
"(―Bhagwan Shri Ram Virajman‖) and the birth-place of Lord Ram (―Asthan Shri"+\
"Ram Janmabhumi‖). The suit is founded on the claim that the law recognises"+\
"both the idol and the birth-place as juridical entities. The claim is that the place of"+\
"birth is sanctified as an object of worship, personifying the divine spirit of Lord"+\
"Ram. Hence, like the idol (which the law recognises as a juridical entity), the"+\
"place of birth of the deity is claimed to be a legal person, or as it is described in"+\
"legal parlance, to possess a juridical status. A declaration of title to the disputed "+\
"site coupled with injunctive relief has been sought."+\
" These suits, together with a separate suit by Hindu worshippers were"+\
"transferred by the Allahabad High Court to itself for trial from the civil court at"+\
"Faizabad. The High Court rendered a judgment in original proceedings arising"+\
"out of the four suits and these appeals arise out of the decision of a Full Bench"+\
"dated 30 September 2010. The High Court held that the suits filed by the Sunni"+\
"Central Waqf Board and by Nirmohi Akhara were barred by limitation. Despite"+\
"having held that those two suits were barred by time, the High Court held in a"+\
"split 2:1 verdict that the Hindu and Muslim parties were joint holders of the"+\
"disputed premises. Each of them was held entitled to one third of the disputed"+\
"property. The Nirmohi Akhara was granted the remaining one third. A preliminary"+\
"decree to that effect was passed in the suit brought by the idol and the birth-place"+\
"of Lord Ram through the next friend."

print(summarize(text))
print('\n keywords \n', keywords(text))
