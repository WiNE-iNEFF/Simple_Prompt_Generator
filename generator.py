import random
prompt = '''photorealistic,
dramatic,
dramatic color,
liquid,
Psychedelic,
anime,
render,
detailed,
super detailed,
hyper detailed,
colorful,
atmosphere,
cinematic,
by wlop,
by ilya kuvshinov,
by ismail inceoglu,
by cory loftis,
by akihiko yoshida,
by james gilleard,
by atey ghailan,
by makoto shinkai,
by goro fujita,
by peter mohrbacher,
by greg rutkowski,
by artgerm,
by alphonse mucha,
by peter mohrbacher, 
by hajime sorayama, 
by wayne barlowe, 
by boris vallejo, 
by aaron horkey, 
by gaston bussiere, 
by craig mullins,
art by peter mohrbacher, 
art by ilya kuvshinov,
art by hajime sorayama, 
art by wayne barlowe, 
art by boris vallejo, 
art by aaron horkey, 
art by gaston bussiere, 
art by craig mullins,
art by wlop,
art by ismail inceoglu,
art by cory loftis,
art by akihiko yoshida,
art by james gilleard,
art by atey ghailan,
art by makoto shinkai,
art by goro fujita,
art by peter mohrbacher,
art by greg rutkowski,
art by artgerm,
art by alphonse mucha,
Chromatic aberration,
glitch art,
glitchy,
Space art,
abstract art,
space,
galaxy,
smoke, 
dark fantasy,
ivy, 
flowers,
epic,
stylized,
sketch,
bold sketch,
character design,
ice gate,
central composition,
baroque, art nouveau,
epic sky, 
cinematic light,
hanging vines,
post-apocalypse,
magical,
volumetric fog,
black background,
shadow,
soft shadow,
concept art,
design concept art,
cyberpunk art,
steampunk blueprint,
volumetric,
volumetric lighting,
goddess of illusion,
stunning, 
breathtaking, 
mirrors, 
glass, 
magic circle,
unreal engine,
unreal engine 5,
octane render,
vray render,
arnold render,
houdini,
terragen,
soft painting,
clear focus,
vfx,
8k,
8k 3d,
4k,
4k 3d,
realistic,
super realistic,
hyper realistic,
ufotable art style,
ghibli art style,
mappa art style,
global illumination,
pixiv,
artstation,
trending on pixiv,
tranding on artstation,
ray tracing,
god rays,
rossdraws global illumination,
anime key visual,
action shot,
young girl,
fanbox,
moody lighting,
lord of the rings,
sharp contrast,
light nover,
light nover cover,
Korean light novel,
Japenese light novel,
Korean light novel cover,
Japenese light novel cover,
game,
visual novel,
full body,
full hd,
dream word,
landscape,
beautiful landscape,
realistic landscape,
photorealistic landscape,
photorealistic dramatic,
photorealistic dramatic anime,
photorealistic dramatic anime boy,
photorealistic dramatic anime girl,
photorealistic dramatic liquid anime girl,
photorealistic dramatic liquid anime boy,
horror,
creepy,
scary,
detailed face,
detailed body,
horror art,
scary art,
creepe art,
funny art,
scary art,
ugly art,
block cities,
Funky pop, 
wearing in punk outfit,
Flat Design Vector Illustrations,
Vector Illustrations,
Flat Design,
RPG Item Icons,
Item Icons,
3D Anime Avatar,
round cute face,
horizon zero dawn,
pubg,
minecraft,
player unknown battleground,
call of duty,
battle field,
world war,
world war 2,
world war 3,
counter strike,
Everlasting summer,
Fate/Stay night,
hdr,
fanart,
artworks,
other dimention,
digital painting,
smooth,
radiant light,
gold,
silver,
rose,
ethereal,
diamond,
biomechanical,
microbes,
Anime Avatar, 
Animal T-Shirt Design,
T-Shirt Design,
Nature Landscape Backgrounds - Winter,
Nature Landscape Backgrounds,
Comic Book Characters,
Birthday Card Mockups,
Card Mockups,
Sci-Fi,
Sci-Fi Zoom Backgrounds,
Animal Crossing Characters,
Anime / Manga,
Retro Psychedelic Posters,
Techno Marble,
Synth,
Synthwave art,
Your Name anime art style,
Nature Sunsets,
Sunsets,
Synthwave,'''.splitlines()
vocab = len(prompt)
#num_word = input(f'Max word (Max {vocab - 1}): ')
generated = []
num_word = 17
for i in range(int(num_word)):
	rand = random.randint(0, vocab)
	generated.append(prompt[rand-1])
print(' '.join(generated))
