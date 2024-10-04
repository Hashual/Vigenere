Comme annoncé dans le rapport ce fichier contient 3 textes de tailles différentes et de buts différents.

Voici le plus petit texte non crypté : 
Voici un message chiffré qui ne contient aucun doublon !

Et sa version cryptée à l'aide de la clé ' Cryptographie '
XFGRBITDEHZIKGTFXYTXVQJPVIEFLIBSTKAJJCRFFSQECT

Si on applique la fonction de Kasiski sur ce plainText le programme nous renvoie : ???
La fonction renvoie ce résultat lorsque le dictionnaire 'repet' est vide.


Voici le texte crypté issu du TD :
XNRDGQZUDN KOPIZTTMRT LKGXPNRLBA OEDFTRBXZA VRRPKQIMAG FRLBNYHCIY
SBGZPLPSLA OZRLLDHAZT TSKUGGURHI UEFPGZCECA WBGOZSKHDB JACOKTDZMQ
IWVANVKEHE JIQBNQRRPP WWMDPPYIFI RSDRZTKUYF WEDSHTBQHB LTLVYFTAUE
AXRAXTNEDS TQHSVSLVZT TIIIPXRQBE ETDBOACEME QBNAJGYTKM MAPLYAVJKQ
CTYEVISQIH VMHBNASSRN GBKOWNZQXM YAUCIYSBGZ PLPSLANMKE THDVMQSDIA
VBOOPLCYWP XAJGYTKMNU HTFRBWLOGY GTROXMEHPA GIVFXNXTRQ TOGERSLVMO
GYGTROXMEH ZCFWSBAEOI WGXMCGZNJN XABTYESMTM CDGASMXYTT YOGAURIHVP
DAZFWRFUJP SMRHZNHARU ZEKHHJXUII JHEWSNTSRN GKUXDSJUVK UYEUKEUAGF
QLVTFPRQNP RRNQTIDRCD ZIXUXTFTKM SMIHVMDBOO PLCYDLBMCC VDFWSBJTVR
LHKPHCYEPM YAUTYESZKE TNKMHBNASS WOUJXQPKZN JUUPTRECUG VFDSPSWMSE
DFKEQQTHDL MEVWRHXNXC DZKRJLCYFW TEIRLCWMJB GOSLHUYUCP LRHUGFWEDA
WQIEIHVBHA ZWCONNEMOZ VIETHOKDUA TTRZOLPTZO Q

Dans ce cas de ce test nous ne connaissons pas la clé de déchiffrement seulement sa taille qui est de 8.
Nous appliquons donc la méthode de Kasiski dessus afin de voir si le programme renvoie la bonne taille de clé.


Une fois passé dans la fonction de Kasiski le programme retourne le résultat suivant :
Clé potentielle : 2, Occurrence du diviseur : 110
Clé potentielle : 4, Occurrence du diviseur : 107
Clé potentielle : 8, Occurrence du diviseur : 106
Clé potentielle : 3, Occurrence du diviseur : 51
Clé potentielle : 6, Occurrence du diviseur : 49

On voit donc que la méthode de Kasiski est relativement précise avec un texte de taille moyenne puisque la taille de la clé connue 8 est le troisième résultat proposé par le programme
Le but de ce jeu d'essai est de déterminer la précision de la méthode de Kasiski avec une taille de clé connue.



Voici maintenant le texte le plus long non crypté. Il va permettre de déterminer si la méthode renvoie le bon résultat mais aussi si le temps de traitementdu programme n'est pas trop élevé:

Il était une fois, dans un petit village niché au cœur des montagnes, une jeune fille appelée Lina. Lina n'était pas comme les autres enfants de son âge. Tandis que ses camarades jouaient dans les champs et couraient après les papillons, Lina passait des heures à rêver et à observer les étoiles. Elle avait une curiosité insatiable pour tout ce qui se passait au-delà de l’horizon visible.
Un jour, en explorant une partie isolée de la forêt qui bordait le village, Lina découvrit un vieux livre couvert de poussière, abandonné sous un grand chêne. La couverture du livre portait un titre mystérieux : "Le Voyage des Mondes Inconnus". Fascinée, elle s’empressa de rentrer chez elle pour commencer à le lire. À peine avait-elle ouvert la première page qu'une lueur étrange enveloppa la pièce, et en un instant, Lina se retrouva dans un autre monde.
Ce nouveau monde était bien différent du sien. Le ciel était d’un violet profond, parsemé d’étoiles brillantes même en plein jour. Les arbres étaient immenses, leurs feuilles d'un bleu saphir, et l’air était empli de sons étranges, comme des murmures. Lina réalisa qu’elle était partie pour un voyage extraordinaire.
Très vite, elle rencontra un guide inattendu : un petit renard argenté, aux yeux perçants et à la fourrure scintillante comme la lumière des étoiles. Il parlait doucement mais avec une grande sagesse.
— "Bienvenue dans le Monde des Mystères", dit-il. "Peu de mortels ont l'occasion de venir ici. Ce livre que tu as trouvé est en fait une clé. Il ouvre la porte vers des royaumes que les humains ne peuvent normalement pas atteindre. Mais attention, ton voyage ne sera pas facile."
Lina, bien que légèrement effrayée, était déterminée à découvrir ce que ce monde avait à offrir. Le renard lui expliqua qu'elle devait traverser plusieurs terres, chacune régie par des lois différentes et peuplée d'êtres fantastiques. Son but : retrouver la Grande Clef des Étoiles, un artefact magique capable de dévoiler les plus grands secrets de l’univers.
La première terre qu'elle traversa était celle des Rivières Chantantes. Les eaux cristallines chantaient des mélodies envoûtantes, et les poissons nageaient en rythme avec la musique. Mais le danger guettait, car quiconque se laissait emporter par les chants des rivières perdait rapidement son chemin. Grâce à son guide, Lina résista à la tentation et poursuivit sa route.
Elle arriva ensuite dans la Forêt des Illusions. Ici, chaque pas semblait la ramener en arrière, et les arbres changeaient constamment d'apparence. Les habitants de la forêt, des esprits malicieux, se moquaient d'elle et tentaient de la désorienter. Mais Lina, armée de patience et de persévérance, finit par déjouer leurs tours et trouva une sortie.
Son voyage la mena alors à la Montagne des Souvenirs, un lieu où l’air était chargé d’émotions passées. En gravissant la montagne, Lina revécu des moments oubliés de son enfance, des souvenirs heureux et tristes. Elle comprit que pour avancer, elle devait accepter son passé et ne pas se laisser envahir par la nostalgie. Ce n’est qu’en atteignant le sommet qu'elle trouva un indice crucial pour la suite de son aventure : une inscription ancienne qui parlait d’un portail caché sous les étoiles.
Après plusieurs jours de marche, Lina et le renard arrivèrent enfin à la Vallée des Ombres Silencieuses, où régnait une nuit éternelle. Les étoiles brillaient intensément ici, mais aucun bruit ne troublait le silence oppressant. Au centre de la vallée se trouvait un immense lac sombre, et au milieu du lac, sur une petite île, se dressait un vieux temple en ruines.
— "C’est ici que se trouve la Grande Clef des Étoiles", murmura le renard. "Mais pour l’atteindre, tu devras affronter la Gardienne des Ombres."
Sans hésiter, Lina s’approcha du lac. Lorsqu'elle posa le pied sur l’île, une silhouette émergea des ténèbres. C’était la Gardienne, une femme d'une beauté surnaturelle, mais ses yeux étaient remplis de tristesse et de douleur.
— "Pourquoi cherches-tu la Grande Clef ?", demanda la Gardienne d'une voix douce mais autoritaire.
— "Je veux comprendre les mystères de l’univers", répondit Lina, avec sincérité. "Je veux savoir ce qui se cache au-delà des étoiles."
La Gardienne la regarda en silence pendant un long moment, puis, d'un geste lent, elle tendit la main. Une lumière scintillante apparut entre ses doigts : c’était la Grande Clef des Étoiles.
— "Cette clef te donnera des réponses, mais elle te montrera aussi des vérités que tu pourrais préférer ignorer. Es-tu prête à tout voir ?"
Lina, bien que troublée, hocha la tête. Elle était prête à accepter les révélations, quelles qu’elles soient. La Gardienne lui remit la clef, et en un instant, le ciel au-dessus de la vallée changea. Les étoiles se mirent à scintiller de mille feux, dessinant des constellations qu’elle n’avait jamais vues auparavant. Des mondes lointains, des galaxies inconnues, des histoires anciennes se dévoilaient devant elle. Mais avec ces merveilles, elle vit aussi la fragilité de l'existence, les cycles de création et de destruction, et la place infime de l'humanité dans l'immensité de l'univers.
Quand la vision s’estompa, Lina se sentit plus humble, mais aussi remplie d’une profonde compréhension. Elle savait qu’elle ne pourrait jamais tout connaître, mais que son voyage l’avait changée à jamais.
Le renard s’approcha d’elle, son regard empreint de sagesse.
— "Tu as obtenu ce que tu cherchais. Maintenant, il est temps de rentrer chez toi."
Lina acquiesça. Avec la clef en main, elle sentit un pouvoir étrange l’envelopper. En un clin d'œil, elle se retrouva à nouveau dans sa chambre, le vieux livre fermé sur ses genoux. Tout semblait exactement comme avant, sauf que désormais, Lina savait qu'il existait bien plus que ce que l'œil pouvait voir.
Elle regarda par la fenêtre, vers les étoiles, et un sourire se dessina sur ses lèvres. Ses aventures dans le Monde des Mystères resteraient gravées en elle pour toujours, et elle savait qu'un jour, peut-être, elle y retournerait pour continuer à explorer les merveilles cachées de l’univers.


Voici à quoi ressemble le texte une fois crypté grâce à la clé "Etsilepoissonrougesavaitquiltourneenronddanssonbocal" de taille 52 :

MEWBLMIIVWXCVJRUTWMNKEBBJPQWEOAVAMGUVOHFXRQWKABOHCGYILMVPNTIVWXWYCSUVTWLZETBDUTTGOHVGEMGGOFFRMZWDSFBIVRPWXFNLRIGLWKCARUYZEFDDSYNUMMDVOGREEHRJXBXDIRFLRNOGNEDGASUAWTHKGMFNZSHZEHRZSTXIJIABZFFAWPVEOCDVSNALRRTVGUCILSZPZTFMLSCOJSLBIJLZSMMECTPLSFCREZNZHHQHCHJACFJHGIYWTLQLFASXGMFGFINIIIUDSMIQMALBHULQIPNUSYKRRVRGBIJGKBWINFRZYGSVWPDYFFUTXMNZPIKJCMTLCFVRHIYRTBUHTDMAPBSRCIEPXNQWPPUMDABNUSWUYNRDTCGLCMFQZCMEIGBLJRUWDRHGIFTWGRPEUSVOSCBMKGIFLBAXEFDXHMGUFINHIPVEXYEVRHOLVEWHCEUOKTFRMABCIBMALWFVVIRRINOTAOXTYAXHBXVFMRPFBAXVFNKUWAFSGLWILWUAVTGASVSEVBNXIJCCEHXBFMAHILTBQQREQRUDLRDAFRBDGIYITNITXTZTWGIIVFNREHRZMQXHYXLZSKLHRIYLSHUHTESFURFBXEWSIHIWEEWMUWSGVBOTMFSOAVMBCVLLSLVGVSHMOQDQSHFSIGSSOOYHXUMYSJJMSMABERYKXSIOBQXDXQQYSLVAXHHJWRQOEPAWZRUOKTOYGNQZPTHXJGTBERJGVKEHELXJIQWXGVIVPPNEHRVPEZWWBCMSKNUSNJTPWPFJJWGRKOCKRLIHMMGIYAWXILJSIYVCZRVGUATDSHTORHTVXLTLMGSBSAHRDDFOHWSJNAXJLIYZSMTBQQRUSFPXRZMJSFMWPACITDQDEFIMDDSRKOCZTSROIMIEOZFGJIPNKIROHEDRRQAFOVSSVRPWOABPIAZMJWBPFBNXEMNBUQWUCVLMHYEQYYAGSGLWRRFSFQBFIEYXXSCICTIFHWFPRBNYILAGANHKLZFKSMTVRXVCZNQWEPGEARMONUXMXJMOIHSBGAZRJWFVEJLVIBWEOKPFSHKZEMFRJRFXNRYJOAESUARILKMMMTBDWFIRUOHYPWMJNLXTYAXRGNVEIWQZHVOSEHVWABSHGLDSGLTZGROAAGBQVJYTMJIXIKXBCDCXEOVGYEFKFBXYERKLSAGOKTFRXUTPMACCNJSYRDIXXWVZRAWUMZZROODRWUHVZRVKUZSABFOSREFZXFBYSGAIDWAREHJGWSTOEQGTLMXTWMRGXIAKWBQWOANGMNHSPEDIKSXLWUOKADSYZBUHMWNLUMEUAMCXAYEGIJSIOLHHEGSAHQFHGRXMGWMLHTQWMNFVIQYWYWCZMWGTYIGTWNRBJJEZFYHUEASJRYVWGXAPBICLUJSTDWRRMOCZXJAQEZLULXWNGCVHVWGVFEHVCUSUIAFFGGTIISZOIHZWAKRVWTYXIFTZSMMFYCAESYURXVRJTNQWAFLAEHFGUOYFNLZPXGCCNWFYRULGRVEXLMYTYAPMCCCRWYARFGHIAPLEOTJEWENEISJWISSLWNCVCSLRIKPGUAZHUVOLGYTEIXFUSYXQIIWJGYBDTEXMXJMEIGFMIMSYCSNXENEMSIXJUQEVSFCRHIFIWILHRRKUVNOHCNEILDMDIPIFUJWFKOFRMFENCPTDNITXBNURWQRCCQLHSRFNCHUOPTPWXLTPWECQKKCAJBUMISIZNBXDLGEAAYRIIGYRAHVLQHWEOVTZGDLRZWZRYTHBSAHPRFKAMUOIQCXIYTLBGMRVXIZGCEWHRCSJZRTQJAYXLVMDVXJQWJSFGSLJEATMAXBTYUPGHMFAGLRDWAJUAPWSGBOUWIOIEAVLVTGQKLONCONKRLAOIWGUNXZNFMLVZMGJOERXTRWDZRBFTIGEXFAFMISLSFGYRTIXILDZSQEBOATHBMZPMGUREHHSAFKWAOMOKTWEKSUPRTFMFSFEZSLKILLZSIKRLMDVVUETIEVVBGFRNFLSAZFBVDLTISZPRRSTWKVNSWNGRLSYETTVIZPMRYJRWTEZHFPDLVUASHYGGMZUNSQPRIRMDDSRKHYTXSIZNBWUFIOXGIIVIRGVFZDLSYAFONSAGEOIISBTICQMWLRRGSLYINEMAVVUZQYBHJREHIWFIRUOEHJKHBVFUEEXKGCGEJBMKGFGZSMURNOTAOXBUUPGOUCBVWNCOZRQTNYFSQFGUOFZXFQCWJBTAWIBLZUOVWTVIBVXUZRXRYDBXMBEGCDVSRWKSAHFCVTWLSVEPPAWFLOTESFORSRZVMVKXMDFCGVAXWBLPYLHSQWKCAFBHAYGXVMDWDIDWFWEJVYAVWUSEBMHCAEXGYCYIGBDDELWQHWHCHSOXAYGXJMWPTRMNSWGRQWKTLEMSWGFUADXSNERTEFJSYDLSFWJSAWOJICTTJTLRDGBSDUVVQYTIKTLUMGQNBPBUHRAXPRJCZPHTDMWZYFHTOFZTMVTRSWKWUFHTWURTGUMLILKCBPWSMFAEZREHHUHUAWABFDFKPEMHFIYGXSVFWEHZDUXPSIODCGFIZETWFTNGLRJCHVOEFWLCVMSUAAVXKXWYHWMMJGWFILYHWMVRKAUFQYTSNCRVIARFQDURVNWFROHGNQMGSTLZPZTWWRRJCGHVWSNITXDWQPNGYJBYVRXBNLWUAWFIVUSVECRXDTPPTGMLGWYVGVXMDLVIMGJCVEXBMVZIRGZQVPDIFSMQHOPTUTXGWBCSJPTSAHYVGCRIFCZOXIHYADTBNRHGIAKFRGHLNNSZYFSUEEVHMDLMIIVAEAREGYREUSJMJKUYBLNACCVIYQLZNFVUEMFSCFHKTPMEWAPHGSAKSWGLBPOIMXOEUIBYMYKICERWGRJHVFLQHWKSGSCWVPPTYZLRSSKDWTQVGYZSALZSUNHGCCTZYIRREEUANLVPBMJZNUHGIYHKWBFHTJZSKOSWFITXWRGAOTHXQPGBYURWSZSFRVVAAKZSFJHGRWMGSALTEFWUZOQLZUIPGRNQCXBFMAHGUCRTMRUGHUOIYWMBRTWNHZYXLBPIBSZYWOQVGNKRWBMEAVUNITMZUXNVHVVBAHXNRXWAZFRWNPFXSCEIHIZFSHHISFRIEADSAXISMFQSNRVIRGISZSOIFVWHEJGVEDWXWBOISCCDWIEGCOXUMODCPXHWPPLHOCNKVNERRFOESVWANORCLLKTJLTICBMVMBRMCCDHGUXEUTYMIFMCLZGEMEVXRYHUKUGACSSPDCIEWAXCHHMJWGQVZOTMNEMSZXFIVOBHFZAEEIVQFLQCRJAHRKSXEFBLSDZMGQMIMWFVQUILWAPDMEQXMDXHIZYIWYRUNUGIRFFSYBFGGLVWSMYWXZMFUSCVBXGRLUILWGWGWXXBNGHMWQLBTHVTRDWBGFZNEEIGVQEPPAIAFIAVZOSMWRZSKBDNQWEOHKRETCRFHWHNGJWGRTRQIRXLUMEEXHTSYFNERYIPWFYEAXJIQWXGWVGXIPCSSWHDBFFSEBRGSCIIGVDIHAIAKSYCSNKQGNORMKQUCDLWXVFZIEZHRVTURLMDBVFTATWIJMQIGSZAYBBISLKWLUKRMMUUBZNHPFVVPVEOOLHNDMWHEPIDLPIAGKSEAOBWLSRCZYKXSIOPZXJYILVQYGGIVYVGEHYEYSLWBOGSUPPEWABYTZTWKGBZSHZPSGVRLBUHVPEICIRQMGCOPOHFRLWBHOWPSEEGLTPGXSTSMRRJGOYHWLVVIEBYMNAOHXREPRJSGRLLRKKSZJFGNEELUQYXXZTWJRRDWFRIXEPXLXIMQYTBNURWGBEGGHOLNLACATEWEWPXFIGEXHRSEOVJJOKWSUKAZTLUVEWSMDBRHRJZBLQTNAFGQFGIAWEQAMDMCQWFFIRJRYYLASOOQKUMIYVWYEAIWFVRRYRIYSASAURGVLRMWTWIBOQKSJRTQYYQWRQEQEBYAPEZYMVXEHJGVODFESYWYJHGDPPXPQDXTBKWDSFTMWRIKDZCZXQNQZGSNURHIFKFHFWIBFWHYBDNANIBFNTQTRMDZIZRBCZIVAISTBCGMYLWNVQIPHEWIHUSDMSBQMOXIDMHFAPWICUHSZVEOMKWWNOIBIBOASNAVCRQEVJOHVVIEWEDYJSFUYIIJWQSCRMUGACISBKRKIJNMEBYALOOCKDYIYCSAHSOHJJOVUXCMLMLLWFXRCVFSWGISGGMKQPEAHDPWJTUYCNZEVKQUDQGRWSXNNOKSWIKWVLVSGIHHFBTVUJIDLZSWGHYOLKRYDCVIVEHQHVATWKGRUICSZFMWVFGTECWLIPYSLILSINMIBDNMYTBNZYIWGKSZSVDRJWBGSSTCSISLWTPXBISUEHZSMIESVZCTTSFMQXBGRVRIYCSFHQTVLMBCPIXOTVXLZLRVSTWFJRCCJVIJEIUVVBCVOBZYCYIWRISGURUISSBBVJGAFHTFADERVIETFRCSPOIMXGIDKUZMCFSMLEWIFXSARXXGGMHFFADLLMMWFLGISUWFHPFAGKENAITATKZYFXRYJBVQNZGYLQAFSNOVUEWIWIQAAEEXHJAWBCCIMWYWCZQCXBCTAHIPRVXZBZFROOEEWYOEEORACPTXMYIIFMNWFFCSMKXGIGEAXJOVDHILZEIWRUSFVLNNKMFFFGNEGVXKAPWPJMFLIEVGXGRKLZMWGTYLPLASJGIVRJFRVWEESASAUUTAGIXKMYIAZMHGIEKCOPSMRNEBXBFMDTJUZGUYHEXBXUPRMLSGSSGLWIRJMESJFVWJOVKDIAVUOITQGKYZLXLJCBVIECSFPHRIWAZYFGEANLXWAOIAIVANSEJ

Une fois la méthode de Kasiski appliquée au texte crypté précédent on obtient le résultat suivant:

Clé potentielle : 2, Occurrence du diviseur : 856
Clé potentielle : 4, Occurrence du diviseur : 633
Clé potentielle : 13, Occurrence du diviseur : 504
Clé potentielle : 26, Occurrence du diviseur : 479
Clé potentielle : 52, Occurrence du diviseur : 448

Le programme nous a renvoyé en prenant plus de temps que précédemment mais en une durée de temps rapide. Ici on peut constater que la taille de la clé correcte est la 5ème proposée.

On remarque donc que ce programme possède un problème puisque la clé potentielle de taille 13 est un multiple de la clé potentielle de taille 26 qui est elle même un multiple de la taille de la clé correcte. On voit donc que la méthode utilisé possède ses limites sur un texte de grande taille. 
