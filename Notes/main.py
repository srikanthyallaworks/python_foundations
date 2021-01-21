text = '''Ahab well knew that although his friends at home would think little of
his entering a boat in certain comparatively harmless vicissitudes of
the chase, for the sake of being near the scene of action and giving
his orders in person, yet for Captain Ahab to have a boat actually
apportioned to him as a regular headsman in the hunt—above all for
Captain Ahab to be supplied with five extra men, as that same boat’s
crew, he well knew that such generous conceits never entered the heads
of the owners of the Pequod. Therefore he had not solicited a boat’s
crew from them, nor had he in any way hinted his desires on that head.
Nevertheless he had taken private measures of his own touching all that
matter. Until Cabaco’s published discovery, the sailors had little
foreseen it, though to be sure when, after being a little while out of
port, all hands had concluded the customary business of fitting the
whaleboats for service; when some time after this Ahab was now and then
found bestirring himself in the matter of making thole-pins with his
own hands for what was thought to be one of the spare boats, and even
solicitously cutting the small wooden skewers, which when the line is
running out are pinned over the groove in the bow: when all this was
observed in him, and particularly his solicitude in having an extra
coat of sheathing in the bottom of the boat, as if to make it better
withstand the pointed pressure of his ivory limb; and also the anxiety
he evinced in exactly shaping the thigh board, or clumsy cleat, as it
is sometimes called, the horizontal piece in the boat’s bow for bracing
the knee against in darting or stabbing at the whale; when it was
observed how often he stood up in that boat with his solitary knee
fixed in the semi-circular depression in the cleat, and with the
carpenter’s chisel gouged out a little here and straightened it a
little there; all these things, I say, had awakened much interest and
curiosity at the time. But almost everybody supposed that this
particular preparative heedfulness in Ahab must only be with a view to
the ultimate chase of Moby Dick; for he had already revealed his
intention to hunt that mortal monster in person. But such a supposition
did by no means involve the remotest suspicion as to any boat’s crew
being assigned to that boat.
'''

words = text.split(' ')
counts = {}

for word in words:
  if not counts.get(word):
    counts[word]=1
  else:
    counts[word] += 1

for word in counts:
  if counts[word]>3:
    print(f'{word}: {counts[word]}')

