import random
#Random Data Fields
sentences=[
    'It was with considerable reluctance that I abandoned in favour of the present undertaking what had long been a favourite project: that of a new edition of Shelton’s “Don Quixote,” which has now become a somewhat scarce book. There are some—and I confess myself to be one—for whom Shelton’s racy old version, with all its defects, has a charm that no modern translation, however skilful or correct, could possess. Shelton had the inestimable advantage of belonging to the same generation as Cervantes; “Don Quixote” had to him a vitality that only a contemporary could feel; it cost him no dramatic effort to see things as Cervantes saw them; there is no anachronism in his language; he put the Spanish of Cervantes into the English of Shakespeare. Shakespeare himself most likely knew the book; he may have carried it home with him in his saddle-bags to Stratford on one of his last journeys, and under the mulberry tree at New Place joined hands with a kindred genius in its pages. But it was soon made plain to me that to hope for even a moderate popularity for Shelton was vain. His fine old crusted English would, no doubt, be relished by a minority, but it would be only by a minority. His warmest admirers must admit that he is not a satisfactory representative of Cervantes. His translation of the First Part was very hastily made and was never revised by him. It has all the freshness and vigour, but also a full measure of the faults, of a hasty production. It is often very literal—barbarously literal frequently—but just as often very loose. He had evidently a good colloquial knowledge of Spanish, but apparently not much more. It never seems to occur to him that the same translation of a word will not suit in every case. It is often said that we have no satisfactory translation of “Don Quixote.” To those who are familiar with the original, it savours of truism or platitude to say so, for in truth there can be no thoroughly satisfactory translation of “Don Quixote” into English or any other language. It is not that the Spanish idioms are so utterly unmanageable, or that the untranslatable words, numerous enough no doubt, are so superabundant, but rather that the sententious terseness to which the humour of the book owes its flavour is peculiar to Spanish, and can at best be only distantly imitated in any other tongue.',
    'Cervantes’ humour is for the most part of that broader and simpler sort, the strength of which lies in the perception of the incongruous. It is the incongruity of Sancho in all his ways, words, and works, with the ideas and aims of his master, quite as much as the wonderful vitality and truth to nature of the character, that makes him the most humorous creation in the whole range of fiction. That unsmiling gravity of which Cervantes was the first great master, “Cervantes’ serious air,” which sits naturally on Swift alone, perhaps, of later humourists, is essential to this kind of humour, and here again Cervantes has suffered at the hands of his interpreters. Nothing, unless indeed the coarse buffoonery of Phillips, could be more out of place in an attempt to represent Cervantes, than a flippant, would-be facetious style, like that of Motteux’s version for example, or the sprightly, jaunty air, French translators sometimes adopt. It is the grave matter-of-factness of the narrative, and the apparent unconsciousness of the author that he is saying anything ludicrous, anything but the merest commonplace, that give its peculiar flavour to the humour of Cervantes. His, in fact, is the exact opposite of the humour of Sterne and the self-conscious humourists. Even when Uncle Toby is at his best, you are always aware of “the man Sterne” behind him, watching you over his shoulder to see what effect he is producing. Cervantes always leaves you alone with Don Quixote and Sancho. He and Swift and the great humourists always keep themselves out of sight, or, more properly speaking, never think about themselves at all, unlike our latter-day school of humourists, who seem to have revived the old horse-collar method, and try to raise a laugh by some grotesque assumption of ignorance, imbecility, or bad taste.',
    "Beginning of dated history—Size of ancient China—Parcelled out into fiefs—Fiefs correspond to modern hien districts— Mesne lords and sub-vassals—Method of migration and colonizing— Course of the Yellow River in 842 B.C.—Distant fiefs in Shan Tung and Chih Li provinces of to-day—A river which subsequently became part of the Grand Canal—The Hwai River system of waters— Europeans always regard China from the sea inwards—Corea, Japan, and Liao Tung unknown in 842 B.C. except, perhaps, to the vassal state in Peking plain—Orthodox Chinese adopting barbarian usages in Shan Tung—Eastern barbarians on the coast to Shanghai—No knowledge of South or West Asia—Left bank of Yellow River was mostly Tartar, except in South Shan Si—Ancient capital in Shan Si—Ancient colonization of the Wei River valleys in Shen Si— Possibilities of Western ideas having been carried by Tartar horsemen from Persia and Turkestan—Traditions of western, eastern, and southern intercourse previous to 842 B.C.—Early knowledge of the River Yang-tsz and its three mouths—Explorations by ancient emperors—Development of China followed much the same normal course as that of Greece or England. The state of Tsin in Shan Si—In 771 B.C.: its ruler escorts the Emperor to his new capital—Only in 671 B.C. does Confucius mention Tsin—Divided from Ts'in by the Yellow River—Important difference between the sounds Tsin and Ts'in—Importance of the whole Yellow River as a natural boundary—The state of Ts'i also engaged in buffer work against Tartar inroads—Remote origin of Ts'i-Ts'in, Tsin, and Ts'i grow powerful as the Emperor grows weaker—The state of Yen in the Peking plain—The founder of Yen immortalized in song—Complete absence of tradition concerning Yen's origin—Its possible relations with Corea and Japan—Centre of political gravity transferred for ever to the north—Tartar movements in Asia generally 800-600 B.C.—Never was a Tarter empire—Reason for using the loose word 'Tartars'—Race divisions then probably very much as now—Attempt to classify the Tartars in definite groups—Ch'wan unknown by any name—Nothing at all was known in China of the north and west: á fortiori of Central Asia",
    'There are several types of intellect, with innumerable variations and combinations. Some see but do not observe. They note effects but look upon them as facts and never seek a cause. Tides lift and rock their boats but they ask not why. They stand at Niagara and view with some outward evidence of delight a stream of water and an awful abyss, but they lift neither their thoughts nor their eyes towards the invisible current of equal volume passing from Nature’s great evaporator, over Nature’s incomprehensible transportation system, back to the mountains, that the rivers may continue to flow to the sea and yet the sea be not full. That class will find little in this volume to commend, and much to criticise. A man is not a pessimist who, when he hears the roar and sees the funnel-shaped cloud, directs his children to the pathway leading to the cyclone cellar. He is not a pessimist who, after noting forty years of boastful planning, realizes that war is inevitable, and urges preparedness. But vithe man is worse than a pessimist—he is a fool—who stands in front of a cyclone, rejoicing in the manifestation of the forces of nature, or faces a world war, expatiating on the greatness of his country and the patriotism and prowess of his countrymen. It is commonly believed that Nero fiddled while Rome burned. Conceding that he did, it was relatively innocent folly compared to the way many Americans fiddled, and fiddled, and fiddled, and fiddled, until Germany was well on the way to world domination. Coming in at fabulous cost and incalculable waste, and saving the situation at the sixtieth minute of the eleventh hour, we not only claim a full day’s pay but seem to resent that those who toiled longer, with no more at stake, are asking that honors be divided.',
    'He remembered it as he had ridden out an hour or so ago, the outskirts with all their depressing ugliness, a cobbled road, a shabby tramcar with a tired horse creeping along a road where dirty children played weary games and shouted shrilly to one another. A miserable region of smoke-begrimed houses and small shops, an unattractive public house at every corner, round which loafed men with the white faces of tired animals, and women dragging babies and shouting abuse to their more venturesome offspring. With painful distinctness he saw it all—the opened factory gates, the belching out of a slatternly mob of shrieking girls and ribald youths, the streets untidy with the refuse of the greengrocers’ shops, the hot, fetid atmosphere of the low-lying town. He closed his eyes—ah, how swiftly it all vanished! In his ears was the pleasant chirping of many insects, the glorious sunshine lay about him like wine, the west wind made music in the woods, one thrush in particular was singing to him blithely from the thatched roof of his cottage—a single throbbing note against a melodious background of the whole woodful of twittering birds. The man smiled to himself, well pleased.',
    'The evening altogether passed off pleasantly to the whole family. Mrs. Bennet had seen her eldest daughter much admired by the Netherfield party. Mr. Bingley had danced with her twice, and she had been distinguished by his sisters. Jane was as much gratified by this as her mother could be, though in a quieter way. Elizabeth felt Jane’s pleasure. Mary had heard herself mentioned to Miss Bingley as the most accomplished girl in the neighbourhood; and Catherine and Lydia had been fortunate enough never to be without partners, which was all that they had yet learnt to care for at a ball. They returned, therefore, in good spirits to Longbourn, the village where they lived, and of which they were the principal inhabitants. They found Mr. Bennet still up. With a book he was regardless of time; and on the present occasion he had a good deal of curiosity as to the event of an evening which had raised such splendid expectations.',
    'During dinner, Mr. Bennet scarcely spoke at all; but when the servants were withdrawn, he thought it time to have some conversation with his guest, and therefore started a subject in which he expected him to shine, by observing that he seemed very fortunate in his patroness. Lady Catherine de Bourgh’s attention to his wishes, and consideration for his comfort, appeared very remarkable. Mr. Bennet could not have chosen better. Mr. Collins was eloquent in her praise. The subject elevated him to more than usual solemnity of manner, and with a most important aspect he protested that “he had never in his life witnessed such behaviour in a person of rank—such affability and condescension, as he had himself experienced from Lady Catherine. She had been graciously pleased to approve of both of the discourses which he had already had the honour of preaching before her. She had also asked him twice to dine at Rosings, and had sent for him only the Saturday before, to make up her pool of quadrille in the evening. Lady Catherine was reckoned proud by many people he knew, but he had never seen anything but affability in her. She had always spoken to him as she would to any other gentleman; she made not the smallest objection to his joining in the society of the neighbourhood nor to his leaving the parish occasionally for a week or two, to visit his relations. She had even condescended to advise him to marry as soon as he could, provided he chose with discretion; and had once paid him a visit in his humble parsonage, where she had perfectly approved all the alterations he had been making, and had even vouchsafed to suggest some herself—some shelves in the closet up stairs.”',
    'But I have one want which I have never yet been able to satisfy, and the absence of the object of which I now feel as a most severe evil, I have no friend, Margaret: when I am glowing with the enthusiasm of success, there will be none to participate my joy; if I am assailed by disappointment, no one will endeavour to sustain me in dejection. I shall commit my thoughts to paper, it is true; but that is a poor medium for the communication of feeling. I desire the company of a man who could sympathise with me, whose eyes would reply to mine. You may deem me romantic, my dear sister, but I bitterly feel the want of a friend. I have no one near me, gentle yet courageous, possessed of a cultivated as well as of a capacious mind, whose tastes are like my own, to approve or amend my plans. How would such a friend repair the faults of your poor brother! I am too ardent in execution and too impatient of difficulties. But it is a still greater evil to me that I am self-educated: for the first fourteen years of my life I ran wild on a common and read nothing but our Uncle Thomas’ books of voyages. At that age I became acquainted with the celebrated poets of our own country; but it was only when it had ceased to be in my power to derive its most important benefits from such a conviction that I perceived the necessity of becoming acquainted with more languages than that of my native country. Now I am twenty-eight and am in reality more illiterate than many schoolboys of fifteen. It is true that I have thought more and that my daydreams are more extended and magnificent, but they want (as the painters call it) keeping; and I greatly need a friend who would have sense enough not to despise me as romantic, and affection enough for me to endeavour to regulate my mind.',
    '“Fear not that I shall be the instrument of future mischief. My work is nearly complete. Neither yours nor any man’s death is needed to consummate the series of my being and accomplish that which must be done, but it requires my own. Do not think that I shall be slow to perform this sacrifice. I shall quit your vessel on the ice raft which brought me thither and shall seek the most northern extremity of the globe; I shall collect my funeral pile and consume to ashes this miserable frame, that its remains may afford no light to any curious and unhallowed wretch who would create such another as I have been. I shall die. I shall no longer feel the agonies which now consume me or be the prey of feelings unsatisfied, yet unquenched. He is dead who called me into being; and when I shall be no more, the very remembrance of us both will speedily vanish. I shall no longer see the sun or stars or feel the winds play on my cheeks. Light, feeling, and sense will pass away; and in this condition must I find my happiness. Some years ago, when the images which this world affords first opened upon me, when I felt the cheering warmth of summer and heard the rustling of the leaves and the warbling of the birds, and these were all to me, I should have wept to die; now it is my only consolation. Polluted by crimes and torn by the bitterest remorse, where can I find rest but in death?',
    '"Too much of yourself in it! Upon my word, Basil, I didnt know you were so vain; and I really cant see any resemblance between you, with your rugged strong face and your coal-black hair, and this young Adonis, who looks as if he was made out of ivory and rose-leaves. Why, my dear Basil, he is a Narcissus, and you—well, of course you have an intellectual expression and all that. But beauty, real beauty, ends where an intellectual expression begins. Intellect is in itself a mode of exaggeration, and destroys the harmony of any face. The moment one sits down to think, one becomes all nose, or all forehead, or something horrid. Look at the successful men in any of the learned professions. How perfectly hideous they are! Except, of course, in the Church. But then in the Church they dont think. A bishop keeps on saying at the age of eighty what he was told to say when he was a boy of eighteen, and as a natural consequence he always looks absolutely delightful. Your mysterious young friend, whose name you have never told me, but whose picture really fascinates me, never thinks. I feel quite sure of that. He is some brainless beautiful creature who should be always here in winter when we have no flowers to look at, and always here in summer when we want something to chill our intelligence. Dont flatter yourself, Basil: you are not in the least like him."'
    'On reaching the library, he found that it was just after five oclock and that the tea had been already brought up. On a little table of dark perfumed wood thickly incrusted with nacre, a present from Lady Radley, his guardians wife, a pretty professional invalid who had spent the preceding winter in Cairo, was lying a note from Lord Henry, and beside it was a book bound in yellow paper, the cover slightly torn and the edges soiled. A copy of the third edition of The St. Jamess Gazette had been placed on the tea-tray. It was evident that Victor had returned. He wondered if he had met the men in the hall as they were leaving the house and had wormed out of them what they had been doing. He would be sure to miss the picture—had no doubt missed it already, while he had been laying the tea-things. The screen had not been set back, and a blank space was visible on the wall. Perhaps some night he might find him creeping upstairs and trying to force the door of the room. It was a horrible thing to have a spy in ones house. He had heard of rich men who had been blackmailed all their lives by some servant who had read a letter, or overheard a conversation, or picked up a card with an address, or found beneath a pillow a withered flower or a shred of crumpled lace.',
    'Alice opened the door and found that it led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw. How she longed to get out of that dark hall, and wander about among those beds of bright flowers and those cool fountains, but she could not even get her head through the doorway; “and even if my head would go through,” thought poor Alice, “it would be of very little use without my shoulders. Oh, how I wish I could shut up like a telescope! I think I could, if I only knew how to begin.” For, you see, so many out-of-the-way things had happened lately, that Alice had begun to think that very few things indeed were really impossible',
    'As she said these words her foot slipped, and in another moment, splash! she was up to her chin in salt water. Her first idea was that she had somehow fallen into the sea, “and in that case I can go back by railway,” she said to herself. (Alice had been to the seaside once in her life, and had come to the general conclusion, that wherever you go to on the English coast you find a number of bathing machines in the sea, some children digging in the sand with wooden spades, then a row of lodging houses, and behind them a railway station.) However, she soon made out that she was in the pool of tears which she had wept when she was nine feet high.',
    'The appearance of our visitor was a surprise to me, since I had expected a typical country practitioner. He was a very tall, thin man, with a long nose like a beak, which jutted out between two keen, grey eyes, set closely together and sparkling brightly from behind a pair of gold-rimmed glasses. He was clad in a professional but rather slovenly fashion, for his frock-coat was dingy and his trousers frayed. Though young, his long back was already bowed, and he walked with a forward thrust of his head and a general air of peering benevolence. As he entered his eyes fell upon the stick in Holmes’s hand, and he ran towards it with an exclamation of joy. “I am so very glad,” said he. “I was not sure whether I had left it here or in the Shipping Office. I would not lose that stick for the world.”',
    'But the dining-room which opened out of the hall was a place of shadow and gloom. It was a long chamber with a step separating the dais where the family sat from the lower portion reserved for their dependents. At one end a minstrel’s gallery overlooked it. Black beams shot across above our heads, with a smoke-darkened ceiling beyond them. With rows of flaring torches to light it up, and the colour and rude hilarity of an old-time banquet, it might have softened; but now, when two black-clothed gentlemen sat in the little circle of light thrown by a shaded lamp, one’s voice became hushed and one’s spirit subdued. A dim line of ancestors, in every variety of dress, from the Elizabethan knight to the buck of the Regency, stared down upon us and daunted us by their silent company. We talked little, and I for one was glad when the meal was over and we were able to retire into the modern billiard-room and smoke a cigarette.',
    'The young Princess Bolkónskaya had brought some work in a gold-embroidered velvet bag. Her pretty little upper lip, on which a delicate dark down was just perceptible, was too short for her teeth, but it lifted all the more sweetly, and was especially charming when she occasionally drew it down to meet the lower lip. As is always the case with a thoroughly attractive woman, her defect—the shortness of her upper lip and her half-open mouth—seemed to be her own special and peculiar form of beauty. Everyone brightened at the sight of this pretty young woman, so soon to become a mother, so full of life and health, and carrying her burden so lightly. Old men and dull dispirited young ones who looked at her, after being in her company and talking to her a little while, felt as if they too were becoming, like her, full of life and health. All who talked to her, and at each word saw her bright smile and the constant gleam of her white teeth, thought that they were in a specially amiable mood that day.',
    'Since the ball he had felt the approach of a fit of nervous depression and had made desperate efforts to combat it. Since the intimacy of his wife with the royal prince, Pierre had unexpectedly been made a gentleman of the bedchamber, and from that time he had begun to feel oppressed and ashamed in court society, and dark thoughts of the vanity of all things human came to him oftener than before. At the same time the feeling he had noticed between his protégée Natásha and Prince Andrew accentuated his gloom by the contrast between his own position and his friend’s. He tried equally to avoid thinking about his wife, and about Natásha and Prince Andrew; and again everything seemed to him insignificant in comparison with eternity; again the question: for what? presented itself; and he forced himself to work day and night at Masonic labors, hoping to drive away the evil spirit that threatened him. Toward midnight, after he had left the countess’ apartments, he was sitting upstairs in a shabby dressing gown, copying out the original transaction of the Scottish lodge of Freemasons at a table in his low room cloudy with tobacco smoke, when someone came in. It was Prince Andrew.',
    'Buck had accepted the rope with quiet dignity. To be sure, it was an unwonted performance: but he had learned to trust in men he knew, and to give them credit for a wisdom that outreached his own. But when the ends of the rope were placed in the stranger’s hands, he growled menacingly. He had merely intimated his displeasure, in his pride believing that to intimate was to command. But to his surprise the rope tightened around his neck, shutting off his breath. In quick rage he sprang at the man, who met him halfway, grappled him close by the throat, and with a deft twist threw him over on his back. Then the rope tightened mercilessly, while Buck struggled in a fury, his tongue lolling out of his mouth and his great chest panting futilely. Never in all his life had he been so vilely treated, and never in all his life had he been so angry. But his strength ebbed, his eyes glazed, and he knew nothing when the train was flagged and the two men threw him into the baggage car.',
    'But it was Dave who suffered most of all. Something had gone wrong with him. He became more morose and irritable, and when camp was pitched at once made his nest, where his driver fed him. Once out of the harness and down, he did not get on his feet again till harness-up time in the morning. Sometimes, in the traces, when jerked by a sudden stoppage of the sled, or by straining to start it, he would cry out with pain. The driver examined him, but could find nothing. All the drivers became interested in his case. They talked it over at meal-time, and over their last pipes before going to bed, and one night they held a consultation. He was brought from his nest to the fire and was pressed and prodded till he cried out many times. Something was wrong inside, but they could locate no broken bones, could not make it out.',
    'At that time it was quite clear in my own mind that the Thing had come from the planet Mars, but I judged it improbable that it contained any living creature. I thought the unscrewing might be automatic. In spite of Ogilvy, I still believed that there were men in Mars. My mind ran fancifully on the possibilities of its containing manuscript, on the difficulties in translation that might arise, whether we should find coins and models in it, and so forth. Yet it was a little too large for assurance on this idea. I felt an impatience to see it opened. About eleven, as nothing seemed happening, I walked back, full of such thought, to my home in Maybury. But I found it difficult to get to work upon my abstract investigations.',
    'It is still a matter of wonder how the Martians are able to slay men so swiftly and so silently. Many think that in some way they are able to generate an intense heat in a chamber of practically absolute non-conductivity. This intense heat they project in a parallel beam against any object they choose, by means of a polished parabolic mirror of unknown composition, much as the parabolic mirror of a lighthouse projects a beam of light. But no one has absolutely proved these details. However it is done, it is certain that a beam of heat is the essence of the matter. Heat, and invisible, instead of visible, light. Whatever is combustible flashes into flame at its touch, lead runs like water, it softens iron, cracks and melts glass, and when it falls upon water, incontinently that explodes into steam.'
    ]
random_words='model carve formation bleed helicopter seminar tank flu chance hospitality predict basketball pawn study superior scale characteristic accident diamond neck fuss bait table abridge temple'
random_words_list=random_words.split(' ')
furnished_sentences=[]
for i in sentences:
    strings=""
    index=0
    while len(strings)<=100:
        strings=strings+i[index]
        index=index+1
    furnished_sentences.append(strings)
sentences=furnished_sentences
#Generation
method_used=[]
encrypted_messages_list=[]
for sentence in sentences:
    #First Caesar
    #Simple Caesar Cipher Encryption
    message_numbers=[]
    shiftkey=random.randint(1, 26)
    message=sentence
    message=message.lower()
    finished_message=[]
    for letter in message:
        finished_message.append(letter)
    #Changing message into number form
    message_numbers=[]
    for letter in finished_message:
        message_num=int(ord(letter)-97)
        if message_num>=0 and message_num<=25:
            message_numbers.append(message_num)
        else:
            message_space=" "
            message_numbers.append(message_space)
    #Encryption
    encryptednumlist=[]
    for letters in message_numbers:
        if isinstance(letters, int) == True:
            encryptednum=(((int(letters))+(int(shiftkey)))%26)+97
            encryptednumlist.append(encryptednum)
        else:
            encryptednumlist.append(message_space)
    #Back to Characters
    encrypted_message=""
    for nums in encryptednumlist:
        if isinstance(nums, int) == True:
            character=chr(int(nums))
            encrypted_message=encrypted_message+character
        else:
            encrypted_message=encrypted_message+" "
    encrypted_messages_list.append(encrypted_message)
    method_used.append(1)
    
    #Second Visionere
    #Visionere Cipher Encrypter
    #Punctuation Warning
    #Keyword lists
    keyword_a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    keyword_b=['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
    keyword_c=['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
    keyword_d=['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
    keyword_e=['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d']
    keyword_f=['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e']
    keyword_g=['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f']
    keyword_h=['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g']
    keyword_i=['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h']
    keyword_j=['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i']
    keyword_k=['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j']
    keyword_l=['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k']
    keyword_m=['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l']
    keyword_n=['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
    keyword_o=['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    keyword_p=['p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    keyword_q=['q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    keyword_r=['r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
    keyword_s=['s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
    keyword_t=['t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
    keyword_u=['u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
    keyword_v=['v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
    keyword_w=['w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']
    keyword_x=['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
    keyword_y=['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']
    keyword_z=['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
    keyword_a_num=[]
    keyword_b_num=[]
    keyword_c_num=[]
    keyword_d_num=[]
    keyword_e_num=[]
    keyword_f_num=[]
    keyword_g_num=[]
    keyword_h_num=[]
    keyword_i_num=[]
    keyword_j_num=[]
    keyword_k_num=[]
    keyword_l_num=[]
    keyword_m_num=[]
    keyword_n_num=[]
    keyword_o_num=[]
    keyword_p_num=[]
    keyword_q_num=[]
    keyword_r_num=[]
    keyword_s_num=[]
    keyword_t_num=[]
    keyword_u_num=[]
    keyword_v_num=[]
    keyword_w_num=[]
    keyword_x_num=[]
    keyword_y_num=[]
    keyword_z_num=[]
    for letter in keyword_a:
        keyword_num=int(ord(letter))-97
        keyword_a_num.append(keyword_num)
    for letter in keyword_b:
        keyword_num=int(ord(letter))-97
        keyword_b_num.append(keyword_num)
    for letter in keyword_c:
        keyword_num=int(ord(letter))-97
        keyword_c_num.append(keyword_num)
    for letter in keyword_d:
        keyword_num=int(ord(letter))-97
        keyword_d_num.append(keyword_num)
    for letter in keyword_e:
        keyword_num=int(ord(letter))-97
        keyword_e_num.append(keyword_num)
    for letter in keyword_f:
        keyword_num=int(ord(letter))-97
        keyword_f_num.append(keyword_num)
    for letter in keyword_g:
        keyword_num=int(ord(letter))-97
        keyword_g_num.append(keyword_num)
    for letter in keyword_h:
        keyword_num=int(ord(letter))-97
        keyword_h_num.append(keyword_num)
    for letter in keyword_i:
        keyword_num=int(ord(letter))-97
        keyword_i_num.append(keyword_num)
    for letter in keyword_j:
        keyword_num=int(ord(letter))-97
        keyword_j_num.append(keyword_num)
    for letter in keyword_k:
        keyword_num=int(ord(letter))-97
        keyword_k_num.append(keyword_num)
    for letter in keyword_l:
        keyword_num=int(ord(letter))-97
        keyword_l_num.append(keyword_num)
    for letter in keyword_m:
        keyword_num=int(ord(letter))-97
        keyword_m_num.append(keyword_num)
    for letter in keyword_n:
        keyword_num=int(ord(letter))-97
        keyword_n_num.append(keyword_num)
    for letter in keyword_o:
        keyword_num=int(ord(letter))-97
        keyword_o_num.append(keyword_num)
    for letter in keyword_p:
        keyword_num=int(ord(letter))-97
        keyword_p_num.append(keyword_num)
    for letter in keyword_q:
        keyword_num=int(ord(letter))-97
        keyword_q_num.append(keyword_num)
    for letter in keyword_r:
        keyword_num=int(ord(letter))-97
        keyword_r_num.append(keyword_num)
    for letter in keyword_s:
        keyword_num=int(ord(letter))-97
        keyword_s_num.append(keyword_num)
    for letter in keyword_t:
        keyword_num=int(ord(letter))-97
        keyword_t_num.append(keyword_num)
    for letter in keyword_u:
        keyword_num=int(ord(letter))-97
        keyword_u_num.append(keyword_num)
    for letter in keyword_v:
        keyword_num=int(ord(letter))-97
        keyword_v_num.append(keyword_num)
    for letter in keyword_w:
        keyword_num=int(ord(letter))-97
        keyword_w_num.append(keyword_num)
    for letter in keyword_x:
        keyword_num=int(ord(letter))-97
        keyword_x_num.append(keyword_num)
    for letter in keyword_y:
        keyword_num=int(ord(letter))-97
        keyword_y_num.append(keyword_num)
    for letter in keyword_z:
        keyword_num=int(ord(letter))-97
        keyword_z_num.append(keyword_num)
    #Asks for message
    message_numbers=[]
    message=sentence
    alpha_chr_len=int(0)
    message=message.lower()
    finished_message=[]
    for letter in message:
        finished_message.append(letter)
    #Changing message into number form
    message_numbers=[]
    for letter in finished_message:
        message_num=int(ord(letter)-97)
        if message_num>=0 and message_num<=25:
            message_numbers.append(message_num)
            alpha_chr_len=int(alpha_chr_len+1)
        else:
            message_space=" "
            message_numbers.append(message_space)
    #Asks what keyword to be used and gives length warning
    random_index=random.randint(0, 24)    
    keyword=random_words_list[random_index]
    keyword=keyword.lower()
    #Makes the keyword into ASCII
    mykeylist=[]
    mykeylistfinished=[]
    variant=0
    for i in keyword:
        numKey=ord(i)-97
        mykeylist.append(numKey)
    lenkeyword=len(keyword)
    for key in range(alpha_chr_len):
        keylistvalues=int(mykeylist[variant])
        mykeylistfinished.append(int(keylistvalues))
        variant=(int(variant+1))%(int(lenkeyword))
    #Encryption using rows and columns
    encrypted_message=[]
    variant=0
    for letters in message_numbers:
        if isinstance(letters, int) == True:
            if keyword_a_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_a_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_b_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_b_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_c_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_c_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_d_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_d_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_e_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_e_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_f_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_f_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_g_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_g_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_h_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_h_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_i_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_i_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_j_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_j_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_k_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_k_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_l_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_l_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_m_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_m_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_n_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_n_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_o_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_o_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_p_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_p_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_q_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_q_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_r_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_r_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_s_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_s_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_t_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_t_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_u_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_u_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_v_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_v_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_w_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_w_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_x_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_x_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_y_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_y_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_z_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_z_num[letters]
                encrypted_message.append(encrypted_message_num)
            else:
                print("ERROR")
            variant=variant+1
        else:
            encrypted_message.append(" ")
    #Making encrypted message back to letters
    encrypted_message_alpha=""
    for num in encrypted_message:
        if isinstance(num, int) == True:
            encrypted_letter=chr((int(num)+97))
            encrypted_message_alpha=encrypted_message_alpha+encrypted_letter
        else:
            encrypted_message_alpha=encrypted_message_alpha+str(" ")
    #Final Display
    encrypted_messages_list.append(encrypted_message_alpha)
    method_used.append(2)
    
    #Third Autokey
    #Autokey Cipher Encrypter
    #Punctuation Warning
    #Keyword lists
    keyword_a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    keyword_b=['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
    keyword_c=['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
    keyword_d=['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
    keyword_e=['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d']
    keyword_f=['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e']
    keyword_g=['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f']
    keyword_h=['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g']
    keyword_i=['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h']
    keyword_j=['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i']
    keyword_k=['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j']
    keyword_l=['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k']
    keyword_m=['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l']
    keyword_n=['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
    keyword_o=['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    keyword_p=['p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    keyword_q=['q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    keyword_r=['r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
    keyword_s=['s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
    keyword_t=['t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
    keyword_u=['u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
    keyword_v=['v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
    keyword_w=['w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']
    keyword_x=['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
    keyword_y=['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']
    keyword_z=['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
    keyword_a_num=[]
    keyword_b_num=[]
    keyword_c_num=[]
    keyword_d_num=[]
    keyword_e_num=[]
    keyword_f_num=[]
    keyword_g_num=[]
    keyword_h_num=[]
    keyword_i_num=[]
    keyword_j_num=[]
    keyword_k_num=[]
    keyword_l_num=[]
    keyword_m_num=[]
    keyword_n_num=[]
    keyword_o_num=[]
    keyword_p_num=[]
    keyword_q_num=[]
    keyword_r_num=[]
    keyword_s_num=[]
    keyword_t_num=[]
    keyword_u_num=[]
    keyword_v_num=[]
    keyword_w_num=[]
    keyword_x_num=[]
    keyword_y_num=[]
    keyword_z_num=[]
    for letter in keyword_a:
        keyword_num=int(ord(letter))-97
        keyword_a_num.append(keyword_num)
    for letter in keyword_b:
        keyword_num=int(ord(letter))-97
        keyword_b_num.append(keyword_num)
    for letter in keyword_c:
        keyword_num=int(ord(letter))-97
        keyword_c_num.append(keyword_num)
    for letter in keyword_d:
        keyword_num=int(ord(letter))-97
        keyword_d_num.append(keyword_num)
    for letter in keyword_e:
        keyword_num=int(ord(letter))-97
        keyword_e_num.append(keyword_num)
    for letter in keyword_f:
        keyword_num=int(ord(letter))-97
        keyword_f_num.append(keyword_num)
    for letter in keyword_g:
        keyword_num=int(ord(letter))-97
        keyword_g_num.append(keyword_num)
    for letter in keyword_h:
        keyword_num=int(ord(letter))-97
        keyword_h_num.append(keyword_num)
    for letter in keyword_i:
        keyword_num=int(ord(letter))-97
        keyword_i_num.append(keyword_num)
    for letter in keyword_j:
        keyword_num=int(ord(letter))-97
        keyword_j_num.append(keyword_num)
    for letter in keyword_k:
        keyword_num=int(ord(letter))-97
        keyword_k_num.append(keyword_num)
    for letter in keyword_l:
        keyword_num=int(ord(letter))-97
        keyword_l_num.append(keyword_num)
    for letter in keyword_m:
        keyword_num=int(ord(letter))-97
        keyword_m_num.append(keyword_num)
    for letter in keyword_n:
        keyword_num=int(ord(letter))-97
        keyword_n_num.append(keyword_num)
    for letter in keyword_o:
        keyword_num=int(ord(letter))-97
        keyword_o_num.append(keyword_num)
    for letter in keyword_p:
        keyword_num=int(ord(letter))-97
        keyword_p_num.append(keyword_num)
    for letter in keyword_q:
        keyword_num=int(ord(letter))-97
        keyword_q_num.append(keyword_num)
    for letter in keyword_r:
        keyword_num=int(ord(letter))-97
        keyword_r_num.append(keyword_num)
    for letter in keyword_s:
        keyword_num=int(ord(letter))-97
        keyword_s_num.append(keyword_num)
    for letter in keyword_t:
        keyword_num=int(ord(letter))-97
        keyword_t_num.append(keyword_num)
    for letter in keyword_u:
        keyword_num=int(ord(letter))-97
        keyword_u_num.append(keyword_num)
    for letter in keyword_v:
        keyword_num=int(ord(letter))-97
        keyword_v_num.append(keyword_num)
    for letter in keyword_w:
        keyword_num=int(ord(letter))-97
        keyword_w_num.append(keyword_num)
    for letter in keyword_x:
        keyword_num=int(ord(letter))-97
        keyword_x_num.append(keyword_num)
    for letter in keyword_y:
        keyword_num=int(ord(letter))-97
        keyword_y_num.append(keyword_num)
    for letter in keyword_z:
        keyword_num=int(ord(letter))-97
        keyword_z_num.append(keyword_num)
    #Asks for message
    message_numbers=[]
    message=sentence
    alpha_chr_len=int(0)
    message=message.lower()
    finished_message=[]
    for letter in message:
        finished_message.append(letter)
    #Changing message into number form
    message_numbers=[]
    message_numbers_letters=[]
    for letter in finished_message:
        message_num=int(ord(letter)-97)
        if message_num>=0 and message_num<=25:
            message_numbers.append(message_num)
            message_numbers_letters.append(message_num)
            alpha_chr_len=int(alpha_chr_len+1)
        else:
            message_space=" "
            message_numbers.append(message_space)
    #Asks what keyword to be used and gives length warning
    random_index=random.randint(0, 24)    
    keyword=random_words_list[random_index]
    keyword=keyword.lower()
    #Makes the keyword into ASCII
    mykeylistfinished=[]
    variant=0
    for i in keyword:
        numKey=ord(i)-97
        mykeylistfinished.append(numKey)
    lenkeyword=len(keyword)
    autokey=alpha_chr_len-lenkeyword
    for key in range(autokey):
        mykeylistfinished.append(message_numbers_letters[variant])
        variant= variant+1
    #Encryption using rows and columns
    encrypted_message=[]
    variant=0
    for letters in message_numbers:
        if isinstance(letters, int) == True:
            if keyword_a_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_a_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_b_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_b_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_c_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_c_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_d_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_d_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_e_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_e_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_f_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_f_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_g_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_g_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_h_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_h_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_i_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_i_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_j_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_j_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_k_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_k_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_l_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_l_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_m_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_m_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_n_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_n_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_o_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_o_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_p_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_p_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_q_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_q_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_r_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_r_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_s_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_s_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_t_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_t_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_u_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_u_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_v_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_v_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_w_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_w_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_x_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_x_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_y_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_y_num[letters]
                encrypted_message.append(encrypted_message_num)
            elif keyword_z_num[0] == mykeylistfinished[variant]:
                encrypted_message_num=keyword_z_num[letters]
                encrypted_message.append(encrypted_message_num)
            else:
                print("ERROR")
            variant=variant+1
        else:
            encrypted_message.append(" ")
    #Making encrypted message back to letters
    encrypted_message_alpha=""
    for num in encrypted_message:
        if isinstance(num, int) == True:
            encrypted_letter=chr((int(num)+97))
            encrypted_message_alpha=encrypted_message_alpha+encrypted_letter
        else:
            encrypted_message_alpha=encrypted_message_alpha+str(" ")
    #Final Display
    encrypted_messages_list.append(encrypted_message_alpha)
    method_used.append(3)

    #Fourth Playfair
    #Playfair Cipher Encryption
    #RSA Generator
    from random import shuffle
    alphabet = [i for i in range(26)]
    shuffle(alphabet)
    alphabet.remove(9)
    #Defines rows and columns for encryption algorithm
    row_1=[alphabet[0],alphabet[1],alphabet[2],alphabet[3],alphabet[4]]
    row_2=[alphabet[5],alphabet[6],alphabet[7],alphabet[8],alphabet[9]]
    row_3=[alphabet[10],alphabet[11],alphabet[12],alphabet[13],alphabet[14]]
    row_4=[alphabet[15],alphabet[16],alphabet[17],alphabet[18],alphabet[19]]
    row_5=[alphabet[20],alphabet[21],alphabet[22],alphabet[23],alphabet[24]]
    column_1=[alphabet[0],alphabet[5],alphabet[10],alphabet[15],alphabet[20]]
    column_2=[alphabet[1],alphabet[6],alphabet[11],alphabet[16],alphabet[21]]
    column_3=[alphabet[2],alphabet[7],alphabet[12],alphabet[17],alphabet[22]]
    column_4=[alphabet[3],alphabet[8],alphabet[13],alphabet[18],alphabet[23]]
    column_5=[alphabet[4],alphabet[9],alphabet[14],alphabet[19],alphabet[24]]
    #Punctuation Warning
    #Asks for message
    message_numbers=[]
    message=sentence
    alpha_chr_len=int(0)
    message=message.lower()
    finished_message=[]
    for letter in message:
        finished_message.append(letter)
    #Changing message into number form
    message_numbers=[]
    for letter in finished_message:
        message_num=int(ord(letter)-97)
        if message_num>=0 and message_num<=25:
            message_numbers.append(message_num)
            alpha_chr_len=int(alpha_chr_len+1)
    while 9 in message_numbers:
        j_index= message_numbers.index(9)
        message_numbers.insert(j_index,8)
        message_numbers.remove(9)
    if (alpha_chr_len%2)==1:
        message_numbers.append(16)
        alpha_chr_len=int(alpha_chr_len+1)
    #Encrption Rules
    variant_1=0
    variant_2=1
    encrypted_nums=[]
    for i in range(alpha_chr_len//2):
        first_num=message_numbers[variant_1]
        second_num=message_numbers[variant_2]
        #Two_Letter Rule
        if first_num==second_num:
            second_num=ord('q')-97
        #Rule 2
        if (first_num in row_1) and (second_num in row_1):
            first_num_index=int(row_1.index(first_num))
            second_num_index=int(row_1.index(second_num))
            encrypted_letter_1=row_1[((first_num_index)+1)%5]
            encrypted_letter_2=row_1[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        elif (first_num in row_2) and (second_num in row_2):
            first_num_index=int(row_2.index(first_num))
            second_num_index=int(row_2.index(second_num))
            encrypted_letter_1=row_2[((first_num_index)+1)%5]
            encrypted_letter_2=row_2[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        elif (first_num in row_3) and (second_num in row_3):
            first_num_index=int(row_3.index(first_num))
            second_num_index=int(row_3.index(second_num))
            encrypted_letter_1=row_3[((first_num_index)+1)%5]
            encrypted_letter_2=row_3[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        elif (first_num in row_4) and (second_num in row_4):
            first_num_index=int(row_4.index(first_num))
            second_num_index=int(row_4.index(second_num))
            encrypted_letter_1=row_4[((first_num_index)+1)%5]
            encrypted_letter_2=row_4[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        elif (first_num in row_5) and (second_num in row_5):
            first_num_index=int(row_5.index(first_num))
            second_num_index=int(row_5.index(second_num))
            encrypted_letter_1=row_5[((first_num_index)+1)%5]
            encrypted_letter_2=row_5[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        #Rule 3
        elif (first_num in column_1) and (second_num in column_1):
            first_num_index=int(column_1.index(first_num))
            second_num_index=int(column_1.index(second_num))
            encrypted_letter_1=column_1[((first_num_index)+1)%5]
            encrypted_letter_2=column_1[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        elif (first_num in column_2) and (second_num in column_2):
            first_num_index=int(column_2.index(first_num))
            second_num_index=int(column_2.index(second_num))
            encrypted_letter_1=column_2[((first_num_index)+1)%5]
            encrypted_letter_2=column_2[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        elif (first_num in column_3) and (second_num in column_3):
            first_num_index=int(column_3.index(first_num))
            second_num_index=int(column_3.index(second_num))
            encrypted_letter_1=column_3[((first_num_index)+1)%5]
            encrypted_letter_2=column_3[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        elif (first_num in column_4) and (second_num in column_4):
            first_num_index=int(column_4.index(first_num))
            second_num_index=int(column_4.index(second_num))
            encrypted_letter_1=column_4[((first_num_index)+1)%5]
            encrypted_letter_2=column_4[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)
        elif (first_num in column_5) and (second_num in column_5):
            first_num_index=int(column_5.index(first_num))
            second_num_index=int(column_5.index(second_num))
            encrypted_letter_1=column_5[((first_num_index)+1)%5]
            encrypted_letter_2=column_5[((second_num_index)+1)%5]
            encrypted_nums.append(encrypted_letter_1)
            encrypted_nums.append(encrypted_letter_2)    
        #Rule 1
        else:
            if first_num in row_1:
                first_num_index=int(row_1.index(first_num))
                if second_num in row_2:
                    second_num_index=int(row_2.index(second_num))
                    encrypted_letter_1=row_1[second_num_index]
                    encrypted_letter_2=row_2[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)   
                elif second_num in row_3:
                    second_num_index=int(row_3.index(second_num))
                    encrypted_letter_1=row_1[second_num_index]
                    encrypted_letter_2=row_3[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_4:
                    second_num_index=int(row_4.index(second_num))
                    encrypted_letter_1=row_1[second_num_index]
                    encrypted_letter_2=row_4[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_5:
                    second_num_index=int(row_5.index(second_num))
                    encrypted_letter_1=row_1[second_num_index]
                    encrypted_letter_2=row_5[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                else:
                    print("Error")
            elif first_num in row_2:
                first_num_index=int(row_2.index(first_num))
                if second_num in row_2:
                    second_num_index=int(row_2.index(second_num))
                    encrypted_letter_1=row_2[second_num_index]
                    encrypted_letter_2=row_1[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_3:
                    second_num_index=int(row_3.index(second_num))
                    encrypted_letter_1=row_2[second_num_index]
                    encrypted_letter_2=row_3[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_4:
                    second_num_index=int(row_4.index(second_num))
                    encrypted_letter_1=row_2[second_num_index]
                    encrypted_letter_2=row_4[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_5:
                    second_num_index=int(row_5.index(second_num))
                    encrypted_letter_1=row_2[second_num_index]
                    encrypted_letter_2=row_5[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                else:
                    print("Error")
            elif first_num in row_3:
                first_num_index=int(row_3.index(first_num))
                if second_num in row_1:
                    second_num_index=int(row_1.index(second_num))
                    encrypted_letter_1=row_3[second_num_index]
                    encrypted_letter_2=row_1[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_2:
                    second_num_index=int(row_2.index(second_num))
                    encrypted_letter_1=row_3[second_num_index]
                    encrypted_letter_2=row_2[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_4:
                    second_num_index=int(row_4.index(second_num))
                    encrypted_letter_1=row_3[second_num_index]
                    encrypted_letter_2=row_4[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_5:
                    second_num_index=int(row_5.index(second_num))
                    encrypted_letter_1=row_3[second_num_index]
                    encrypted_letter_2=row_5[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                else:
                    print("Error")
            elif first_num in row_4:
                first_num_index=int(row_4.index(first_num))
                if second_num in row_1:
                    second_num_index=int(row_1.index(second_num))
                    encrypted_letter_1=row_4[second_num_index]
                    encrypted_letter_2=row_1[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_2:
                    second_num_index=int(row_2.index(second_num))
                    encrypted_letter_1=row_4[second_num_index]
                    encrypted_letter_2=row_2[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_3:
                    second_num_index=int(row_3.index(second_num))
                    encrypted_letter_1=row_4[second_num_index]
                    encrypted_letter_2=row_3[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_5:
                    second_num_index=int(row_5.index(second_num))
                    encrypted_letter_1=row_4[second_num_index]
                    encrypted_letter_2=row_5[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                else:
                    print("Error")
            elif first_num in row_5:
                first_num_index=int(row_5.index(first_num))
                if second_num in row_1:
                    second_num_index=int(row_1.index(second_num))
                    encrypted_letter_1=row_5[second_num_index]
                    encrypted_letter_2=row_1[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_2:
                    second_num_index=int(row_2.index(second_num))
                    encrypted_letter_1=row_5[second_num_index]
                    encrypted_letter_2=row_2[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_3:
                    second_num_index=int(row_3.index(second_num))
                    encrypted_letter_1=row_5[second_num_index]
                    encrypted_letter_2=row_3[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                elif second_num in row_4:
                    second_num_index=int(row_4.index(second_num))
                    encrypted_letter_1=row_5[second_num_index]
                    encrypted_letter_2=row_4[first_num_index]
                    encrypted_nums.append(encrypted_letter_1)
                    encrypted_nums.append(encrypted_letter_2)
                else:
                    print("Error")
            else:
                print("Error")
        variant_1=variant_1+2
        variant_2=variant_2+2
    #Making encrypted message back to letters
    encrypted_message=""
    for num in encrypted_nums:
        encrypted_letter=chr((int(num)+97))
        encrypted_message=encrypted_message+encrypted_letter
    #Final Display
    encrypted_messages_list.append(encrypted_message)
    method_used.append(4)

    #Fifth Cipher Das Code
    #Das Code Encrypter
    #Punctuation Warning
    #Asks for message
    message_numbers=[]
    message=sentence
    alpha_chr_len=int(0)
    message=message.lower()
    finished_message=[]
    for letter in message:
        finished_message.append(letter)
    #Changing message into number form
    message_numbers=[]
    for letter in finished_message:
        message_num=int(ord(letter)-97)
        if message_num>=0 and message_num<=25:
            message_numbers.append(message_num)
            alpha_chr_len=int(alpha_chr_len+1)
        else:
            message_space=" "
            message_numbers.append(message_space)
    #Ask what alphabet to be used
    alphabet_choice=random.randint(1, 10)
    #Alphabet Generator
    alphabet1=['z','a','b','y','x','c','d','w','v','e','f','u','t','g','h','s','r','i','j','q','p','k','l','o','n','m']
    alphabet2=['z','m','a','n','y','l','b','o','x','k','c','p','w','j','d','q','v','i','e','r','u','h','f','s','t','g']
    alphabet3=['g','t','u','h','f','s','v','i','e','r','w','j','d','q','x','k','c','p','y','l','b','o','z','m','a','n']
    alphabet4=['a','z','y','b','c','x','w','d','e','v','u','f','g','t','s','h','i','r','q','j','k','p','o','l','m','n']
    alphabet5=['a','t','n','g','z','h','m','u','b','s','o','f','y','i','l','v','c','r','p','e','x','j','k','w','d','q']
    alphabet6=['f','n','s','a','u','l','h','y','e','o','r','b','v','k','i','x','d','p','q','c','w','j','t','m','g','z']
    alphabet7=['v','o','h','a','j','c','f','m','t','k','r','y','u','n','w','p','i','b','g','d','e','l','s','z','q','x']
    alphabet8=['d','j','f','l','r','x','w','z','u','o','i','c','g','a','e','k','q','m','s','y','v','p','t','n','h','b']
    alphabet9=['j','e','z','u','p','k','f','a','v','q','l','g','b','w','r','m','h','c','x','s','n','i','d','y','t','o']
    alphabet10=['h','m','r','w','b','g','l','q','v','a','f','k','p','u','z','e','j','o','t','y','d','i','n','s','x','c']
    alphabet1num=[]
    alphabet2num=[]
    alphabet3num=[]
    alphabet4num=[]
    alphabet5num=[]
    alphabet6num=[]
    alphabet7num=[]
    alphabet8num=[]
    alphabet9num=[]
    alphabet10num=[]
    for letter in alphabet1:
        num=ord(letter)-97
        alphabet1num.append(num)
    for letter in alphabet2:
        num=ord(letter)-97
        alphabet2num.append(num)
    for letter in alphabet3:
        num=ord(letter)-97
        alphabet3num.append(num)
    for letter in alphabet4:
        num=ord(letter)-97
        alphabet4num.append(num)
    for letter in alphabet5:
        num=ord(letter)-97
        alphabet5num.append(num)
    for letter in alphabet6:
        num=ord(letter)-97
        alphabet6num.append(num)
    for letter in alphabet7:
        num=ord(letter)-97
        alphabet7num.append(num)
    for letter in alphabet8:
        num=ord(letter)-97
        alphabet8num.append(num)
    for letter in alphabet9:
        num=ord(letter)-97
        alphabet9num.append(num)
    for letter in alphabet10:
        num=ord(letter)-97
        alphabet10num.append(num)
    #Creates a common variable to perform encryption process faster
    if alphabet_choice == 1:
        alphabet_chosen=alphabet1num
    elif alphabet_choice == 2:
        alphabet_chosen=alphabet2num
    elif alphabet_choice == 3:
        alphabet_chosen=alphabet3num
    elif alphabet_choice == 4:
        alphabet_chosen=alphabet4num
    elif alphabet_choice == 5:
        alphabet_chosen=alphabet5num
    elif alphabet_choice == 6:
        alphabet_chosen=alphabet6num
    elif alphabet_choice == 7:
        alphabet_chosen=alphabet7num
    elif alphabet_choice == 8:
        alphabet_chosen=alphabet8num
    elif alphabet_choice == 9:
        alphabet_chosen=alphabet9num
    elif alphabet_choice == 10:
        alphabet_chosen=alphabet10num
    else:
        print("ERROR")
    #Asks for Starting Letter and stores value
    starting_letter_choice=random.randint(97, 122)
    starting_letter=int(starting_letter_choice-97)
    #Asks how to generate keys
    random_num=random.randint(1, 2)
    if random_num==1:
        keyword_gen="KEA"
    else:
        keyword_gen="RNG"
    keyword_gen=keyword_gen.upper()
    if keyword_gen == "KEA":
        #Asks keyword and converts it into all lowercase
        random_index=random.randint(0, 24)    
        mystr=random_words_list[random_index]
        mystr=mystr.lower()
        #Makes the keyword into ASCII
        mykeylist=[]
        mykeylist1=[]
        for i in mystr:
            numKey=ord(i)-97
            mykeylist.append(numKey)
            mykeylist1.append(numKey)
        #Keyword Elongation Algorithm start
        #SEQUENCE 1 Starts
        # +1 
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+1)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -1
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-1)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +2
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+2)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -2
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-2)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +3
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+3)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -3
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-3)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +4
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+4)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -4
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-4)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +5
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+5)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -5
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-5)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +6
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+6)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -6
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-6)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +7
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+7)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -7
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-7)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +8
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+8)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -8
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-8)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +9
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+9)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -9
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-9)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +10
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+10)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -10
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-10)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +11
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+11)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -11
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-11)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +13
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+13)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -13
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-13)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +14
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+14)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -14
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-14)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +15
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+15)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -15
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-15)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +17
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+17)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -17
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-17)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +19
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+19)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -19
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-19)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +21
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+21)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -21
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-21)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +22
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+22)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -22
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-22)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +23
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+23)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -23
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-23)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +25
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+25)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -25
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-25)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +26
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+26)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -26
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-26)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 1 Ends

        #SEQUENCE 2 Starts
        # +2
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+2)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -2
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-2)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +4
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+4)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -4
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-4)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +6
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+6)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -6
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-6)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +8
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+8)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -8
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-8)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +10
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+10)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -10
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-10)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +14
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+14)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -14
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-14)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +22
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+22)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -22
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-22)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +26
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+26)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -26
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-26)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 2 End

        #SEQUENCE 3 Start
        # +3
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+3)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -3
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-3)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +6
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+6)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -6
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-6)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +9
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+9)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -9
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-9)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +15
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+15)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -15
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-15)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +21
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+21)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -21
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-21)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 3 End

        #SEQUENCE 4 Start
        # +4
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+4)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -4
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-4)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +8
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+8)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -8
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-8)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 4 End

        #SEQUENCE 5 Start
        # +5
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+5)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -5
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-5)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +10
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+10)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -10
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-10)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +15
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+15)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -15
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-15)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +25
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+25)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -25
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-25)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 5 End

        #SEQUENCE 6 Start
        # +6
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+6)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -6
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-6)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 6 End

        #SEQUENCE 7 Start
        # +7
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+7)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -7
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-7)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +14
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+14)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -14
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-14)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +21
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+21)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -21
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-21)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 7 End

        #SEQUENCE 8 Start
        # +8
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+8)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -8
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-8)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 8 End

        #SEQUENCE 9 Start
        # +9
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+9)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -9
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-9)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 9 End

        #SEQUENCE 10 Start
        # +10
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+10)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -10
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-10)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 10 End

        #SEQUENCE 11 Start
        # +11
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+11)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -11
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-11)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +22
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+22)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -22
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-22)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 11 End

        #SEQUENCE 12 Start
        # +12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -12
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-12)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 12 End

        #SEQUENCE 13 Start
        # +13
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+13)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -13
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-13)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # +26
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+26)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -26
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-26)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 13 End

        #SEQUENCE 14 Start
        # +14
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+14)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -14
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-14)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 14 End

        #SEQUENCE 15 Start
        # +15
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+15)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -15
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-15)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 15 End

        #SEQUENCE 16 Start
        # +16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -16
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-16)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 16 End

        #SEQUENCE 17 Start
        # +17
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+17)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -17
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-17)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 17 End

        #SEQUENCE 18 Start
        # +18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -18
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-18)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 18 End

        #SEQUENCE 19 Start
        # +19
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+19)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -19
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-19)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 19 End

        #SEQUENCE 20 Start
        # +20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x+20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -20
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-20)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 20 End

        #SEQUENCE 21 Start
        # +21
        changedkeylist=mykeylist1
        for i,x in enumerate(changedkeylist):
            newvalue=(x+21)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -21
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-21)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 21 End

        #SEQUENCE 22 Start
        # +22
        changedkeylist=mykeylist1
        for i,x in enumerate(changedkeylist):
            newvalue=(x+22)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -22
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-22)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 22 End

        #SEQUENCE 23 Start
        # +23
        changedkeylist=mykeylist1
        for i,x in enumerate(changedkeylist):
            newvalue=(x+23)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -23
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-23)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 23 End

        #SEQUENCE 24 Start
        # +24
        changedkeylist=mykeylist1
        for i,x in enumerate(changedkeylist):
            newvalue=(x+24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -24
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-24)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 24 End

        #SEQUENCE 25 Start
        # +25
        changedkeylist=mykeylist1
        for i,x in enumerate(changedkeylist):
            newvalue=(x+25)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -21
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-25)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 25 End

        #SEQUENCE 26 Start
        # +26
        changedkeylist=mykeylist1
        for i,x in enumerate(changedkeylist):
            newvalue=(x+26)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        # -26
        changedkeylist=mykeylist1
        for i, x in enumerate(changedkeylist):
            newvalue=(x-26)%26
            changedkeylist[i]=newvalue
        mykeylist=mykeylist+changedkeylist
        #SEQUENCE 26 End
        #Keyword Elongation Algorithm end
        length_limit=len(mykeylist)
        keys=mykeylist
    else:
        #RNG Generation
        keynums=[]
        for nums in range(alpha_chr_len):
            import random
            random_int=int(random.randint(0, 25))
            keynums.append(random_int)
        keys=keynums
    #Encryption Process Starts
    encrypted_num_list=[]
    variant=0
    for letters in message_numbers:
        if isinstance(letters, int) == True:
            start_position=starting_letter
            end_position=letters
            shift_index=int(int(end_position)-int(start_position))
            key_value=keys[variant]
            key_index=alphabet_chosen.index(key_value)
            encrypted_num_index=(int(int(key_index)+shift_index))%26
            encrypted_num=alphabet_chosen[encrypted_num_index]
            encrypted_num_list.append(encrypted_num)
            variant=variant+1
        else:
            encrypted_num_list.append(" ")
    #Encryption Process Ends
    #Making encrypted message back to letters
    encrypted_message=""
    for num in encrypted_num_list:
        if isinstance(num, int) == True:
            encrypted_letter=chr((int(num)+97))
            encrypted_message=encrypted_message+encrypted_letter
        else:
            encrypted_message=encrypted_message+str(" ")
    #Final Display
    encrypted_messages_list.append(encrypted_message)
    method_used.append(5)
print(method_used, encrypted_messages_list)
        
