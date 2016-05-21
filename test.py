from kayfuncs import *
import networkx as nx
import matplotlib.pyplot as plt
import itertools as itr
from collections import Counter
import operator

from kayfuncs import *


st = "I went and saw this movie last night after being coaxed to by a few friends of mine. I'll admit that I was reluctant to see it because from what I knew of Ashton Kutcher he was only able to do comedy. I was wrong. Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism. The sign of a good movie is that it can toy with our emotions. This one did exactly that. The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half."
st1 = """LACKAWANNA BLUES is a fine stage play by Ruben Santiago-Hudson and an even finer film as the author adapted his own life story for the screen. This brilliant film ignites the screen with rich colors, fine music, brilliant editing, superb direction by George C. Wolfe, and a cast so stunning that they make an encore viewing compulsory! Yes, it is just that good.<br /><br />The story is based on the author's life as the child 'Junior' (Marcus Carl Franklin) raised in the inimitable home of soulfully empathetic Rachel "Nanny" Crosby (S. Epatha Merkerson), a lady who devoted her life to aiding the disenfranchised by transporting them from the South, from mental hospitals, and from the streets to Lackawanna, New York. The boy recalls all the lessons he learned about life from the inhabitants of the house - odd characters with painful pasts - and from the disintegration of his racially mixed biological family rescued by Nanny. The myriad characters of the home are too numerous to outline but they are portrayed by some of the finest actors in the business: Terrence Howard, Rosie Perez, Mos Def, the beautiful Carmen Ejogo, Louis Gossett Jr., Jeffrey Wright, Ernie Hudson, Charlayne Woodward, Jimmy Smits, Patricia Wettig, Macy Gray, Liev Schreiber, Kathleen Chalfant, Lou Myers, Hill Harper - the list goes on and on.<br /><br />In the course of the film we are introduced to the cruelties of racism, the history of desegregation, the dynamics of drug abuse and violence, the infectious joy of African American music contributions to our musical culture, and the courage of one fine woman who battled all the hardships the world can dish out to maintain the dignity of those with whom she came into contact. S. Epatha Merkerson is wholly submerged in this role, a role she makes shine like a beacon of reason in a world of chaos. She offers one of the most stunning performances of the past years, and had this film been released in the theaters instead of as an HBO movie, she without a doubt would add the Oscar to place along side her Golden Globe award.<br /><br />The entire cast is exceptional and Wolfe handles the acting and the story like a master: like riffs in a jazz piece, he pastes tiny moments of conversation with each character and Junior along with flashes of scenes from the story with the matrix of dance fests at the local clubs brimming over the top with incredible blues, jazz, dancing, and joy. The production crew has mounted this little miracle of a picture with extreme care and never for a moment does attention lag from the momentum of the story. Highly Recommended, almost Compulsory Viewing! Grady Harp"""
st2 = "I am kayvan, and this is a test sentence. universiy of tehran. in this sentence I want to check some things"


p = path_analysis(st2, 3)
print p

#deg_cen = dict(Counter(d) + Counter(c))
#print type(deg_cen)
#s_deg_cen = sorted(deg_cen.items(), key=operator.itemgetter(1))
#for el in s_deg_cen:
#    print el

#from sklearn.feature_extraction.text import TfidfVectorizer 
#vectorizer = TfidfVectorizer()
#train_x = vectorizer.fit_transform(["this is a test k1", 
#                                    "another test k1", 
#                                    "figure out how test works k1"])
#                                    
#print train_x