import sims4.commands

@sims4.commands.Command('m', command_type=sims4.commands.CommandType.Live)
def pb_moveobj(_connection=None):
	command = 'bb.moveobjects'
	sims4.commands.client_cheat(command, _connection)

@sims4.commands.Command('cf', command_type=sims4.commands.CommandType.Live)
def pb_casfull(_connection=None):
	command = '|testingcheats on'
	sims4.commands.client_cheat(command, _connection)
	command = 'cas.fulleditmode'
	sims4.commands.client_cheat(command, _connection)

@sims4.commands.Command('u', command_type=sims4.commands.CommandType.Live)
def pb_unlock(_connection=None):
	command = 'bb.showhiddenobjects'
	sims4.commands.client_cheat(command, _connection)
	command = 'bb.showliveeditobjects'
	sims4.commands.client_cheat(command, _connection)
	command = 'bb.ignoregameplayunlocksentitlement'
	sims4.commands.client_cheat(command, _connection)

@sims4.commands.Command('s', 'super', command_type=sims4.commands.CommandType.Live)
def pb_super(_connection=None):
	command = '|testingcheats on'
	sims4.commands.client_cheat(command, _connection)
	command = 'cas.fulleditmode'
	sims4.commands.client_cheat(command, _connection)
	command = 'bb.moveobjects on'
	sims4.commands.client_cheat(command, _connection)
	command = 'bb.showhiddenobjects'
	sims4.commands.client_cheat(command, _connection)
	command = 'bb.showliveeditobjects'
	sims4.commands.client_cheat(command, _connection)
	command = 'bb.ignoregameplayunlocksentitlement'
	sims4.commands.client_cheat(command, _connection)
	command = 'bb.enablefreebuild'
	sims4.commands.client_cheat(command, _connection)

@sims4.commands.Command('shortcuts', command_type=sims4.commands.CommandType.Live)
def pb_shortcuts(_connection=None):
	output = sims4.commands.CheatOutput(_connection)
	output("--- SHORTCUTS ---\ncf – testingcheats on + cas.fulleditmode\neco <eco lifestyle value> - eco_footpring.set_eco_footpring_state <eco lifestyle value>\nh – headlineeffects off/on\nm – bb.moveobjects\nseason <season value> – seasons.set_season <season value>\nsetskill <skill> <level> – stats.set_skill_level <skill> <level>; for skill name shortcuts type setskill\nshortcuts – list shortcuts\nu – bb.showhiddenobjects + bb.ignoregameplayunlocksentitlement + bb.showliveeditobjects\ns | super – testingcheats on + cas.fulleditmode + bb.moveobjects + bb.showhiddenobjects + bb.showliveeditobjects\n    + bb.ignoregameplayunlocksentitlement + bb.enablefreebuild")

headline:bool = False

@sims4.commands.Command('h', command_type=sims4.commands.CommandType.Live)
def pb_headlineon(_connection=None):
	global headline	
	if headline is False:
		command = 'headlineeffects off'
		sims4.commands.client_cheat(command, _connection)
		headline = True 
	else:
		command = 'headlineeffects on'
		sims4.commands.client_cheat(command, _connection)
		headline = False

@sims4.commands.Command('season', command_type=sims4.commands.CommandType.Live)
def pb_setseason(setseason:str=None, _connection=None):
	output = sims4.commands.CheatOutput(_connection)
	seasons = {'0': 'Summer', '1': 'Fall', '2': 'Winter', '3': 'Spring'}

	if setseason in seasons:
		y=seasons.get(setseason)
		command = "|seasons.set_season {}".format(setseason)
		sims4.commands.client_cheat(command, _connection)
		output("Season set to {}".format(y))
	else:
		output("You need to set a season!\n0 = Summer\n1 = Fall\n2 = Winter\n3 = Spring")	

@sims4.commands.Command('setskill', command_type=sims4.commands.CommandType.Live)
def pb_setskill(skill:str=None, level:int=None, _connection=None):
	output = sims4.commands.CheatOutput(_connection)
	skills = {'acting': 'Major_Acting', 'arch': 'Major_Archaeology', 'baking': 'Major_Baking', 'bowling': 'Skill_Bowling', 'bartending': 'AdultMajor_Bartending', 'charisma': 'AdultMajor_Charisma', 'comedy': 'AdultMajor_Comedy', 'cooking': 'AdultMajor_HomestyleCooking', 'homestylecooking': 'AdultMajor_HomestyleCooking', 'dancing': 'Minor_Dancing', 'dj': 'Major_DJ', 'fabric': 'AdultMajor_Fabrication', 'fitness': 'Skill_Fitness', 'fishing': 'AdultMajor_Fishing', 'flower': 'AdultMajor_FlowerArranging', 'garden': 'AdultMajor_Gardening', 'gourmet': 'AdultMajor_GourmetCooking', 'guitar': 'AdultMajor_Guitar', 'hand': 'AdultMajor_Handiness', 'herb': 'Major_Herbalism', 'juice': 'AdultMinor_JuiceFizzing', 'knit': 'AdultMajor_Knitting', 'logic': 'AdultMajor_Logic', 'media': 'Minor_Media', 'mischief': 'AdultMajor_Mischief', 'painting': 'AdultMajor_Painting', 'parent': 'Major_Parenting', 'pet': 'skill_Dog', 'photo': 'Major_Photography', 'piano': 'AdultMajor_Piano', 'pipe': 'Major_PipeOrgan', 'programming': 'AdultMajor_Programming', 'research': 'Major_ResearchDebate', 'robot': 'Major_Robotics', 'rocketscience': 'AdultMajor_RocketScience', 'selvador': 'Minor_LocalCulture', 'singing': 'Major_Singing', 'vampire': 'VampireLore', 'vet': 'Major_Vet', 'gaming': 'AdultMajor_VideoGaming', 'violin': 'AdultMajor_Violin', 'wellness': 'Major_Wellness', 'writing': 'AdultMajor_Writing', 'creative': 'Skill_Child_Creativity', 'mental': 'Skill_Child_Mental', 'motor': 'Skill_Child_Motor', 'social': 'Skill_Child_Social'}

	if skill in skills:
		if level is not None and level <=10:
			x=skills.get(skill)
			command = "|stats.set_skill_level {} {}".format(x, level)
			sims4.commands.client_cheat(command, _connection)
			output("{} skill set to level {}".format(x, level))
		else:
			output("You need to set a valid level (0-10)!")
	else:
		output("You need to set a skill! Valid shortcuts are {}".format(sorted(skills.keys())))

@sims4.commands.Command('eco', command_type=sims4.commands.CommandType.Live)
def pb_setecolifestyle(setecolifestyle:str=None, _connection=None):
	output = sims4.commands.CheatOutput(_connection)
	ecolifestyles = {'0': 'Green', '1': 'Neutral', '2': 'Industrial'}

	if setecolifestyle in ecolifestyles:
		e=ecolifestyles.get(setecolifestyle)
		command = "|eco_footprint.set_eco_footprint_state {}".format(setecolifestyle)
		sims4.commands.client_cheat(command, _connection)
		output("Eco Lifestyle set to {}".format(e))
	else:
		output("You need to set a eco lifestyle!\n0 = Green\n1 = Neutral\n2 = Industrial")	