Kernel.pbMessage(_INTL("Script added by https://www.youtube.com/TheCoolKid19"))
sp = ChooseNumberParams.new
sp.setRange(1, PBSpecies.maxValue)
sp.setInitialValue(1)
sp.setCancelValue(0)
species=Kernel.pbMessageChooseNumber(_INTL("Input the Pokemon Species ID from the Pokemon ID List"),sp)
if species!=0
  params=ChooseNumberParams.new
  params.setRange(1,PBExperience::MAXLEVEL)
  params.setInitialValue(5)
  params.setCancelValue(0)
  level=Kernel.pbMessageChooseNumber(_INTL("Set the Pokémon's level."),params)
  if level>0
    oldspeciesname=PBSpecies.getName(pkmn.species)
    pkmn.species=species
    pkmn.calcStats
    oldname=pkmn.name
    pkmn.name=PBSpecies.getName(pkmn.species) if pkmn.name==oldspeciesname
    pbDisplay(_INTL("{1}'s species was changed to {2}.",oldname,PBSpecies.getName(pkmn.species)))
    pbSeenForm(pkmn)
    pbRefreshSingle(pkmnid)
  end
end